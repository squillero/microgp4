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

# Copyright 2020-2021 Giovanni Squillero and Alberto Tonda
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
from typing import Type, Any, List, Tuple

from .base import Base


class FitnessTupleMultiobj(tuple, Base):
    """Fitness used for multiple objective purposes."""

    def __bool__(self) -> bool:
        return all(v is not None for v in tuple(self))

    def __gt__(self, other: "FitnessTupleMultiobj") -> bool:
        raise NotImplementedError

    def __eq__(self, other: "FitnessTupleMultiobj") -> bool:
        return tuple(self) == tuple(other)

    def __ne__(self, other: "FitnessTupleMultiobj") -> bool:
        return tuple(self) != tuple(other)

    def __ge__(self, other: "FitnessTupleMultiobj") -> bool:
        return tuple(self) > tuple(other) or tuple(self) == tuple(other)

    def __lt__(self, other: "FitnessTupleMultiobj") -> bool:
        return not tuple(self) >= tuple(other)

    def __le__(self, other: "FitnessTupleMultiobj") -> bool:
        return not tuple(self) > tuple(other)

    def __str__(self) -> str:
        if len(self) > 1:
            return "%s%s" % (self.__class__.__name__, str(tuple(self)))
        else:
            return "%s(%s)" % (self.__class__.__name__, str(self[0]))

    def __repr__(self):
        return "<{} at {} {}>".format(type(self), id(self), tuple(self))

    def _is_dominated(self, other: Type['FitnessTupleMultiobj']) -> bool:
        """Return True if the current fitness is dominated by the other one"""
        return any(z[0] > z[1] for z in zip(self, other)) and all(z[0] >= z[1] for z in zip(self, other))

    @staticmethod
    def sort(fmap: List[Tuple[Any, Type['FitnessTupleMultiobj']]]) -> List[Tuple[Any, Type['FitnessTupleMultiobj']]]:
        """Sort a list of tuple (Any, FitnessTupleMultiobj) using Pareto front

        Args:
            fmap: list of tuple (Any, FitnessTupleMultiobj)

        Returns:
            an ordered list of tuples (Any, FitnessTupleMultiobj)
        """
        # Ranking will contain as key the tuple: (Individual, Individual.fitness) and as value the ranking position
        ranking = dict()
        pos = 0
        # Continue until fmap contains elements
        while len(fmap) > 0:
            # Check each tuple left in the list
            for individual, current_fitness in fmap:
                # Check if the actual individual is not dominated by any of the others
                if all(not individual.fitness.is_dominated(individual.fitness, other=e.fitness)
                       for e in {i for i, f in fmap if i != individual}):
                    # Insert the individual in the ranking
                    ranking[(individual, current_fitness)] = pos
            # Remove the just ranked individuals (keys with value == pos
            for individual_fitness_tuple in {k for k, v in ranking if v == pos}:
                fmap.remove(individual_fitness_tuple)
            pos += 1
        return [k for k, v in sorted(ranking.items(), key=lambda x: x[1])]
        # Example:
        # real_order[
        #     {ind3, ind2},
        #     {ind5, ind1, ind7},
        #     {ind4},
        #     {ind6, ind8},
        #     {ind9}
        # ]
        # ranking = {
        #     (ind1, ind1.fitness): 2,
        #     (ind2, ind2.fitness): 1,
        #     (ind3, ind3.fitness): 1,
        #     (ind4, ind4.fitness): 3,
        #     (ind5, ind5.fitness): 2,
        #     (ind6, ind6.fitness): 4,
        #     (ind7, ind7.fitness): 2,
        #     (ind8, ind8.fitness): 4,
        #     (ind9, ind9.fitness): 5
        # }
        # returned_value = [
        #     (ind2, ind2.fitness)
        #     (ind3, ind3.fitness)
        #     (ind1, ind1.fitness)
        #     (ind5, ind5.fitness)
        #     (ind7, ind7.fitness)
        #     (ind4, ind4.fitness)
        #     (ind6, ind6.fitness)
        #     (ind8, ind8.fitness)
        #     (ind9, ind9.fitness)
        # ]
