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

from ..abstract import Paranoid, Pedantic


class Parameter(Paranoid, Pedantic):
    """Base class for Macros' parameters (a Paranoid, Pedantic class)

    Base parameters cannot be used directly and provide a blueprint for all
    parameter sub classes. Please note that attributes of the subclasses must
    be bound to specific values to finally get usable parameters.

    """

    def __init__(self, name: str, *args, **kwargs) -> None:
        assert not args, "Extra arguments in SimpleParameter: %s" % (str(args),)
        assert not kwargs, "Extra key arguments in SimpleParameter: %s" % (str(kwargs),)
        self._name = name
        self._value = None

    @property
    def name(self) -> str:
        return f"${self._name}"

    @property
    def value(self) -> 'NodeID':
        """Get current value of the parameter"""
        return self._value

    @property
    def individual(self) -> 'Individual':
        """Get current individual of the parameter"""
        return self._individual

    @value.setter
    def value(self, value) -> None:
        """Set the current value of the parameter. With validity check."""
        self._value = value
        class_, type_ = str(self.__class__.__name__), str(type(value))
        assert self.is_valid(value), "Incorrect Value for an " + class_ + ": (" + type_ + ")" + str(value)

    def run_paranoia_checks(self) -> None:
        assert self.is_valid(self.value), "Invalid value '%s' for parameter '%s'" % (self.value, self)

    def is_valid(self, value) -> bool:
        """Check whether the given value is valid for the parameters"""
        raise NotImplementedError

    def mutate(self, sigma) -> None:
        """Mutate current value according to sigma (ie. strength)."""
        raise NotImplementedError

    def __str__(self):
        class_, type_ = str(self.__class__.__name__), str(type(self.value))
        assert self.is_valid(self.value), "Incorrect Value for an " + class_ + ": (" + type_ + ")" + str(self.value)
        return self.value

    def __format__(self, format_spec):
        return format(self.value, format_spec)


class Structural(Parameter):
    """Base class for Macros' structural parameters, ie. parameters requiring
    references to their name, the Individual and the NodeID they are in. This
    class inherits from Parameter.
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


class Special(Structural):
    """Base class for special Macros' pseudo-parameters. Special parameters do
    require a reference to the Individual, thus they inherits from Structural.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def value(self):
        """The value of a special parameters is itself. Behavior might be
        customized using the __format__ function.
        """
        return self

    def run_paranoia_checks(self) -> bool:
        """Worrying about a Special parameter is useless."""
        return True

    def is_valid(self, value) -> bool:
        """Checking a Special parameter for validity is useless."""
        return True

    def mutate(self, sigma) -> None:
        """Trying to mutate a Special parameter is an error."""
        assert False, f"Trying to mutate Special parameter {self}"
