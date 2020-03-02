# -*- coding: utf-8 -*-
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0a1 "Kiwi"   #
#  / / / / / __/ /_/ / // /   (!) by Giovanni Squillero and Alberto Tonda   #
# / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         #
# \__  /\____/_/   /__  __/                                                 #
#   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!!" #
#                                                                           #
#############################################################################

# Copyright 2019 Giovanni Squillero and Alberto Tonda
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

from collections import deque
from typing import Sequence

from .common_data_structures import Frame
from .utils import logging


class _SimpleNode:
    """Oversimplified tree node"""

    def __init__(self, frame: Frame) -> None:
        self.frame = frame
        self.distance_from_root = None
        self.children = list()

    def add_child(self, child: "_SimpleNode") -> None:
        assert child not in self.children, "NodeID already listed as child"
        child.distance_from_root = self.distance_from_root + 1
        self.children.append(child)

    def debug_print(self, level: int) -> None:
        logging.bare("%s. %s" % ('.' * level * 2, self.frame))
        for c in self.children:
            c.debug_print(level + 1)

    def post_order_visit(self) -> Sequence[Frame]:
        for n in self.children:
            yield from n.post_order_visit()
        yield self.frame

    def pre_order_visit(self) -> Sequence[Frame]:
        yield self.frame
        for n in self.children:
            yield from n.pre_order_visit()


class SimpleTree:
    """Oversimplified tree for managing frame structure"""

    def __init__(self, root: Frame) -> None:
        self.node_dict = dict()
        self.root = _SimpleNode(root)
        self.root.distance_from_root = 0
        self.store(self.root)

    def store(self, node: _SimpleNode):
        """Updates the node dictionary & performs few sanity checks"""
        assert node.frame not in self.node_dict, f"Frame '{node.frame}' already in the node dictionary"
        assert node not in self.node_dict.values(), f"NodeID '{node}' already in the node dictionary"
        self.node_dict[node.frame] = node

    def get_sub_frames(self, frame: Frame) -> Sequence[Frame]:
        """Retrieves frames embedded in a given frame"""
        assert frame in self.node_dict, f"Can't find '{frame}' in node dictionary '{self.node_dict}'"
        return [n.frame for n in self.node_dict[frame].children]

    def get_distance_from_root(self, frame: Frame):
        """Returns the distance from root frame"""
        assert frame in self.node_dict, f"Can't find '{frame}' in node dictionary '{self.node_dict}'"
        return self.node_dict[frame].distance_from_root

    def add_path(self, path: Sequence[Frame]) -> None:
        """Adds all nodes in a frame path to the tree"""
        path = deque(path)
        assert not path[0].name, "Root node not a RootFrame"
        next_node = self.root
        while next_node and path:
            parent_node = next_node
            path.popleft()
            next_node = next((n for n in parent_node.children if n.frame == path[0]), None)
        while path:
            child = _SimpleNode(path.popleft())
            self.store(child)
            parent_node.add_child(child)
            parent_node = child

    def debug_print(self):
        """Displays tree"""
        self.root.debug_print(0)

    def post_order_visit(self) -> Sequence[Frame]:
        """Returns all frames in post-order"""
        yield from self.root.post_order_visit()

    def pre_order_visit(self) -> Sequence[Frame]:
        """Returns all frames in pre-order"""
        yield from self.root.pre_order_visit()
