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
from .base import Parameter
from microgp import random_generator
import microgp as ugp4


class Integer(Parameter):
    """Integer parameter in a given range.

    **Example**:

    >>> int256 = ugp4.make_parameter(ugp4.parameter.Integer, min=0, max=256)

    Args:
        min (int): minimum value **included**.
        max (int): maximum value **not included**.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert getattr(self, 'min', None) is not None, "Illegal or missing min (not using make_parameter?)"
        assert getattr(self, 'max', None) is not None, "Illegal or missing max (not using make_parameter?)"
        assert self.min < self.max, "Illegal min/max values"
        self.mutate(1)

    def is_valid(self, value):
        """Check if the passed value is in range min, max.

        Args:
            value: value to be checked.

        Returns:
            True if it is valid. False otherwise.
        """
        if not isinstance(value, int):
            return False
        if value < self.min or value >= self.max:
            return False
        return True

    def mutate(self, sigma: float = 0.5):
        assert 0 <= sigma <= 1, "Invalid strength: " + str(sigma) + " (should be 0 <= s <= 1)"
        if sigma == 0:
            logging.debug("sigma == 0")
        elif sigma == 1:
            self._value = random_generator.randrange(self.min, self.max)
        else:
            self._value = random_generator.randrange(self.min, self.max, loc=self._value, strength=sigma)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        assert self.min <= new_value < self.max, "The given value is not in self.min <= new_value < self.max"
        self._value = new_value
