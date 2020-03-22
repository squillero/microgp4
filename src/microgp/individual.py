# -*- coding: utf-8 -*-
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0 "Kiwi"     #
#  / / / / / __/ /_/ / // /   (!) by Giovanni Squillero and Alberto Tonda   #
# / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         #
# \__  /\____/_/   /__  __/                                                 #
#   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!!" #
#                                                                           #
#############################################################################

# Copyright 2020 Giovanni Squillero and Alberto Tonda
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List, Tuple, Set, Dict, Union, Sequence
from collections import Counter, defaultdict
import warnings
import copy

import networkx as nx

from .abstract import Paranoid, Pedantic
from .common_data_structures import Frame
from .constraints import Constraints, Section, RootSection, MacroPool
from .macro import Macro
from .node import NodeID
from .parameter import Information, Structural
from .properties import Properties
from .simple_tree import SimpleTree, _SimpleNode
from .utils import logging


class GraphWrapper:
    """Namespace for node-related methods & checks

    Args:
        graph (nx.DiGraph): DiGraph that the GraphWrapper contains
        individual (Individual): individual to whom the graph belongs
    """

    def __init__(self, graph: nx.DiGraph, individual: 'Individual') -> None:
        """GraphWrapper builder"""
        self._graph = graph
        self.in_degree = self._graph.in_degree
        self.out_degree = self._graph.out_degree
        self.degree = self._graph.degree
        self._individual = individual

    def __getitem__(self, node: NodeID):
        return self.graph.node_view[node]

    def nodes(self,
              section: Union[Frame, str] = None,
              frame: Union[Frame, str] = None,
              frame_path_limit: int = None,
              only_heads: bool = False,
              data: bool = False) -> Sequence[NodeID]:
        """Get a list of node composing an individual.

        Gets the list of all nodes composing an individual. If section_name is
        specified, limits the list to nodes in frames belonging that section;
        if frame_name is specified, limits the list to nodes in the specified
        frame.

        Args:
            frame (Frame or str): Frame nodes belong to
            section (Section or str): Section nodes belong to
            only_heads (bool): Only returns heads (default False)
        """

        assert not (section and frame), "Can't specify BOTH section_name and frame"
        assert (not frame_path_limit or section or
                frame), "frame_path_limit can only be specified with section_name or frame_name"

        if section:
            if isinstance(section, str):
                section = self._individual.constraints[section]
            node_list = get_nodes_in_section(self._individual, section, frame_path_limit=frame_path_limit)
        elif frame:
            if isinstance(frame, str):
                assert frame in (
                    f.name for f in self._individual.frame_tree.node_dict), "Can't find frame '%s'" % (frame,)
                frame = next(f for f in self._individual.frame_tree.node_dict if f.name == frame)
            node_list = get_nodes_in_frame(self._individual, frame, frame_path_limit=frame_path_limit)
        else:
            node_list = list(self._graph.nodes)

        if only_heads:
            internal_nodes = set(t for f, t, k in self._graph.edges(node_list, keys=True) if k == 'next')
            node_list = [n for n in node_list if n not in internal_nodes]
            pass

        # Both the dict and the list are must be *sorted* in a predictable order!
        if data:
            node_dict = dict()
            for n, d in self._graph.nodes(data=True):
                if n in node_list:
                    d['path'] = self.get_fullpath(n)
                    node_dict[n] = d
            return {k: node_dict[k] for k in sorted(node_dict.keys())}
        else:
            return sorted(node_list)

    def edges(self, *args, **kwargs):
        return sorted(self._graph.edges(*args, **kwargs))

    @property
    def node_view(self):
        warnings.warn("Direct access to the NetworkX NodeView class inside the individual is deprecated", DeprecationWarning, stacklevel=2)
        return self._graph.nodes

    @property
    def edge_view(self):
        warnings.warn("Direct access to the NetworkX EdgeView class inside the individual is deprecated", DeprecationWarning, stacklevel=2)
        return self._graph.edges

    def add_node(self, *args, **kwargs):
        self._graph.add_node(*args, **kwargs)

    def remove_node(self, *args, **kwargs):
        self._graph.remove_node(*args, **kwargs)

    def add_edge(self, *args, **kwargs):
        self._graph.add_edge(*args, **kwargs)

    def remove_edge(self, *args, **kwargs):
        self._graph.remove_edge(*args, **kwargs)


    def get_section(self, node: NodeID) -> Section:
        """Returns the Section a node is in

        Args:
            node (NodeID): NodeID of the node that is contained in the section

        Returns:
            Section to which the known belongs
        """
        return self._graph.nodes[node]['frame_path'][-1].section

    def get_fullpath(self, node: NodeID) -> str:
        """Returns the full path of a node as a string

        Args:
            node (NodeID): NodeID of the node of which I want to know the path

        Returns:
            String of the path of the node
        """
        path = [f.name for f in self._graph.nodes[node]['frame_path']]
        assert path[0] == '', "Internal error: <ROOT> frame is not '' but '%s'" % (path[0],)
        return "/".join([''] + path[1:])

    def is_head(self, node: NodeID) -> bool:
        """Checks if it's the head of a chain of nodes connected through 'next' edges

        Args:
            node (NodeID): node to check

        Returns:
            True if it is head, False otherwise
        """
        incoming_keys = {k for _, _, k in self._graph.in_edges(node, keys=True)}
        return 'next' not in incoming_keys


