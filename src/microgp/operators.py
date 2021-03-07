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

from typing import List

from .genoperator import GenOperator
from .utils import logging
from microgp import random_generator


class Operators:
    # TODO: Double Check
    """This class wraps all operators, manages statistics, and GenOperator
    selection. The selection is made on the basis of the arity and the
    success and failure statistics of the operator.

    **Examples:**

    - Create and fill an Operators object to be passed to a Darwin object

    >>> operators = ugp4.Operators()
    >>> init_op1 = ugp4.GenOperator(ugp4.create_random_individual, 0)
    >>> operators += init_op1
    >>> mutation_op1 = ugp4.GenOperator(ugp4.remove_node_mutation, 1)
    >>> operators += mutation_op1
    >>> crossover_op1 = ugp4.GenOperator(ugp4.switch_proc_crossover, 2)
    >>> operators += crossover_op1
    >>> crossover_op2 = ugp4.GenOperator(ugp4.five_individuals_crossover, 5)
    >>> operators += crossover_op2

    - Select k operators that has arity in the given range

    >>> selected_operators = operators.select(max_arity=0, k=10)
    >>> selected_operators = operators.select(min_arity=1, max_arity=2 k=20)
    """

    def __init__(self) -> None:
        self._gen_operators = list()
        self.stats = dict()

    def __iadd__(self, gen_operator: GenOperator) -> 'Operators':
        """Insert in the list of GenOperators the passed GenOperator"""
        assert gen_operator, "gen_operator can't be None"
        assert isinstance(gen_operator, GenOperator), "gen_operator must be a GenOperator type"
        if gen_operator not in self._gen_operators:
            self._gen_operators.append(gen_operator)
        else:
            logging.debug(f"\"{gen_operator}\" is already in the list of operators")
        return self

    def __isub__(self, gen_operator: GenOperator) -> 'Operators':
        """Remove in the list of GenOperators the passed GenOperator"""
        assert gen_operator, "gen_operator can't be none"
        assert isinstance(gen_operator, GenOperator), "gen_operator must be a GenOperator type"
        if gen_operator in self._gen_operators:
            self._gen_operators.remove(gen_operator)
        else:
            logging.debug(f"There is not \"{gen_operator}\" in the list of operators")
        return self

    def __contains__(self, operator_to_find) -> bool:
        """Check if the passed GenOperator is in the list of GenOperators"""
        for operator in self._gen_operators:
            if operator == operator_to_find:
                return True
        return False

    def select(self, min_arity: int = 0, max_arity: int = None) -> GenOperator:
        """Select a set of operators with arity in [min_arity, max_arity]

        Args:
            min_arity (int): minimum arity of the operators that will be returned
            max_arity (int): maximum arity of the operators that will be returned
            k (int): number of genetic operators to return

        Returns:
            a valid genetic operator
        """
        assert max_arity is None or min_arity <= max_arity, "min_arity must be <= then max_arity"
        assert min_arity >= 0 and (max_arity is None or max_arity >= 0), "Both min_arity and max_arity must be >= 0"
        assert len(self._gen_operators) > 0, "No operators available"

        valid_operators = list()
        for candidate_operator in self._gen_operators:
            if candidate_operator.arity >= min_arity and (max_arity is None or candidate_operator.arity <= max_arity):
                valid_operators.append(candidate_operator)

        assert len(valid_operators) > 0, "No operators available for the given set of arities"

        # TODO: consider statistics in future implementations
        operator = random_generator.choice(valid_operators)
        return operator

    @property
    def functions(self):
        return [function[0] for function in self._gen_operators]
