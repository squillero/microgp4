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

from typing import List, Union

from .base import Structural
from ..individual_operators import unroll_macro_list, Individual
from ..utils import logging
from ..node import NodeID
from microgp import random_generator
import microgp as ugp


class Reference(Structural):
    """Base class for references. Inherits from Structural"""

    def _valid_targets(self) -> List[NodeID]:
        raise NotImplementedError

    def is_valid(self, value):
        return value is not None and value in self._valid_targets()

    @property
    def value(self) -> NodeID:
        """Get the destination NodeID"""
        return next((t for f, t, k in self.individual.graph.edges(self.node, keys=True) if k == self.name), None)


class LocalReference(Reference):
    """A reference to a Node connected through (undirected) "next" edges

    **Examples:**

    >>> ref_fwd = ugp.make_parameter(ugp.parameter.LocalReference,
    >>>                              allow_self=False,
    >>>                              allow_forward=True,
    >>>                              allow_backward=False,
    >>>                              frames_up=1)
    >>> ref_bcw = ugp.make_parameter(ugp.parameter.LocalReference,
    >>>                              allow_self=False,
    >>>                              allow_forward=False,
    >>>                              allow_backward=True,
    >>>                              frames_up=1)

    Args:
        allow_self (bool): The referenced node may be the node itself;
        allow_forward (bool): The referenced node may be a successors;
        allow_backward (bool): The referenced node may be a predecessors;
        frames_up (int): How many frame up the reference must be within (optional, default: 0, i.e., only the current frame)
    """

    def __init__(self, individual: Individual, offset: int = None, *args, **kwargs):
        super().__init__(individual=individual, *args, **kwargs)
        if hasattr(self, 'frames_up'):
            self.frames_up = self.frames_up + 1
        else:
            self.frames_up = 1
        assert isinstance(getattr(self, 'allow_self', None),
                          bool), "Illegal or missing allow_self (not using make_parameter?)"
        assert isinstance(getattr(self, 'allow_forward', None),
                          bool), "Illegal or allow_forward min (not using make_parameter?)"
        assert isinstance(getattr(self, 'allow_backward', None),
                          bool), "Illegal or missing allow_backward (not using make_parameter?)"
        if offset:
            self._offset = offset
            self._value = None
        else:
            self._offset = None
            self.mutate(1)

    def _valid_targets(self) -> List[NodeID]:
        assert len(self.individual.graph.node_view[self.node]['frame_path']) >= -self.frames_up, \
            f"Can't go up the requested number of frames"
        frame_path = self.individual.graph.node_view[self.node]['frame_path'][0:self.frames_up]
        vtargets = list()
        if self.allow_backward:
            vtargets += [
                n for n in self.individual.get_predecessors(self.node)
                if self.individual.graph.node_view[n]['frame_path'][0:len(frame_path)] == frame_path
            ]
        if self.allow_self:
            vtargets += [self.node]
        if self.allow_forward:
            vtargets += [
                n for n in self.individual.get_successors(self.node)
                if self.individual.graph.node_view[n]['frame_path'][0:len(frame_path)] == frame_path
            ]
        # logging.debug("Valid targets for %s: %s" % (frame_path, vtargets))
        return vtargets

    def mutate(self, sigma: float = 0.5) -> None:
        assert 0 <= sigma <= 1, "Invalid strength: " + str(sigma) + " (should be 0 <= s <= 1)"
        old_target = next((t for f, t, k in self.individual.graph.edges(self.node, keys=True) if k == self.name), None)
        # print(self._valid_targets())
        if not self._valid_targets():
            logging.debug(f"No valid targets for {self.name}")
            # Parameter can't be mutated because there aren't valid targets
        # assert self._valid_targets(), f"No valid targets for {self.name}"
        if sigma == 0:
            logging.debug("sigma == 0")
        # Mutate with probability sigma
        else:
            # Choose the new target
            new_target = self.choose_local_target_node(old_target, sigma)

            if old_target:
                self.individual.graph.remove_edge(self.node, old_target, self.name)
            self.individual.graph.add_edge(self.node, new_target, self.name)
        # Everything ok

    def value_to_offset(self) -> int:
        """Return the distance of the destination node from the actual one"""
        """ Examples:
            | self.node = n231
            | n218 -> n219 -> n224 -> n227 -> n231 -> n232 -> n240 -> n241
            |                                  _______________^ = +2
            | self.node = n232
            | n218 -> n219 -> n224 -> n227 -> n231 -> n232 -> n240 -> n241
            |          ^______________________________  = -4
       """
        succs = [self.node] + self._individual.get_successors(self.node)
        if self.value in succs:
            n_of_jumps = succs.index(self.value)
        else:
            precs = [self.node] + self._individual.get_predecessors(self.node)
            if self.value in precs:
                n_of_jumps = -precs.index(self.value)
            else:
                exit("This should not happen")
        return n_of_jumps

    def offset_to_value(self, offset: int) -> Union[NodeID, None]:
        """Return the correspondent destination NodeID starting from the offset. Or None"""
        """
           self.node = n231 and offset = -2
            ( n218 -> n219 -> n224 -> n227 -> n231 -> n232 -> n240 -> n241)
           Returns: n224
           
           self.node = n224 and offset = -6
           ( n218 -> n219 -> n224 -> n227 -> n231 -> n232 -> n240 -> n241 )
           Returns: None
       """
        if not self._valid_targets():
            return None
        if offset == 0:
            return self.node
        elif offset > 0:
            succs = [self.node] + self._individual.get_successors(self.node)
            if offset >= len(succs):
                if succs[-1] in self._valid_targets():
                    return succs[-1]
                else:
                    return None
            else:
                # print(offset, " ", succs, " ", self._valid_targets())
                if succs[offset] in self._valid_targets():
                    return succs[offset]
                else:
                    return None
        else:
            precs = [self.node] + self._individual.get_predecessors(self.node)
            if -offset >= len(precs):
                if precs[-1] in self._valid_targets():
                    return precs[-1]
                else:
                    return None
            else:
                if precs[-offset] in self._valid_targets():
                    return precs[-offset]
                else:
                    return None

    @property
    def value(self) -> NodeID:
        """Get the destination NodeID"""
        return next((t for f, t, k in self.individual.graph.edges(self.node, keys=True) if k == self.name), None)

    @value.setter
    def value(self, new_value: NodeID):
        assert isinstance(new_value, NodeID), "new_value must be a NodeID"
        assert new_value in self._valid_targets(), "new_value must be in valid targets"

        old_target = next((t for f, t, k in self.individual.graph.edges(self.node, keys=True) if k == self.name), None)
        if old_target:
            self.individual.graph.remove_edge(self.node, old_target, self.name)
        self.individual.graph.add_edge(self.node, new_value, self.name)
        self._offset = None
        self._value = new_value

    def choose_local_target_node(self, old_target: NodeID, sigma: float) -> NodeID:
        """Choose a new valid target for the LocalReference parameter

        Args:
            old_target (NodeID): old target NodeID
            sigma (float): likelihood of mutation

        Returns:
            A new target NodeID
        """
        if sigma == 1:
            new_target = random_generator.choice(self._valid_targets())
        else:
            valid_targets = self._valid_targets()
            new_target = random_generator.choice(seq=valid_targets,
                                                 last_index=valid_targets.index(old_target),
                                                 strength=sigma)
        return new_target

    @property
    def offset(self) -> int:
        return self._offset

    @offset.setter
    def offset(self, new_offset: int):
        assert isinstance(
            new_offset,
            int) or not new_offset, f"Passed offset must be and int or None object. Got {type(new_offset)} instead"
        old_target = next((t for f, t, k in self.individual.graph.edges(self.node, keys=True) if k == self.name), None)
        if old_target:
            self.individual.graph.remove_edge(self.node, old_target, self.name)
        self._value = None
        self._offset = new_offset