class Individual(Paranoid, Pedantic):
    """A solution encoded in MicroGP, the unit of selection in the evolutive
    process. Individuals are directed multigraph (`MultiDiGraph` in NetworkX),
    that is, more than one directed edges may connect the same pair of nodes.
    An individual must be finalized to be printed and copied, once it is
    finalized (individual._finalized == True) it can't be modified.

    *What an Individual contains*:

    - `id` (int): is the unique id of the individual

    - `_constraints` (Constraints): is a reference to the constraints used to generate them

    - `_graph` contains a reference to the nx MultiDiGraph. Inside it, node are identified by their unique id (`NodeID` object) and their data are stored as attributes:

        - `macro`: a reference to the macro

        - `parameters`: a dictionary with the actual parameters values

        - `frame_path`: path of the node in the constraints hierarchy

    - `_entry_point` (NodeID): containis the NodeID of the head of the main section (frame)

    - `_operator` (callable): contains the pointer to the operator with which it was created

    - `_parents` (Set[Individual] or None): set of parent individuals from which the individual was created. None if it has no parents

    - `_age` (int): count of how many epochs the individual lived

    - `_canonic_phenotype` (str): phenotype of the individual. It can be retrieved by printing the individual. It must be finalized

    Args:
        constraints: constraints of the individual
        copy_from: Individual to clone (if specified)

    **Examples:**

    - Create a new individual with its constraints

    >>> first_individual = Individual(constraints=constraints)

    - Clone an individual (same graph, same parameter values, different NodeIDs and id)

    >>> copied_individual = Individual(constraints=first_individual.constraints, copy_from=first_individual)

    - Print the phenotype representation of an individual

    >>> print(first_individual)
    """

    _COUNTER = 0

    def __init__(self, constraints: Constraints = None, copy_from: 'Individual' = None) -> None:
        """Individual builder"""
        self._id = Individual._COUNTER
        Individual._COUNTER += 1
        self._finalized = False
        self._valid = None
        self._frame_tree = SimpleTree(Frame('', RootSection()))
        self._age = 0
        self._operator = None
        self._unlinked_nodes = dict()
        self._imported_procs = dict()
        self._canonic_phenotype = None
        if not copy_from:
            self._constraints = constraints
            self._graph = GraphWrapper(graph=nx.MultiDiGraph(), individual=self)
            self._section_counter = Counter()
            self.properties = defaultdict(Properties)
            self._parents = None
            self._canonic_phenotype = None
            self._parents = set()
            self._entry_point = None
        else:
            assert isinstance(copy_from, Individual), '"copy_from" parameter must be an Individual object'
            assert copy_from._finalized, 'The individual to copy from must be finalized'
            # Copy constraints from the original individual
            self._constraints = copy_from._constraints
            # Build an empty graph wrapper
            self._graph = GraphWrapper(graph=nx.MultiDiGraph(), individual=self)

            self.properties = copy.deepcopy(copy_from.properties)

            # Copy the graph of the "copy_from" individual (only nodes)
            self._section_counter = None
            node_translation = self.copy_section_node_structure(copy_from, copy_from._entry_point)
            self._section_counter = copy.deepcopy(
                copy_from._section_counter)  # This line must be placed after the copy of the node structure

            destination_nodes = set(self.graph.nodes())
            self.fill_nodes_with_parameters(copy_from, node_translation, destination_nodes)

            self._parents = {copy_from}
            assert len(self.graph.nodes()) == len(copy_from.graph.nodes()), "Something went wrong"

    @property
    def id(self) -> int:
        return self._id

    @property
    def graph(self) -> GraphWrapper:
        return self._graph

    #@property
    #def graph(self) -> nx.DiGraph:
    #    """Last resort, direct access to Individual's graph."""
    #    return self.graph_wrapper.graph

    @property
    def constraints(self) -> Constraints:
        return self._constraints

    @property
    def frame_tree(self) -> SimpleTree:
        return self._frame_tree

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        """Set the age of the individual"""
        assert value >= 0, "Age value must be >= 0"
        self._age = value

    @property
    def parents(self) -> Union[None, Set['Individual']]:
        return self._parents

    @parents.setter
    def parents(self, parents: Union[None, Set['Individual']]):
        """Set the set of individual parents"""
        self._parents = parents

    @property
    def operator(self) -> callable:
        return self._operator

    @operator.setter
    def operator(self, value):
        """Set the operator used to create this individual"""
        self._operator = value

    @property
    def root_frame(self) -> Frame:
        return self.frame_tree.root.frame

    @property
    def sections(self) -> Sequence[Section]:
        return tuple({f.section for f in self._frame_tree.node_dict})

    @property
    def graph_wrapper(self) -> GraphWrapper:
        return self._graph

    @property
    def entry_point(self) -> NodeID:
        return self._entry_point

    @entry_point.setter
    def entry_point(self, new_entry_point: NodeID):
        """Set the entry point of the main section (first node of the node structure)"""
        assert isinstance(new_entry_point, NodeID), "New entry point must be a NodeID"
        assert self.graph.node_view[new_entry_point], "New entry point is not in the individual"
        self._entry_point = new_entry_point

    @property
    def unlinked_nodes(self):
        return self._unlinked_nodes

    #
    # @unlinked_nodes.setter
    # def unlinked_nodes(self, key, value):
    #     self._unlinked_nodes[key] = value

    def __getattr__(self, attribute: str):
        """Lazy attribute 'fitness' is calculated only when needed using constraint's evaluator

        Args:
            attribute: attribute to be returned

        Returns:
            Requested attribute
        """
        if attribute != 'fitness' and attribute != 'fitness_comment':
            error_msg = "'%s' object has no attribute '%s'" % (self.__class__.__name__, attribute)
            raise AttributeError(error_msg)
        fitness, comment = self.constraints.evaluator(self)
        setattr(self, 'fitness', fitness)
        setattr(self, 'fitness_comment', comment)
        return getattr(self, attribute)

    def __hash__(self):
        assert self._finalized, "Individual %d is unhashable (not yet finalized)" % (self._id,)
        return hash(str(self))

    def is_valid(self) -> bool:
        """Test whole set of `checkers` to validate the individual

        Returns:
            True if the individual have passed all the tests, False otherwise
        """
        if not self._finalized:
            logging.warning("Assessing the validity of a non-finalized individual")
            self.finalize()
        if self._valid is None:
            self._valid = check_individual_validity(self)
        return self._valid

    def get_unique_frame_name(self, section: Union[Section, str]) -> str:
        """Get a name never used in the individual by any other frame

        Args:
            section (Section): section to which the frame refers (Section
                object or name of the section)

        Returns:
            The unique name of the new frame
        """
        if isinstance(section, Section):
            section = section.name
        self._section_counter[section] += 1
        return "%s_%d" % (section, self._section_counter[section])

    def draw(self, *args, edge_color=None, with_labels=True, node_size=700, node_color=None, **kwargs):
        """Draws the individual. All parameters are passed to nx.draw. If `node_color == None` then each `next-chain`
        will be colored with different colors (max 10 colors).
        """
        if not edge_color:
            edge_color = [col for _, _, col in self.graph.edges(data='color', default='red')]
        if not node_color:
            node_color = self.next_chain_colors()
        # Node: try to dray with "spring"
        return nx.draw_circular(self.graph,
                                *args,
                                edge_color=edge_color,
                                with_labels=with_labels,
                                node_size=node_size,
                                node_color=node_color,
                                font_color='white',
                                **kwargs)

    def next_chain_colors(self):
        colors = [
            'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray',
            'tab:olive', 'tab:cyan'
        ]
        node_colors = [''] * len(self.graph.nodes)
        heads = self.check_entry_point()
        known_heads = set(heads)
        index = 0
        real_pos = [k for k in self.graph.graph.nodes()._nodes.keys()]
        while heads:
            node = heads.pop(0)
            while node:
                real_index = real_pos.index(node)
                node_colors[real_index] = colors[index]
                successors = [(label, target) for _, target, label in self.graph.edges(node, keys=True)]
                node = None
                for label, target in successors:
                    if label == 'next':
                        assert node is None, "Multiple next edges"
                        node = target
                    elif self.graph.is_head(target) and target not in known_heads:
                        heads.append(target)
                        known_heads.add(target)
            index = (index + 1) % len(colors)
        return node_colors

    def add_node(self, parent_node: Union[NodeID, None], macro: Macro, frame_path: Sequence[Frame]) -> NodeID:
        """Adds a node in the individual and chains it

        Args:
            parent_node (NodeID or None):  the previous block in the dump, if
            None the node will be the root of the individual
            macro (Macro):  the macro that the node will contain
            frame_path (Sequence of Frame): the full frame path to the section containing the node.

        Returns:
            The NodeID of the node just created
        """
        assert not self._finalized, "Individual has been finalized"
        # creates and links the new node
        new_node = NodeID()
        self.graph.add_node(new_node)
        if parent_node:
            old_next = self.get_next(parent_node)
            if old_next:
                self.graph.remove_edge(parent_node, old_next, 'next')
                self.graph.add_edge(new_node, old_next, 'next', color='black')
            self.graph.add_edge(parent_node, new_node, 'next', color='black')

        # add frame path information
        self.graph.node_view[new_node]['frame_path'] = frame_path

        # add macro information
        self.graph.node_view[new_node]['macro'] = macro
        self.graph.node_view[new_node]['parameters'] = None
        # that's all
        return new_node

    # noinspection PyArgumentList
    def delete_node(self, node_to_delete: NodeID) -> None:
        """Delete the node from the graph and connect the edges of the currently connected nodes

        Args:
            node_to_delete (NodeID): Node to delete
        """
        assert self.graph.node_view[node_to_delete], "This node is not in the graph"
        assert isinstance(node_to_delete, NodeID), "The node to delete must be a NodeID"

        prev = self.get_predecessors(node_to_delete)
        next = self.get_next(node_to_delete)

        # A -> B -> C   remove B
        if prev and next:
            prev = prev[0]
            self.graph.remove_edge(prev, node_to_delete, 'next')
            self.graph.remove_edge(node_to_delete, next, 'next')
            self.graph.add_edge(prev, next, 'next', color='black')
        # A -> B        remove B
        elif prev:
            prev = prev[0]
            self.graph.remove_edge(prev, node_to_delete, 'next')
        #      B -> C   remove B
        elif next:
            self.graph.remove_edge(node_to_delete, next, 'next')

        self.graph.remove_node(node_to_delete)
        assert node_to_delete not in self.graph.nodes(), "The selected node can't be removed"

    def get_section_heads(self) -> Dict[Section, NodeID]:
        internal_nodes = set(t for f, t, k in self.graph.edges(keys=True) if k == 'next')
        return {d[1].section: n for n, d in self.graph.graph.nodes("frame_path") if n not in internal_nodes}

    def convert_node_to_string(self, node: NodeID) -> str:
        """Generates the string with the node's current parameters

        Args:
            node: NodeID of the node to be converted into string

        Returns:
            The string that describes the macro and its parameters of the selected node
        """
        vars_ = dict()
        for parameter_name, parameter in self.graph.node_view[node]['parameters'].items():
            vars_[parameter_name] = parameter.value
            pass
        if self.graph.in_degree(node) > 1 and not self.graph.is_head(node):
            label = self.graph.get_section(node).label_format.format(node=node)
        else:
            label = ''
        return label + self.graph.node_view[node]['macro'].text.format(**vars_)

    def get_next(self, node: NodeID) -> NodeID:
        """Get the successor of node (ie. the next block in the dump)

        Args:
            node (NodeID): NodeID of the node of which I need the next

        Returns:
            NodeID of the next node, None if it is the last one in the graph
        """
        assert isinstance(node, NodeID), "Parameter must be of class 'Node' not %s" % (type(node),)
        assert node.run_paranoia_checks()
        assert len([to for _, to, key in self.graph.edge_view(node, keys=True) if key == 'next'
                    ]) <= 1, "Found more than one next"
        # pretty weird use of a generator, but it could be efficient...
        return next((to for _, to, key in self.graph.edge_view(node, keys=True) if key == 'next'), None)

    def get_successors(self, node: NodeID) -> List[NodeID]:
        """Get the list of al successors of a given node (following next's)

        Args:
            node (NodeID): NodeID of the node of which I need the successors

        Returns:
            The list of NodeID of subsequent nodes, None if there are none
        """
        assert isinstance(node, NodeID), "Node is not a Node!"
        tmp_g = nx.DiGraph(((f, t) for f, t, k in self.graph.edges(keys=True) if k == 'next'))
        successors = list()
        n = list(tmp_g.successors(node))
        while n:
            assert len(n) == 1, "Found more than one next"
            assert isinstance(n[0], NodeID), "Node is not a Node!"
            successors += n
            n = list(tmp_g.successors(n[0]))
        return successors

    def get_predecessors(self, node: NodeID) -> List[NodeID]:
        """Get the list of al predecessors of a given node (following next's)

        Args:
            node (NodeID): NodeID of the node of which I need the predecessors

        Returns:
            The list of NodeID of preceding nodes, None if there are none
        """
        assert isinstance(node, NodeID), "node is not a Node!"
        tmp_g = nx.DiGraph(((f, t) for f, t, k in self.graph.edges(keys=True) if k == 'next'))
        if node not in tmp_g.nodes:
            return []
        predecessors = list()
        n = list(tmp_g.predecessors(node))
        while n:
            assert len(n) == 1, "Found more than one next"
            assert isinstance(n[0], NodeID), "Node is not a Node!"
            predecessors += n
            n = list(tmp_g.predecessors(n[0]))
        return predecessors

    def frames(self, section: Section = None, section_name: str = None) -> Set[Frame]:
        """Get all frames of an individual belonging to a given section

        Args:
            section (Section): limit to frames belonging to the section
            section_name (str): limit to frames belonging to the section (name)

        Returns:
            A set of frames
        """
        return get_frames(self, section=section, section_name=section_name)

    def _initialize_frames(self) -> None:
        """Initialize the frame tree using the frame paths of the nodes"""
        assert all([p for n, p in self.graph.node_view(data='frame_path')]), "One or more nodes have frame_path == None"
        # Calculate paths
        for p in [p for n, p in self.graph.node_view(data='frame_path')]:
            self._frame_tree.add_path(p)

        # Add properties for frames
        for frame in self.frames():
            self.properties[frame].update(frame.section.properties)
            self.properties[frame].checkers.update(frame.section.make_default_checkers())

        # Add properties for macros
        for frame in (frame for frame in self.frames() if isinstance(frame.section, MacroPool)):
            for macro in (m for m in frame.section.macro_pool if m.properties):
                logging.debug(f"Copying props: {frame} <- {macro}")
                logging.debug(macro.properties)
                self.properties[frame].update(macro.properties)

        # Add root properties
        self.properties[self.root_frame].update(self.constraints.global_properties)
        for section in (s for s in self.sections if s != self.root_frame.section and getattr(s, 'instances', None)):
            sec = section.name
            (min_instances, max_instances) = section.instances
            self.properties[self.root_frame].add_checker(
                lambda section_counter_cumulative, **v: section_counter_cumulative[sec] >= min_instances)
            self.properties[self.root_frame].add_checker(
                lambda section_counter_cumulative, **v: section_counter_cumulative[sec] <= max_instances)

    def randomize_macros(self, uninitialized_nodes: Set['Individual'] = None) -> None:
        """Randomize the values of the parameters inside the macros

        Args:
            uninitialized_nodes: set of nodes that contain the parameters to initialize
        """
        if not uninitialized_nodes:
            # Can't use a set [ie. uninitialized_nodes = set(self.graph.nodes()) ]
            uninitialized_nodes = list(self.graph.nodes())
        assert len(uninitialized_nodes) > 0, "You have to pass at least one node in the set"
        for u_node in uninitialized_nodes:
            assert u_node in self.graph.nodes(), "One or more nodes not in the graph"
        # Nodes *need* to be processed in a fully predictable order!
        # TODO: sorted(.)
        for node in uninitialized_nodes:
            macro = self.graph.node_view[node]['macro']
            self.initialize_macros(macro, node)

    def initialize_macros(self, macro: Macro, node: NodeID) -> None:
        """Initialize (randomly) the parameters of the selected macro in the node

        Args:
            macro (Macro): macro that contains the parameters to build and initialize
            node (NodeID): node to initialize
        """
        parameters = dict()
        for parameter_name, parameter_type in macro.parameters_type.items():
            kwargs = dict()
            if issubclass(parameter_type, Structural):
                kwargs["node"] = node
                kwargs["individual"] = self
            parameters[parameter_name] = parameter_type(name=parameter_name, **kwargs)
            if parameter_name == 'reference':
                assert parameters[parameter_name].value, "aaa"
        self.graph.node_view[node]['parameters'] = parameters

    def finalize(self) -> None:
        """Final setup of an individual: manage the pending movable nodes, remove non-visitable nodes from the graph,
            initialize the frame tree and the properties, set the canonical representation of an individual."""
        assert not self._finalized, "Individual already finalized"
        if self.link_movable_nodes() == False:
            self._valid = False
            self._finalized = True
            return
        self.clean_graph()
        self._initialize_frames()
        self.properties[self.root_frame].add_base_builder(
            lambda individual, **v:
            {'macro_list_global': [(d['macro'], d['path']) for n, d in individual.graph.nodes(data=True).items()]})
        self.set_canonical()
        self._finalized = True

    def __str__(self) -> str:
        """Get the phenotype of an individual (string)"""
        assert self._finalized, "Individual can't be converted to str because it is not finalized"
        return self._canonic_phenotype

    def check_entry_point(self) -> List[Union[NodeID, None]]:
        """Check if there is only one head for the main and if it corresponds
        to the previously set `self._entry_point`

        Returns:
            A list with one NodeID or None (the first node of the main)
        """
        assert self._entry_point, "self._entry_point can't be None"
        heads = self.graph.nodes(section='main', only_heads=True)
        assert len(heads) == 1, "Found more than one entry point in Section 'main'"
        assert heads[0] == self._entry_point, \
            f"Entry point doesn't correspond to self._entry_point: {heads[0]} != {self._entry_point}"
        return [self._entry_point]

    def set_canonical(self) -> None:
        """Set the canonical representation of an individual (`self._canonic_phenotype`)"""
        assert not self._canonic_phenotype, "Canonical phenotype already set"
        node_counter = 1
        heads = self.check_entry_point()
        known_heads = set(heads)
        while heads:
            node = heads.pop(0)
            while node:
                node._canonical = node_counter
                successors = [(label, target) for _, target, label in self.graph.edges(node, keys=True)]
                node = None
                for label, target in successors:
                    if label == 'next':
                        assert node is None, "Multiple next edges"
                        node = target
                    elif self.graph.is_head(target) and target not in known_heads:
                        heads.append(target)
                        known_heads.add(target)
                node_counter += 1
        macros = list()
        heads = [self._entry_point]
        known_heads = set(heads)
        while heads:
            node = heads.pop(0)
            while node:
                macros.append(self.convert_node_to_string(node))
                # from .parameter.reference import ExternalReference
                # for parameter in self.graph.raw_nodes[node]['parameters'].values():
                #     if isinstance(parameter, ExternalReference):
                #         self.graph.raw_nodes[parameter.value]
                successors = [(label, target) for _, target, label in self.graph.edges(node, keys=True)]
                node = None
                for label, target in successors:
                    if label == 'next':
                        assert node is None, "Multiple next edges"
                        node = target
                    elif self.graph.is_head(target) and target not in known_heads:
                        heads.append(target)
                        known_heads.add(target)
        self._canonic_phenotype = "\n".join(macros)

    def link_movable_nodes(self) -> Union[bool, None]:
        """Set the value of the parameters of type LocalReference and ExternalReference when the node is movable"""
        if len(self._unlinked_nodes.keys()) == 0:
            return
        # This is the phase in which I setup the nodes of the copied frame/proc and then set the edges from the nodes
        #   already inside the current individual
        # self._unlinked_nodes is a dict containing as key the NodeID of the first node of the next-chain of the nodes
        #   structure to be moved. The value is the tuple containing:
        #   - [0] The NodeID of the node that must have as next the first node of the structure to be moved
        #   - [1] The NodeID of the first node after the structure to be moved
        #   - [2] The frame path that all nodes of next-chain structure will have
        for head in self._unlinked_nodes.keys():
            parent, first_outside, frame_path = self._unlinked_nodes[head]
            # I want to move a set of nodes
            was_entry_point = False
            if parent:
                node_id_to_delete = self.get_next(parent)
            else:
                # Check if the structure to delete is the first part of the main
                if self.graph.node_view[self._entry_point]["frame_path"] == frame_path:
                    node_id_to_delete = self._entry_point
                    was_entry_point = True
                else:
                    return False
            if first_outside:
                # Find the last node of the movable nodes chain
                tmp = head
                while self.get_next(tmp):
                    tmp = self.get_next(tmp)
                last = tmp

            # Save the list of node id of the nodes to delete
            nodes_to_delete = []
            while node_id_to_delete and node_id_to_delete != first_outside:
                nodes_to_delete.append(node_id_to_delete)
                node_id_to_delete = self.get_next(node_id_to_delete)

            # Convert into offsets the LocalReferences that have as destination the nodes to delete
            # Save in node_id_with_params_to_change the list of NodeIDs that have parameters to be changed
            from microgp.parameter import LocalReference
            for node in self.graph.nodes(frame=frame_path[1]):
                for parameter_name, parameter in self.graph.node_view[node]["parameters"].items():
                    if isinstance(parameter, LocalReference):  # and parameter.value in nodes_to_delete:
                        parameter.offset = parameter.value_to_offset()

            for node in nodes_to_delete:
                self.delete_node(node)

            if parent:
                if first_outside:
                    self.graph.remove_edge(parent, first_outside)
                self.graph.add_edge(parent, head, 'next', color='black')
            else:
                if was_entry_point:
                    self._entry_point = head
            if first_outside:
                self.graph.add_edge(last, first_outside, 'next', color='black')

            # Set the frame path for the movable nodes [[and link the local references if there are any]]
            movable_node_id = head
            while movable_node_id and movable_node_id != first_outside:
                self.graph.node_view[movable_node_id]["frame_path"] = frame_path
                movable_node_id = self.get_next(movable_node_id)

            # Change the destinations of the local references that have been changed after the deletion of the nodes
            for node in self.graph.nodes(frame=frame_path[1]):
                for parameter_name, parameter in self.graph.node_view[node]["parameters"].items():
                    if isinstance(parameter, LocalReference) and parameter.offset:
                        parameter.value = parameter.offset_to_value(parameter.offset)
                        if not parameter.value:
                            logging.bare("This individual will ever be not valid")
                            pass
        self._unlinked_nodes = dict()

    def arrange_movable_proc(self, nodes_to_copy_from, source_individual, first_movable_node):
        # The source proc frame will be used as unique key for self._unlinked_procs dict
        # source_proc_frame = source_individual.nodes[nodes_to_copy_from[0]]['frame_path'][1]
        # individual._imported_procs[source_proc_frame] = first_movable_node

        # Build the frame path of each node in the proc
        source_frame_paths = []
        for source_node_id in nodes_to_copy_from:
            source_frame_paths.append(source_individual.nodes[source_node_id]['frame_path'])

        # Set the frame path of each node in the proc
        nodes_count = 0
        node = first_movable_node
        frame_translation = dict()
        while node:
            assert source_frame_paths and len(source_frame_paths) > 0, "No more frame paths available"
            source_frame_path = source_frame_paths.pop(0)
            frame_path = [self.frame_tree.root.frame]
            source_frame_path = source_frame_path[1:]
            for frame in source_frame_path:
                if not frame_translation.get(frame, None):
                    section = frame.section
                    new_frame = Frame(self.get_unique_frame_name(section), section)
                    frame_translation[frame] = new_frame
                frame_path = tuple(frame_path) + tuple([frame_translation[frame]])
            self.graph.node_view[node]['frame_path'] = frame_path
            node = self.get_next(node)
            nodes_count += 1

    def clean_graph(self) -> None:
        """Remove the non-visitable nodes from `self._graph`"""
        visited = []
        heads = self.check_entry_point()
        known_heads = set(heads)
        while heads:
            node = heads.pop(0)
            while node:
                visited.append(node)
                successors = [(label, target) for _, target, label in self.graph.edges(node, keys=True)]
                node = None
                for label, target in successors:
                    if label == 'next':
                        assert node is None, "Multiple next edges"
                        node = target
                    elif self.graph.is_head(target) and target not in known_heads:
                        heads.append(target)
                        known_heads.add(target)
        nodes_to_delete = set(self.graph.node_view) - set(visited)
        for node in nodes_to_delete:
            self.delete_node(node)
            # logging.warning(f"Node {node} has been deleted because it is not connected to the graph")

    def copy_section_node_structure(self, source_individual: 'Individual', source_head: NodeID = None) -> \
            Dict[NodeID, NodeID]:
        """Copy the structure of a section from the `source_individual` to `self`. Used by the builder of the Individual
        when `copy_from` is not `None`.

        Args:
            source_individual (Individual): Individual from which to copy the section structure
            source_head (NodeID): NodeID of the head of the `next-chain` (section)

        Returns:
            The correspondences between source `NodeID`s and destination `NodeID`s
        """
        assert source_individual, "source_individual can't be None"
        assert self._finalized is not True, "Destination individual can't be finalized"

        if not source_head:
            heads = source_individual.check_entry_point()
        else:
            heads = [source_head]
        # node_translation contains as keys the source_individual NodeIDs and as value the correspondent destination
        #   individual NodeIDs
        node_translation = dict()
        known_heads = set(heads)
        while heads:
            source_node_id = heads.pop(0)
            parent = None
            while source_node_id:
                source_node = source_individual.graph.node_view[source_node_id]
                frame_path = source_node['frame_path']
                # Create the node and add it in the graph
                destination_node_id = self.add_node(parent, source_node['macro'], frame_path)
                node_translation[source_node_id] = destination_node_id
                parent = destination_node_id
                # Pick the next node
                successors = [
                    (label, target) for _, target, label in source_individual.graph.edges(source_node_id, keys=True)
                ]
                source_node_id = None
                for label, target in successors:
                    if label == 'next':
                        assert source_node_id is None, "Multiple next edges"
                        source_node_id = target
                    elif source_individual.graph.is_head(target) and target not in known_heads:
                        heads.append(target)
                        known_heads.add(target)
        if source_head == source_individual._entry_point or not source_head:
            self._entry_point = node_translation[source_head]
        return node_translation

    def fill_nodes_with_parameters(self, source_individual: 'Individual', node_translation: Dict[NodeID, NodeID],
                                   destination_nodes: Set[NodeID]):
        # Copy parameters values
        nodes_tot = destination_nodes
        uninitialized_nodes = set(nodes_tot)
        while uninitialized_nodes:
            for destination_node_id in uninitialized_nodes:
                # Create parameters and copy their values
                l = len(self.graph.nodes())
                parameters = self.copy_parameters(source_individual, node_translation, destination_node_id)
                assert len(self.graph.nodes()) == l, f'Parameters: {parameters}, DestNodeID: {destination_node_id}, ' \
                                               f'SrcNodeID: {[k for k, v in node_translation.items() if v == destination_node_id][0]}'
                self.graph.node_view[destination_node_id]['parameters'] = parameters
            uninitialized_nodes = destination_nodes - nodes_tot
            nodes_tot = destination_nodes

    def copy_parameters(self, source_individual: 'Individual', node_translation: Dict[NodeID, NodeID],
                        destination_node_id: NodeID):
        """Create parameters of the given node and copy their values from the original node (=``node_translation.keys()``)

        Args:
            source_individual (Individual): individual that contains the parameter values of the nodes to copy
            node_translation (Dict[NodeID, NodeID]): correspondences between source node ids and destination node ids
            destination_node_id (NodeID): NodeID of the node to copy

        Returns:
            Dictionary that contains the parameters of the new copied node
        """
        assert isinstance(source_individual, Individual), "source_individual must be an Individual object"
        parameters = dict()
        # Get the node to be copied
        source_node_id = [k for k, v in node_translation.items() if v == destination_node_id][0]
        source_node = source_individual.graph.node_view[source_node_id]
        from microgp.parameter import ExternalReference
        # Iterate for each node parameter in the original individual node
        for parameter_name, parameter in source_node['parameters'].items():
            data = dict()
            data["name"] = parameter_name
            if isinstance(parameter, Structural):
                data["individual"] = self
                data["node"] = destination_node_id
                if type(parameter) == Information:
                    pass
                else:
                    # Get the correspondent new NodeID
                    reference_destination = parameter.value
                    assert reference_destination in node_translation.keys(), "Something wrong"
                    # Get the correspondent NodeID belonging to the destination individual
                    new_value = node_translation[reference_destination]
                    if isinstance(parameter, ExternalReference):
                        data["do_not_init"] = True
            else:
                new_value = parameter.value
            new_parameter = type(parameter)(**data)
            if not isinstance(parameter, Information):
                new_parameter.value = new_value
                assert new_parameter.value == new_value, "Something went wrong"
            parameters[parameter_name] = new_parameter
        return parameters

    def create_movable_nodes(self,
                             source_individual: 'Individual',
                             nodes_to_copy_from: List[NodeID],
                             is_new_proc: bool = False) -> NodeID:
        first_node_id = None
        parent = None
        for source_node_id in nodes_to_copy_from:
            source_node = source_individual.graph.node_view[source_node_id]
            new_node_id = self.add_node(parent, source_node["macro"], None)
            self.copy_parameters_movable(source_individual, new_node_id, source_node_id)
            if not first_node_id:
                first_node_id = new_node_id
                if is_new_proc == True:
                    assert first_node_id not in self._imported_procs.values(
                    ), "Node already in self._imported_procs.values()"
                    source_proc_frame = source_individual.nodes[source_node_id]['frame_path'][1]
                    self._imported_procs[source_proc_frame] = first_node_id
            parent = new_node_id
        return first_node_id

    def copy_parameters_movable(self, source_individual: 'Individual', new_node_id: NodeID, source_node_id: NodeID):
        from .parameter.reference import ExternalReference, LocalReference
        source_node = source_individual.graph.node_view[source_node_id]
        parameters = dict()
        for parameter_name, parameter in source_node['parameters'].items():
            data = dict()
            data["name"] = parameter_name
            if issubclass(type(parameter), Structural):
                data["individual"] = self
                data["node"] = new_node_id
                from .parameter import Special
                if issubclass(type(parameter), Special):
                    # NOTE: do not use the same Information, otherwise the set_canonical() will not work properly
                    parameter = type(parameter)(**data)
                elif isinstance(parameter, ExternalReference):
                    # If the parameter is an ExternalReference, then the new proc must be copied
                    first_source_proc_node = parameter.value

                    source_proc_frame = source_individual.nodes[first_source_proc_node]['frame_path'][1]
                    if source_proc_frame in self._imported_procs.keys():
                        # Proc already copied, link the current node to the first node of the proc
                        first_movable_node = self._imported_procs[source_proc_frame]
                    else:
                        # Create the structure of the new procedure
                        # nodes_to_copy_from = get_nodes_visit_order(source_individual, first_source_proc_node)
                        chosen_frame = source_individual.nodes[first_source_proc_node]['frame_path'][1]
                        nodes_to_copy_from = get_nodes_in_frame(source_individual, chosen_frame)

                        # Create movable nodes of the selected proc
                        first_movable_node = self.create_movable_nodes(source_individual,
                                                                       nodes_to_copy_from,
                                                                       is_new_proc=True)
                        assert first_movable_node, "Ops, something went wrong in creation of movable nodes"

                        self.arrange_movable_proc(nodes_to_copy_from, source_individual, first_movable_node)

                    # Set the final_destination of the external reference of the selected node__________________________
                    parameter = type(parameter)(**data)
                    parameter.value = first_movable_node
                elif isinstance(parameter, LocalReference):
                    # Save relative references that will be copied in a second phase. This because if I copy
                    offset = parameter.value_to_offset()
                    if not offset:
                        exit("This should not happen")
                    # Save the offset. The availability of a a valid target for the destination_node will be checked in
                    #   second phase, when the parameter will be created and the nodes structure will be fully created
                    data['offset'] = offset
                    parameter = type(parameter)(**data)
                else:
                    exit("This should not happen")
            else:
                # The non-Structural parameters must be copied in value
                new_value = source_node['parameters'][parameter_name].value
                # data["copy_from"] = new_value
                parameter = type(parameter)(**data)
                parameter.value = new_value
            parameters[parameter_name] = parameter
        self.graph.node_view[new_node_id]["parameters"] = parameters

    def __eq__(self, other: 'Individual'):
        assert self._finalized and other._finalized, "One or more individuals are not finalized"
        return self._canonic_phenotype == other._canonic_phenotype


