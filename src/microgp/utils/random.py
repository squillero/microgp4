# -*- coding: utf-8 -*-
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0a1 "Kiwi"   #
#  / / / / / __/ /_/ / // /   A versatile evolutionary optimizer & fuzzer   #
# / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         #
# \__  /\____/_/   /__  __/                                                 #
#   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!"  #
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

from typing import Sequence, List, Any, Optional, Collection
import warnings
import random as py_random
from numpy import random as np_random
from scipy.stats import truncnorm
from . import logging


class MicroGP_Random():
    """Internal random engine to guarantee reproducibility."""

    def __init__(self):
        self._py_random = py_random.Random()
        self._np_random = np_random.get_state()
        self._calls = 0
        self.seed(42)

    def seed(self, *args, **kwargs):
        self._calls = 0
        return self._py_random.seed(*args, **kwargs)

    def randrange(self, a: int, b: int, *args, **kwargs) -> int:
        """Alias for randint(a, b-1)"""
        return self.randint(a, b - 1)

    def randint(self, a: int, b: int, loc: Optional[int] = None, strength: Optional[float] = None) -> int:
        """Return a random integer N such that a <= N <= b. Do consider mean (loc) and strength."""
        self._calls += 1
        assert isinstance(a, int) and isinstance(b, int), f"Range must be int"
        assert a <= b, f"Illegal range [{a}, {b}]"
        assert loc is None or isinstance(loc, int), f"Mean must be int (found: {type(loc)}"
        assert loc is None or strength is not None, f"Strength must be specified if loc is used"
        assert loc is None or a <= loc <= b, f"Illegal loc (loc=f{loc})"
        assert strength is None or strength == 1 or loc is not None, f"loc must be specified if a strength < 1 is used"
        assert strength is None or 0 <= strength <= 1, f"Illegal strength (strength={strength})"

        if strength is None or strength == 1:
            # pure random
            val = self._py_random.randint(a, b)
        elif strength == 0:
            # deterministic
            val = loc
        else:
            # "true" random
            scale = strength / (1 - strength**3)
            scale *= b - a
            sa, sb = (a - .5 - loc) / scale, (b + .5 - loc) / scale

            # restore n' save numpy random state hoping for reproducibility
            np_random.set_state(self._np_random)
            raw_val = truncnorm.rvs(a=sa, b=sb, loc=loc, scale=scale)
            self._np_random = np_random.get_state()

            val = int(round(raw_val))
        assert a <= val <= b, f"Stochastic panic: val={val} not in [{a}, {b}]"
        return val

    def random(self, *args, **kwargs):
        """Proxy for random.random()"""
        self._calls += 1
        return self._py_random.random(*args, **kwargs)

    def shuffle(self, *args, **kwargs):
        """Proxy for random.shuffle()"""
        self._calls += 1
        return self._py_random.shuffle(*args, **kwargs)

    def choice(self,
               seq: Sequence[Any],
               last_index: Optional[int] = None,
               strength: Optional[float] = None,
               return_index: Optional[bool] = False) -> Any:
        """Return a random element or its index from the sequence seq. Do consider last_index and strength."""
        self._calls += 1
        assert seq, f"seq must be a valid sequence (found: {seq})"
        assert last_index is None or isinstance(last_index, int), f"last_index must be int (found: {type(last_index)})"
        assert last_index is None or strength is not None, f"Strength must be specified if last_index is used"
        assert last_index is None or 0 <= last_index < len(seq), f"Illegal last_index (last_index=f{last_index})"
        assert strength is None or strength == 1 or last_index is not None, f"last_index must be specified if a strength < 1 is used"
        assert strength is None or 0 <= strength <= 1, f"Illegal strength (strength={strength})"

        if not last_index or strength == 1:
            new_index = self._py_random.randrange(0, len(seq))
        elif strength == 0:
            new_index = last_index
        else:
            new_index = self.randint(0, len(seq) - 1, loc=last_index, strength=strength)
        if return_index:
            return new_index
        else:
            return seq[new_index]

    def group_choice(self, population: Collection[Any], num: float = 1, **kwargs) -> List[Any]:
        """Proxy for random.choiches()"""
        self._calls += 1
        result = [self.choice(population) for _ in range(int(num))]
        while self.random() < num % 1:
            result.append(self.choice(population))
        return result

    def __str__(self):
        random_state = hex(abs(hash(self._py_random.getstate())))
        return f"{self._calls}:0x{random_state}"


random_generator = MicroGP_Random()
