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

from ..utils import logging
from .abstract import Parameter
from microgp import random_generator
import microgp as ugp4


class Bitstring(Parameter):
    """Fixed-length bitstring parameter.

    **Example:**

    >>> word8 = ugp4.make_parameter(ugp4.parameter.Bitstring, len_=8)

    Args:
        len\_ (int > 0): length of the bit string
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert getattr(self, 'len_', None), "Illegal or missing length (not using make_parameter?)"
        assert self.len_ > 0, "Length must be positive"

    def is_valid(self, value):
        if not isinstance(value, str):
            return False
        if len(value) != self.len_:
            return False
        return all((b == '0' or b == '1') for b in value)

    def mutate(self, strength: float = 0.5):
        assert 0 <= strength <= 1, "Invalid strength: " + str(strength) + " (should be 0 <= s <= 1)"
        if strength == 0:
            logging.debug("strength == 0")
        elif strength == 1:
            bits_list = random_generator.choices([0, 1], k=self.len_)
            self.value = ''.join(map(str, bits_list))
        else:
            i = random_generator.randint(0, self.len_ - 1)
            value = list(self._value.strip())
            value[i] = str(1 - int(value[i]))
            self.value = ''.join(map(str, value))
            while random_generator.random() < strength:
                i = random_generator.randint(0, self.len_ - 1)
                value[i] = str(1 - int(value[i]))
                self.value = ''.join(map(str, value))

    @property
    def value(self) -> str:
        """Get current value of the parameter (type str)"""
        return "".join([str(v) for v in self._value])

    @value.setter
    def value(self, new_value: str):
        """Set a new value for the parameter (type str)"""
        self._value = new_value