class ExternalReference(Reference):
    """A reference to a NodeID non connected through (undirected) "next" edges.

    **Examples:**

    >>> proc1 = ugp.make_parameter(ugp.parameter.ExternalReference, section_name='proc1', min=5, max=5)

    Args:
        section_name (str): name of the new target section.
    """

    def __init__(self, individual: 'Individual', *args, **kwargs):
        do_not_init = kwargs.get('do_not_init', None)
        if do_not_init:
            del kwargs['do_not_init']
        super().__init__(individual=individual, *args, **kwargs)
        assert isinstance(getattr(self, 'section_name', None),
                          str), "Illegal or missing section_name (not using make_parameter?)"
        self._final_destination = None
        if self.individual.nodes[self.node]["frame_path"] is None or do_not_init:
            return
        else:
            # Avoid the mutation in case of this parameter is contained in a movable node. A movable node has not a
            #   frame path, therefore the valid target method that is used in mutate can't run correctly
            self.mutate(1)
        # assert isinstance(kwargs['section_name'], str), "Illegal or missing section_name (not using make_parameter?)"

    def is_valid(self, value):
        n = self.name
        return value is not None and value in self._valid_targets()

    def _valid_targets(self) -> List[NodeID]:
        assert self.section_name in self.individual.constraints.sections, "No section named '%s' in constraints. Valid: %s." % (
            self.section_name, self.individual.constraints.sections)
        nodes = set(self.individual.nodes(section=self.section_name))
        not_heads = set(t for f, t, k in self.individual.graph.edges(keys=True) if k == 'next')
        return list(nodes - not_heads)

    def mutate(self, sigma: float = 0.5) -> None:
        assert 0 <= sigma <= 1, "Invalid strength: " + str(sigma) + " (should be 0 <= s <= 1)"
        if sigma == 0:
            logging.debug("sigma == 0")
        else:
            old_target = next((t for f, t, k in self.individual.graph.edges(self.node, keys=True) if k == self.name),
                              None)
            potential_targets = self._valid_targets() + [None]

            # Choose the new target
            new_target = random_generator.choice(potential_targets)

            # Create a new procedure
            if new_target is None:
                # Let's create a new section
                nodes = unroll_macro_list(self.individual, self.section_name)
                macro, frame_path = nodes.pop(0)
                new_target = self.individual.add_node(parent_node=None, macro=macro, frame_path=frame_path)
                parent = new_target
                uninitialized_nodes = {parent}
                for macro, frame_path in nodes:
                    parent = self.individual.add_node(parent_node=parent, macro=macro, frame_path=frame_path)
                    uninitialized_nodes.add(parent)
                self.individual.randomize_macros(uninitialized_nodes)

            if old_target:
                self.individual.graph.remove_edge(self.node, old_target, self.name)
            self.individual.graph.add_edge(self.node, new_target, self.name, color='green')

            self._value = new_target

    @property
    def value(self) -> NodeID:
        """Get the destination NodeID"""
        return next((t for f, t, k in self.individual.graph.edges(self.node, keys=True) if k == self.name), None)

    @value.setter
    def value(self, new_value: NodeID) -> None:
        assert isinstance(new_value, NodeID), "new_value must be a NodeID"
        old_target = next((t for f, t, k in self.individual.graph.edges(self.node, keys=True) if k == self.name), None)
        if old_target:
            self.individual.graph.remove_edge(self.node, old_target, self.name)
        self.individual.graph.add_edge(self.node, new_value, self.name, color='green')

        self._value = new_value

    @property
    def final_destination(self) -> Union[NodeID, None]:
        return self._final_destination

    @final_destination.setter
    def final_destination(self, destination: Union[NodeID, None]):
        assert isinstance(destination, NodeID) or not destination, "destination not a NodeID or None"
        self._final_destination = destination
        old_target = next((t for f, t, k in self.individual.graph.edges(self.node, keys=True) if k == self.name), None)
        if old_target:
            self.individual.graph.remove_edge(self.node, old_target, self.name)
        self._value = None
