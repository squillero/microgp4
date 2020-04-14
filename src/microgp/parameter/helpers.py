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

import warnings
from typing import Type, Any
from .abstract import Parameter
from ..node import NodeID
from ..individual import Individual


def make_parameter(base_class: Type[Parameter], **attributes: Any) -> Type:
    """Binds a Base parameter class, fixing some of its internal attributes.

    Args:
        base_class (Parameter): Base class for binding parameter.
        **attributes (dict): Attributes.

    Returns:
        Bound parameter.

    **Examples:**

        >>> register = ugp4.make_parameter(ugp4.parameter.Categorical, alternatives=['ax', 'bx', 'cx', 'dx'])
        >>> int8 = ugp4.make_parameter(ugp4.parameter.Integer, min_=-128, max_=128)
        >>> p1, p2 = register(), int8()
    """
    signature = ", ".join([str(k) + "=" + str(v) for k, v in attributes.items()])
    return type("{}({})".format(base_class.__name__, signature), (base_class,), attributes)


class FloatingLocalReference:
    """A LocalReference that be almost safely moved between individuals"""

    def __init__(self):
        self._reference_node = None
        self._original_target_node = None
        self._offset = None

    def set(self, target_node: NodeID, reference_node: NodeID, individual: Individual) -> None:
        self._reference_node = individual.nodes[reference_node]
        self._original_target_node = individual.nodes[target_node]
        local_nodes = individual.graph_manager.get_all_predecessors(reference_node) + [
            reference_node
        ] + individual.graph_manager.get_all_successors(reference_node)
        self._offset = local_nodes.index(target_node) - local_nodes.index(reference_node)

    def get(self, reference_node: NodeID, individual: Individual) -> NodeID:
        local_nodes = individual.graph_manager.get_all_predecessors(reference_node) + [
            reference_node
        ] + individual.graph_manager.get_all_successors(reference_node)
        index = local_nodes.index(reference_node) + self._offset
        index = min(index, len(local_nodes) - 1)
        index = max(index, 0)
        return local_nodes[index]
