# -*- coding: utf-8 -*-
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0a1 "Kiwi"   #
#  / / / / / __/ /_/ / // /   A versatile evolutionary optimizer & fuzzer   #
# / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         #
# \__  /\____/_/   /__  __/                                                 #
#   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!"  #
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

from typing import Any, List, Optional

import microgp as ugp4
from .abstract import Reference
from ..node import NodeID


class LocalReference(Reference):
    """A reference to a Node connected through (undirected) "next" edges

    **Examples:**

    >>> ref_fwd = ugp4.make_parameter(ugp4.parameter.LocalReference,
    >>>                              allow_self=False,
    >>>                              allow_forward=True,
    >>>                              allow_backward=False,
    >>>                              frames_up=1)
    >>> ref_bcw = ugp4.make_parameter(ugp4.parameter.LocalReference,
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

    def _get_valid_targets(self) -> List[NodeID]:
        try:
            frames_up = self.frames_up + 1
        except AttributeError:
            frames_up = 1
        assert len(
            self.individual.nodes[self.node].frame_path) >= -frames_up, f"Can't go up the requested number of frames"

        frame_path = self.individual.nodes[self.node].frame_path[0:frames_up]
        vtargets = list()
        if self.allow_backward:
            vtargets += [
                n for n in self.individual.nodes[self.node].predecessors
                if self.individual.nodes[n].frame_path[0:len(frame_path)] == frame_path
            ]
        if self.allow_self:
            vtargets += [self.node]
        if self.allow_forward:
            vtargets += [
                n for n in self.individual.nodes[self.node].successors
                if self.individual.nodes[n].frame_path[0:len(frame_path)] == frame_path
            ]
        # logging.debug("Valid targets for %s: %s" % (frame_path, vtargets))
        return vtargets

    def run_paranoia_checks(self) -> bool:
        assert isinstance(getattr(self, 'allow_self', None),
                          bool), "Illegal or missing allow_self (not using make_parameter?)"
        assert isinstance(getattr(self, 'allow_forward', None),
                          bool), "Illegal or allow_forward min (not using make_parameter?)"
        assert isinstance(getattr(self, 'allow_backward', None),
                          bool), "Illegal or missing allow_backward (not using make_parameter?)"
        return super().run_paranoia_checks()


class ExternalReference(Reference):
    """A reference to a NodeID non connected through (undirected) "next" edges.


    >>> proc1 = ugp4.make_parameter(ugp4.parameter.ExternalReference, section_name='proc1', min=5, max=5)

    Args:
        section_name (str): name of the new target section.
    """

    def _get_valid_targets(self) -> List[NodeID]:
        return self.individual.nodes(section_selector=self.section_name, heads_selector=True)

    def initialize(self, value: Optional[Any] = None) -> None:
        # TODO! CREATE SECTIONS!!!!!
        pass

    def run_paranoia_checks(self) -> bool:
        assert isinstance(getattr(self, 'section_name', None), str), \
            "Illegal or missing section_name (not using make_parameter?)"
        return super().run_paranoia_checks()
