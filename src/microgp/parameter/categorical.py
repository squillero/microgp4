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

from microgp import *
from ..utils import logging
from .abstract import Parameter
from microgp import random_generator
import microgp as ugp4


class Categorical(Parameter):
    """Categorical parameter. It can take values in 'alternatives'.

    **Example:**

    >>> registers = ugp4.make_parameter(ugp4.parameter.Categorical, alternatives=['ax', 'bx', 'cx', 'dx'])


    Args:
        alternatives (list): list of possible values
    """

    def is_valid(self, value):
        if value is None: return True
        return value in self.alternatives

    def mutate(self, strength: float = 0.5):
        assert 0 <= strength <= 1, "Invalid strength: " + str(strength) + " (should be 0 <= s <= 1)"
        if strength == 0:
            logging.debug("strength == 0")
        else:
            self.value = random_generator.choice(self.alternatives)

    def run_paranoia_checks(self) -> bool:
        assert getattr(self, 'alternatives', None), "Illegal or missing alternatives list (not using make_parameter?)"
        return super().run_paranoia_checks()


class CategoricalSorted(Categorical):
    """CategoricalSorted parameter. It can take values in 'alternatives'. It
    behaves differently during the mutation phase.

    **Example:**

    >>> cat_sor = ugp4.make_parameter(ugp4.parameter.CategoricalSorted, alternatives=['e', 'f', 'g', 'h', 'i', 'l'])

    Args:
        alternatives (list): sorted list of possible values
    """

    def mutate(self, strength: float = 0.5):
        assert getattr(self, 'alternatives', None), "Illegal or missing alternatives list (not using make_parameter?)"
        assert 0 <= strength <= 1, "Invalid strength: " + str(strength) + " (should be 0 <= s <= 1)"
        if strength == 0:
            logging.debug("strength == 0")
        else:
            self.value = random_generator.choice(self.alternatives,
                                                 self.alternatives.index(self._value),
                                                 strength=strength)

    def run_paranoia_checks(self) -> bool:
        assert getattr(self, 'alternatives', None), "Illegal or missing alternatives list (not using make_parameter?)"
        assert len(self.alternatives) == len(set(
            self.alternatives)), f"Found duplicated values in alternatives: {self.alternatives}"
        return super().run_paranoia_checks()
