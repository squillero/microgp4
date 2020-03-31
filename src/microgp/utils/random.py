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

# MicroGP's own random generator.

from typing import List, Any
import random as py_random
from numpy import random as np_random
from scipy.stats import truncnorm
from . import logging


class MicroGP_Random():

    def __init__(self):
        self._py_random = py_random.Random()
        self._np_random = np_random.get_state()
        self._calls = 0
        self.seed(42)

    def seed(self, *args, **kwargs):
        self._calls = 0
        return self._py_random.seed(*args, **kwargs)

    def randint(self, start: int, stop: int, strength=False) -> int:
        self._calls += 1
        assert isinstance(start, int) and isinstance(stop, int), "Range must be int"
        assert strength is None or 0 <= strength <= 1, "Illegal strength"

        if strength is None or strength == 1:
            # pure random
            val = self._py_random.randint(start, stop)
        elif strength == 0:
            # deterministic
            val = 0
        else:
            # "true" random
            min_ = start - .5
            max_ = stop + .5
            scale = strength/(1-strength**3)
            scale *= start - stop
            a, b = min_/scale, max_/scale
            # restore n' save numpy random state hoping for reproducibility
            np_random.set_state(self._np_random())
            val = round(truncnorm.rvs(a=a, b=b, loc=0, scale=scale))
            self._np_random = np_random.get_state()
            assert start <= val <= stop, f"Uh!? val={val}"
        return val

    def random(self, *args, **kwargs):
        self._calls += 1
        return self._py_random.random(*args, **kwargs)

    def shuffle(self, *args, **kwargs):
        self._calls += 1
        return self._py_random.shuffle(*args, **kwargs)

    def choice(self, *args, sigma=None, previous_index=None, **kwargs) -> Any:
        assert (sigma is None and previous_index is None) or (
            sigma is not None and previous_index is not None), "both sigma and previous_index should be specified"
        self._calls += 1
        return self._py_random.choice(*args, **kwargs)

    def choices(self, *args, **kwargs) -> List[Any]:
        self._calls += 1
        return self._py_random.choices(*args, **kwargs)

    def __str__(self):
        random_state = hex(abs(hash(self._py_random.getstate())))
        return f"{self._calls}:0x{random_state}"


random_generator = MicroGP_Random()
