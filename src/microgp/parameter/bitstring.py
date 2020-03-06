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

from ..utils import logging
from .base import Parameter
from microgp import rnd
import microgp as ugp


class Bitstring(Parameter):
    """Fixed-length bitstring parameter.

    **Example:**

    >>> word8 = ugp.make_parameter(ugp.parameter.Bitstring, len_=8)

    Args:
        len\_ (int > 0): length of the bit string
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert getattr(self, 'len_', None), "Illegal or missing length (not using make_parameter?)"
        assert self.len_ > 0, "Length must be positive"
        self.mutate(1)

    def is_valid(self, value):
        if not isinstance(value, str):
            return False
        if len(value) != self.len_:
            return False
        return all((b == '0' or b == '1') for b in value)

    def mutate(self, sigma: float = 0.5):
        assert 0 <= sigma <= 1, "Invalid strength: " + str(sigma) + " (should be 0 <= s <= 1)"
        if sigma == 0:
            logging.debug("sigma == 0")
        elif sigma == 1:
            bits_list = rnd.choices([0, 1], k=self.len_)
            self._value = ''.join(map(str, bits_list))
        else:
            i = rnd.randint(0, self.len_-1)
            value = list(self._value.strip())
            value[i] = str(1 - int(value[i]))
            self.value = ''.join(map(str, value))
            while rnd.random() < sigma:
                i = rnd.randint(0, self.len_ - 1)
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

