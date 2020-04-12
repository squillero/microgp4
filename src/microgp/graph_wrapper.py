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

from typing import List, Set, Dict, Sequence, Optional, Union, Any, Collection
from collections import Counter, defaultdict
from collections import abc
import warnings
import copy

import networkx as nx

from .abstract import Paranoid, Pedantic
from .common_data_structures import Frame
from .constraints import Constraints, Section, RootSection, MacroPool
from .macro import Macro
from .node import NodeID
from .parameter import Parameter, Information, Structural
from .properties import Properties
from .simple_tree import SimpleTree, _SimpleNode
from .utils import logging


class NodeWrapper:
    def __init__(self, node_id: NodeID, data: dict) -> None:
        # Can't use self. as it would recurse __setattr__
        self.__dict__['_id'] = node_id
        self.__dict__['_data'] = data

    @property       # dynamically-created, read-only attribute
    def id(self):
        return self._id

    @property       # dynamically-created, read-only attribute
    def path(self) -> Optional[str]:
        if self._data['frame_path'][0] is not None:
            assert self._data['frame_path'][0].name == '', f"Internal error: <ROOT> frame is not '' but '{self._data['frame_path'][0]}'"
            return '/'.join(p.name for p in self._data['frame_path'])
        else:
            return None  # floating node!

    def __str__(self):
        return f"Node({self.id})"

    def __getattr__(self, attribute: str) -> Any:
        if attribute in self._data:
            # or super().setattr(self, attribute, self._data[attribute])
            self.__dict__[attribute] = self._data[attribute]
        else:
            self.__dict__[attribute] = None
        return self.__dict__[attribute]

    def __setattr__(self, attribute: str, value: Any) -> None:
        #self.__dict__['_data'][attribute] = value
        self._data[attribute] = value

    def __getitem__(self, parameter_name: str) -> Any:
        assert isinstance(parameter_name, str), f"Parameter name should be string (found: {type(parameter_name)})"
        if parameter_name[0] == '$':
            # parameter inside the macro
            if parameter_name[1:] in self._data['parameters']:
                return self._data['parameters'][parameter_name[1:]].value
            else:
                return None
        else:
            return getattr(self, parameter_name)

    def __setitem__(self, parameter_name: str, value: Any) -> None:
        assert isinstance(parameter_name, str), f"Parameter name should be string (found: {type(parameter_name)})"
        self._data[parameter_name] = value



class NodesCollection(abc.Mapping, abc.Set, abc.Callable):
    """A read/write collection of the nodes of an individual quite but not completely different from a NetworkX view

    When used as a dictionary it allows read-only access to NodeViews. E.g.,

        >>> for n in ind.node_list;
        >>>     print(ind.node_list[n]['foo'])
        >>>     ind.node_list[n]['bar'] = 41    # nodes can be modified as a dictionary
        >>>     ind.node_list[n].baz += 1       # or as properties

    When `NodesCollection` is used as a function it allows to select nodes using various filters, e.g.,

        >>> ind.node_list(select_section='main', select_heads=False, data=True)

    Args:
        data: When data is ``None``, the return value is a list of :meth:`microgp.node.NodeID`. When data is ``True``,
            the return value is dictionary of dictionaries ``{node_id: {<all node properties>}}``. When data is the key
            of a node property, the return value is a dictionary ``{node_id: <the specified field>}``

        default: When property selected by data does not exists, the node is included in the result withe the specified
            value. If ``default`` is ``None``, the node is not included in the result.

        select_section (str or Section): Only include nodes belonging to the specified section.

        select_frame  (str or Frame): Only include nodes belonging to the specified frame.

        select_heads (None or bool): if specified, return only nodes that are heads of sections (``True``); or nodes that
            are internal to sections (``False``)

    Returns:
        Either a list or a dictionary, see `data`
    """

    # See <https://stackoverflow.com/questions/472000/usage-of-slots>
    __slots__ = ('_individual', '_nx_graph', '_nodes')

    def __getstate__(self):
        return {'_individual': self._individual, '_graph': self._nx_graph, '_nodes': self._nodes}

    def __setstate__(self, state):
        self._individual = state['_individual']
        self._nx_graph = state['_graph']
        self._nodes = state['_nodes']

    def __init__(self, individual: "Individual") -> None:
        self._individual = individual
        self._nx_graph = individual._real_nx_graph
        self._nodes = {n: NodeWrapper(n, d) for n, d in sorted(self._nx_graph.nodes(data=True))}
        for n1, n2, k in self._nx_graph.edges(keys=True):
            assert k == 'next' or k[0] == '$', "All edges should be parameter"
            self._nodes[n1][k] = n2

    # Mapping methods
    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __getitem__(self, key):
        if not isinstance(key, NodeID):
            key = NodeID(key)
        assert key in self._nodes, f"Node {key} not in the individual ({list(self._nodes)})"
        return NodeWrapper(node_id=key, data=self._nx_graph.nodes[key])

    # Set methods
    def __contains__(self, n):
        return n in self._nodes

    # NodeWrapper
    def __call__(self,
                 nodes: Collection[Union[NodeID, int]] = None,
                 data: Union[str, bool] = False,
                 default: Any = None,
                 select_section: Union[Section, str] = None,
                 select_frame: Union[Frame, str] = None,
                 select_heads: Optional[bool] = None) -> Union[List[NodeID], Dict[NodeID, Any]]:
        assert not (select_section and select_frame), "Can't filter both by frame and section"

        # let's filter node list
        selected_node = list(self)

        if select_section:
            if isinstance(select_section, str):
                select_section = self._individual.constraints.sections[select_section]
            selected_node = [
                n for n in selected_node if select_section in (f.section for f in self._nodes[n]['frame_path'])
            ]

        if select_frame:
            if isinstance(select_frame, Frame):
                selected_node = [n for n in selected_node if select_frame in self._nodes[n]['frame_path']]
            else:
                selected_node = [
                    n for n in selected_node if select_frame in (f.name for f in self._nodes[n]['frame_path'])
                ]

        if select_heads is not None:
            internal_nodes = set(t for f, t, k in self._nx_graph.edges(selected_node, keys=True) if k == 'next')
            if select_heads:
                selected_node = [n for n in selected_node if n not in internal_nodes]
            else:
                selected_node = [n for n in selected_node if n in internal_nodes]

        if nodes:
            selected_node = [n for n in selected_node if n in {NodeID(n) for n in nodes}]

        # data is False: return a list of NodeID
        if data is False:
            return selected_node

        # data is either True or str: return a dict NodeID -> Any
        node_dict = dict()
        for n in selected_node:
            if data is True:
                node_dict[n] = self._nodes[n]
            else:
                node_dict[n] = self._nodes[n][data]
        return node_dict
