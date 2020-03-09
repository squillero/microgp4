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

from microgp import *
from ..utils import logging
from .base import Parameter
from .helpers import sigma_choice
from microgp import rnd
import microgp as ugp


class Categorical(Parameter):
    """Categorical parameter. It can take values in 'alternatives'.

    **Example:**

    >>> registers = ugp.make_parameter(ugp.parameter.Categorical, alternatives=['ax', 'bx', 'cx', 'dx'])


    Args:
        alternatives (list): list of possible values
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert getattr(self, 'alternatives', None), "Illegal or missing alternatives list (not using make_parameter?)"
        self.mutate(1)

    def is_valid(self, value):
        return value in self.alternatives

    def mutate(self, sigma: float = 0.5):
        assert 0 <= sigma <= 1, "Invalid strength: " + str(sigma) + " (should be 0 <= s <= 1)"
        if sigma == 0:
            logging.debug("sigma == 0")
            return False
        elif sigma == 1:
            new_value = rnd.choice(self.alternatives)
            self._value = new_value
        else:
            new_value = rnd.choice(self.alternatives)
            self._value = new_value
            while rnd.random() < sigma:
                new_value = rnd.choice(self.alternatives)
                self._value = new_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        assert new_value in self.alternatives, "The given value is not in self.alternatives"
        self._value = new_value


class CategoricalSorted(Parameter):
    """CategoricalSorted parameter. It can take values in 'alternatives'. It
    behaves differently during the mutation phase.

    **Example:**

    >>> cat_sor = ugp.make_parameter(ugp.parameter.CategoricalSorted, alternatives=['e', 'f', 'g', 'h', 'i', 'l'])

    Args:
        alternatives (list): sorted list of possible values
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert getattr(self, 'alternatives', None), "Illegal or missing alternatives list (not using make_parameter?)"
        self.mutate(1)

    def is_valid(self, value):
        return value in self.alternatives

    def mutate(self, sigma=1):
        assert 0 <= sigma <= 1, "Invalid strength: " + str(sigma) + " (should be 0 <= s <= 1)"
        if sigma == 0:
            logging.debug("sigma == 0")
        # Mutate with strength: sigma
        elif sigma == 1:
            self._value = rnd.choice(self.alternatives)
        else:
            actual_index = self.alternatives.index(self._value)
            new_value = sigma_choice(seq=self.alternatives, previous_index=actual_index, sigma=sigma)
            self._value = new_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        assert new_value in self.alternatives, "The given value is not in self.alternatives"
        self._value = new_value
