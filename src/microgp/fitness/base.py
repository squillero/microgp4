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
from typing import Type, Dict, Any, List, Tuple


class Base:
    """Base class for storing fitness.

    The different selection schemes are implemented simply by overriding the >
    (greater than) operator. See the other fitness.Classes for details.

    Please note that, according to Spencer's 'Survival of the Fittest',
    the bigger the better. Thus we are *maximizing* the fitness and not
    minimizing a mathematical function.
    """

    def __bool__(self) -> bool:
        """True if valid"""
        raise NotImplementedError

    def __gt__(self, other: "Base") -> bool:
        """True if more fit (ie. preferable to)"""
        raise NotImplementedError

    def __eq__(self, other: "Base") -> bool:
        """True if equally fit"""
        raise NotImplementedError

    def __ne__(self, other: "Base") -> bool:
        """True if not equally fit. There is no need to override this function."""
        raise NotImplementedError

    def __ge__(self, other: "Base") -> bool:
        """True if more or equally fit. There is no need to override this function."""
        raise NotImplementedError

    def __lt__(self, other: "Base") -> bool:
        """True if less fit. There is no need to override this function."""
        raise NotImplementedError

    def __le__(self, other: "Base") -> bool:
        """True if less or equally fit. There is no need to override this function."""
        raise NotImplementedError

    def _is_dominated(self, other: Type["Base"]) -> bool:
        raise NotImplementedError

    @staticmethod
    def sort(fmap: List[Tuple[Any, Type["Base"]]]) -> List[Tuple[Any, Type["Base"]]]:
        raise NotImplementedError


def is_dominated(x: Type["Base"], y: Type["Base"]) -> bool:
    return x._is_dominated(y)