def get_nodes_in_frame(individual: Individual, frame: Frame, frame_path_limit: int = None) -> List[NodeID]:
    """Gets all nodes of an individual inside a given frame

    Args:
        individual (Individual): the individual
        frame (Frame): the frame
        frame_path_limit (int): how much deep must be the path

    Returns:
        A list of of Nodes
    """
    node_list = list()
    for node, data in individual.graph.node_view("frame_path"):
        if data:
            if frame_path_limit:
                if frame_path_limit > 0:
                    data = data[0:frame_path_limit]
                else:
                    data = data[len(data) + frame_path_limit:]
            if frame in data:
                node_list.append(node)
    return node_list


def get_nodes_in_section(individual: Individual,
                         section: Section,
                         frame_path_limit: int = None,
                         head: bool = False) -> List[NodeID]:
    """Gets all nodes of an individual inside a given frame

    If `frame_path_limit` is set to N with N > 0, only the first N frames are
    considered for the match. If With N < 0, only the last N frames are
    considered for the match.

    Args:
        individual (Individual): the individual
        section (Section): the section
        frame_path_limit (int): limit the frame path
        head (bool): returns only the head of the section

    Returns:
        The list of nodes in the selected section
    """

    node_list = list()
    for node, data in individual.graph.node_view("frame_path"):
        if frame_path_limit:
            if frame_path_limit > 0:
                data = data[0:frame_path_limit]
            else:
                data = data[len(frame_path_limit) + frame_path_limit:]
        if section in (f.section for f in data):
            node_list.append(node)
    return node_list


