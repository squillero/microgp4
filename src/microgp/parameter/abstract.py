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

from abc import ABC
from typing import List
from typing import Optional, Any
from ..utils import logging
from ..abstract import Paranoid, Pedantic
from ..node import NodeID


class Parameter(Paranoid, Pedantic, ABC):
    """Abstract Base Class for Macros' parameters (a Paranoid, Pedantic class)

    Base parameters cannot be used directly and provide a blueprint for all
    parameter sub classes. Please note that attributes of the subclasses must
    be bound to specific values to finally get usable parameters.

    """

    def __init__(self, name: str, *args, **kwargs) -> None:
        assert not args, f"Extra arguments in SimpleParameter: {str(args)}"
        assert not kwargs, f"Extra key arguments in SimpleParameter: {str(kwargs)}"
        self._name = name
        self._value = None

    @property
    def name(self) -> str:
        return f"${self._name}"

    @property
    def value(self) -> Any:
        """Get current value of the parameter"""
        assert self.run_paranoia_checks()
        return self._value

    @value.setter
    def value(self, value) -> None:
        """Set the current value of the parameter. With validity check."""
        self._value = value
        assert self.run_paranoia_checks()

    def initialize(self, value: Optional[Any] = None) -> None:
        """Initialize parameter either to s given value or randomly

        Args:
            value (Any): value of the parameter, if None then take a random value (i.e., mutate with strength=1)
        """
        if value is None:
            self.mutate(strength=1)
        else:
            self.value = value

    def mutate(self, strength) -> None:
        """Mutate current value according to strength (ie. strength)."""
        raise NotImplementedError

    def is_valid(self, value) -> bool:
        """Check whether the given value is valid for the parameters"""
        raise NotImplementedError

    def run_paranoia_checks(self) -> bool:
        assert self._value is None or self.is_valid(
            self._value), f"Invalid value '{self._value}' ({type(self._value)}) for parameter {type(self)}"
        return True

    def __str__(self):
        return str(self._value)

    def __format__(self, format_spec):
        return format(self._value, format_spec)


class Structural(Parameter, ABC):
    """Abstract Base Class for Macros' structural parameters

    Structural arameters require references to the Individual and the NodeID they are in.
    This class inherits from Parameter.
    """

    def __init__(self, individual: 'Individual', node: 'NodeID', **kwargs) -> None:
        super().__init__(**kwargs)
        self._individual = individual
        self._node = node

    # read only reference to individual/node
    @property
    def individual(self) -> 'Individual':
        return self._individual

    @property
    def node(self) -> 'NodeID':
        return self._node

    def run_paranoia_checks(self) -> bool:
        assert isinstance(self._node, NodeID), f"Invalid node '{self._node}' ({type(self._value)})"
        return super().run_paranoia_checks()


class Special(Structural, ABC):
    """Base class for special Macros' pseudo-parameters.

    Special parameters do require a reference to the Individual, thus they inherits from Structural.
    """

    def is_valid(self, value) -> bool:
        """Checking a Special parameter for validity is useless."""
        return True

    def mutate(self, strength) -> None:
        """Trying to mutate a Special parameter is quite useless."""
        pass


class Reference(Structural, ABC):
    """Base class for references. Inherits from Structural"""

    def _valid_targets(self) -> List[NodeID]:
        raise NotImplementedError

    def is_valid(self, value: NodeID) -> bool:
        if value is None: return True
        return value not in self._valid_targets()

    @property
    def value(self) -> NodeID:
        """Get the destination NodeID directly from NetworkX"""
        return self.individual.graph_manager.get_parameter(self.node, self.name)

    @value.setter
    def value(self, new_reference: Optional[NodeID]) -> None:
        old_reference = self.individual.graph_manager.get_parameter(self.node, self.name)
        if old_reference:
            self.individual.graph_manager.remove_edge(self.node, old_reference)
        if new_reference is not None:
            self.individual.graph_manager.add_edge(self.node, new_reference, self.name)

    def mutate(self, strength: float = 0.5) -> None:
        assert 0 <= strength <= 1, "Invalid strength: " + str(strength) + " (should be 0 <= s <= 1)"
        if strength == 0:
            logging.debug("strength == 0")
        elif not self._valid_targets():
            logging.debug(f"No valid targets for {self.name}")
            self.value = None
        else:
            old_target = self.value
            valid_targets = self._valid_targets()
            if old_target in valid_targets:
                old_index = valid_targets.index(old_target)
            else:
                old_index = None
            self.value = random_generator.choice(valid_targets, last_index=old_index, strength=strength)
