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
from typing import Union, Set

from .individual import Individual
from .individual_operators import order_by_fitness
from .utils import logging
from microgp import rnd


class Population:
    """This class contains the set of individuals composing the population and
    manages the selection, insertion, removal of the individuals based on the
    age or whether their phenotype is already in the population. A non-valid
    individual can't be inserted.

    .. _`Tournament selection`: https://en.wikipedia.org/wiki/Tournament_selection

    **Examples:**

    - Add a set of individuals in the population

    >>> darwin.population += set(list_of_individuals)

    - Add a single individual in the population

    >>> darwin.population += set(individual_A)
    >>> darwin.population += set(individual_B)

    - Remove a single individual from the population

    >>> darwin.population -= set(individual_A)

    - Remove multiple individuals (set) from the population

    >>> darwin.population = darwin.population - set(individual_A)

    - Retrieve from population an individual using tournament selection `Tournament selection`_

    >>> selected_individual = darwin.tournament_selection(tau)

    - Retrieve the entire set of individual contained in the population

    >>> population = darwin.population.individuals

    """

    def __init__(self) -> None:
        self._individuals = set()

    def select(self, tau: float = 2) -> Individual:
        """Select an individual from the population calling the
        tournament_selection(tau) method"""
        return self.tournament_selection(tau)

    def __iadd__(self, individuals: Union[Individual, Set[Individual]]) -> 'Population':
        """Insert an individual or a set of valid individual if they are not
        in the population and return the population object"""
        for individual in individuals:
            assert individual.is_valid(), 'Individual must be valid to be added to population'
            # Check if the individual is not already in he list
            if not individual in self._individuals:
                self._individuals.add(individual)
        return self

    def __isub__(self, individual: Individual) -> 'Population':
        """Remove the passed individual from the population if present.
        Return the population object"""
        if individual in self._individuals:
            logging.debug("The selected individual can't be removed from population (it is not inside it)")
            self._individuals.remove(individual)
        return self

    def __sub__(self, set_to_except: Set[Individual]) -> Set[Individual]:
        """Perform the difference between the population and the given set"""
        return self._individuals.difference(set_to_except)

    def __len__(self) -> int:
        return len(self._individuals)

    def tournament_selection(self, tau: float = 2) -> Individual:
        """Run several tournaments among a few (floor(tau) or ceil(tau))
        individuals and return the best one based on the fitness"""
        assert self._individuals, 'There are not individuals in the population'
        individuals = rnd.choices(list(self._individuals), k=int(tau))
        if rnd.random() < (tau - int(tau)):
            individuals.append(rnd.choice(self._individuals))
        best = order_by_fitness(individuals)[0]
        return best

    @staticmethod
    def grow_old(individuals: Set[Individual]) -> None:
        """Increment the age of a set of individuals. Typically the set is
        {Population - Archive}"""
        for individual in individuals:
            individual.age += 1

    def filter_by_age(self, max_age: int = None) -> None:
        """Remove from the population the individuals that are too old
        (individual.age >= max_age)"""
        assert max_age is not None and max_age > 0, "Max age not specified or <= 0"
        young_individuals = set()
        for individual in self._individuals:
            if individual.age < max_age:
                young_individuals.add(individual)
        self._individuals = young_individuals

    @staticmethod
    def filter_clones() -> None:
        """Check whether or not there are individuals with the same
        (canonical) phenotype and then remove them"""
        # TODO: for future implementations: check if the phenotype (canonic) is identical
        #  (consider doing it in population.__iadd__)
        # print("Filter clones not implemented")
        pass

    @property
    def individuals(self) -> Set[Individual]:
        return self._individuals