def get_frames(individual: Individual, section: Section = None, section_name: str = None) -> Set[Frame]:
    """Gets all frames of an individuals belonging to a given section

    Args:
        individual (Individual): the individual
        section (Section): limit to frames belonging to the section
        section_name (str): limit to frames belonging to the section (name)

    Returns:
        A set of frames
    """

    assert not section or not section_name, "section and section_name cannot be both specified"

    if isinstance(section, str):
        section = individual.sections[section]

    frames = set()
    for path in (p for k, p in individual.graph.node_view('frame_path')):
        if path:
            for frame in path:
                if section_name and frame.section.name == section_name:
                    frames.add(frame)
                elif section and frame.section == section:
                    frames.add(frame)
                elif not section and not section_name:
                    frames.add(frame)
    return frames


def get_macro_pool_nodes_count(individual: Individual, frames: Set[Frame] = None) -> Dict[Frame, int]:
    """Get a dict containing {Frame: number_of_macros}. Selects only MacroPools

    Args:
        frames (Set[Frame]): set of frames of which I want the number of nodes
        individual (Frame): Individual from which count the nodes

    Returns:
        Dictionary containing the amount of nodes (value) for each Frame (key)

    :meta private:
    """
    frame_count = dict()
    for node_id, value in individual.graph.node_view().items():
        # Get the last frame (it is always a MacroPool)
        macro_pool = value["frame_path"][len(value["frame_path"]) - 1]
        # Save the number of nodes in that frame
        if not frames or macro_pool in frames:
            frame_count[macro_pool] = len(get_nodes_in_frame(individual, frame=macro_pool))
    return frame_count


