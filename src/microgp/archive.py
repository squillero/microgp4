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
from .fitness.base import is_dominated
from .individual import Individual


class Archive:
    """This class manages the set of individuals not dominated by all other
    individuals currently or previously contained in the
    :mod:`microgp.darwin.Darwin._population`.

    **Examples:**

    - Try to insert an individual in the archive:

    >>> self._archive += individual

    The individual will be inserted only if it is not dominated by all
    individual already inside the archive. If it is not dominated then the
    individuals that just became dominated are removed from the archive.
    """

    def __init__(self) -> None:
        """Archive builder"""
        self._individuals = set()

    def __iadd__(self, candidate_individual: Individual) -> 'Archive':
        """Add to the archive a new individual if it is not dominated by any
        of the individuals already present. The individuals that just became
        dominated are removed from the archive.

        Args:
            candidate_individual: Individual to be inserted into the archive

        Returns:
            The archive just updated
        """
        if all(not is_dominated(e.fitness, candidate_individual.fitness) for e in self._individuals):
            self._individuals = {candidate_individual} | {
                e for e in set(self._individuals) if not is_dominated(candidate_individual.fitness, e.fitness)
            }
        return self

    def __str__(self) -> str:
        """Return a string with the phenotypes of all individuals inside the
        archive"""
        if not self._individuals:
            return "No individuals in archive"
        string = "\n;" + "-" * 76
        for individual in self._individuals:
            string += "\n" + str(individual) + "\n With score of: " + str(individual.fitness)
        string += "\n;" + "-" * 76
        return string

    @property
    def individuals(self):
        return self._individuals
