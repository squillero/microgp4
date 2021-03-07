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

from .fitnesstuplemultiobj import FitnessTupleMultiobj
from microgp import random_generator


class Lexicase(FitnessTupleMultiobj):
    """A fitness for using Lexicase Selection.

    *Lexicase Selection* is a technique supposedly able to handle
    multi-objective problems where solutions must perform optimally on each
    of many test cases.

    See 'Solving Uncompromising Problems With Lexicase Selection', by
    T. Helmuth, L. Spector, and J. Matheson
    <https://dx.doi.org/10.1109/TEVC.2014.2362729>

    Note: as an alternative, consider using *Chromatic Selection*.
    """

    def __gt__(self, other: "Lexicase") -> bool:
        order = list(range(len(self)))
        random_generator.shuffle(order)
        return tuple(self[i] for i in order) > tuple(other[i] for i in order)