def check_individual_validity(individual: Individual) -> bool:
    """Check an individual against its constraints.

    Check the validity of all parameters (e.g., range), then the default
    `Properties` (e.g., number of macros in sections), and finally all the
    custom `Properties` added by the user.

    The result is cached, as individuals must be `finalized` to be checked

    Args:
        individual (Individual): the individual to be checked

    Returns:
        The validity as a boolean value
    """
    # examine all frames in the individual
    values = dict()
    for node, data in individual.graph.node_view(data=True):
        if not all(p.is_valid(p.value) for p in data['parameters'].values()):
            return False
    # logging.debug("*** Checking individual %r" % (individual,))

    for frame in individual.frame_tree.post_order_visit():
        cumulative_values = dict()
        for f in individual.frame_tree.get_sub_frames(frame):
            for k, v in individual.properties[f].cumulative_values.items():
                if k not in cumulative_values:
                    cumulative_values[k] = v
                else:
                    # logging.debug("(merge sibling) %s: %s + %s:%s -> %s" % (k, cumulative_values[k], f.name, v, cumulative_values[k] + v))
                    # Note for a C geek: "cumulative_values[k] += v" did not work -- remember why?
                    cumulative_values[k] = cumulative_values[k] + v
        individual.properties[frame].update_values(individual=individual,
                                                   frame=frame,
                                                   cumulative_values=cumulative_values)

    for frame in individual.frame_tree.post_order_visit():
        # logging.debug("Checking %s" % (frame,))
        # logging.debug("%s" % (individual.properties[frame],))
        if not individual.properties[frame].run_checks():
            return False

    return True


def _update_values(individual: Individual, node: _SimpleNode) -> None:
    cumulative_values = dict()
    for n in node.children:
        _update_values(individual, n)
        for k, v in individual.properties[n.frame].cumulative_values.items():
            if k not in cumulative_values:
                cumulative_values[k] = v
            else:
                # logging.debug("(merge sibling) %s: %s + %s -> %s" % (k, cumulative_values[k], v, cumulative_values[k] + v))
                cumulative_values[k] += v
        # logging.debug("After %s: cumulative = %s" % (n.frame.name, cumulative_values))

    # logging.debug("REC Checking %s" % (node.frame,))
    # logging.debug("In %s: cumulative_values = %s" % (node.frame.name, cumulative_values))
    individual.properties[node.frame].update_values(individual=individual,
                                                    frame=node.frame,
                                                    cumulative_values=cumulative_values)
