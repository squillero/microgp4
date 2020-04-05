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
#o
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Type, Any, List, Tuple
import operator

from .base import Base


class FitnessTuple(tuple, Base):
    """Fitness used for single objective purposes."""

    def __bool__(self) -> bool:
        return all(v is not None for v in tuple(self))

    def __gt__(self, other: "FitnessTuple") -> bool:
        raise NotImplementedError

    def __eq__(self, other: "FitnessTuple") -> bool:
        return tuple(self) == tuple(other)

    def __ne__(self, other: "FitnessTuple") -> bool:
        return tuple(self) != tuple(other)

    def __ge__(self, other: "FitnessTuple") -> bool:
        return tuple(self) > tuple(other) or tuple(self) == tuple(other)

    def __lt__(self, other: "FitnessTuple") -> bool:
        return not tuple(self) >= tuple(other)

    def __le__(self, other: "FitnessTuple") -> bool:
        return not tuple(self) > tuple(other)

    def __str__(self) -> str:
        if len(self) > 1:
            return "%s%s" % (self.__class__.__name__, str(tuple(self)))
        else:
            return "%s(%s)" % (self.__class__.__name__, str(self[0]))

    def __repr__(self):
        return "<{} at {} {}>".format(type(self), id(self), tuple(self))

    def _is_dominated(self, other: Type['FitnessTuple']) -> bool:
        """Return True if the current fitness is dominated by the other one"""
        return tuple(self) > tuple(other)

    @staticmethod
    def sort(fmap: List[Tuple[Any, Type['FitnessTuple']]]) -> List[Tuple[Any, Type['FitnessTuple']]]:
        """Sort a list of tuple (Any, FitnessTuple)

        Args:
            fmap: list of tuple (Any, FitnessTuple)

        Returns:
            an ordered list of tuples (Any, FitnessTuple)
        """
        fmap.sort(key=operator.itemgetter(1), reverse=True)
        return fmap
