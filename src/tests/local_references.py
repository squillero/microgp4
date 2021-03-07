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

import argparse
import sys

import microgp as ugp4
from microgp.utils import logging

if __name__ == "__main__":
    ugp4.show_banner()

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase log verbosity")
    parser.add_argument("-d",
                        "--debug",
                        action="store_const",
                        dest="verbose",
                        const=2,
                        help="log debug messages (same as -vv)")
    args = parser.parse_args()

    if args.verbose == 0:
        ugp4.logging.DefaultLogger.setLevel(level=ugp4.logging.INFO)
    elif args.verbose == 1:
        ugp4.logging.DefaultLogger.setLevel(level=ugp4.logging.VERBOSE)
    elif args.verbose > 1:
        ugp4.logging.DefaultLogger.setLevel(level=ugp4.logging.DEBUG)
        ugp4.logging.debug("Verbose level set to DEBUG")

    # Local References
    generic = ugp4.make_parameter(ugp4.parameter.LocalReference,
                                  allow_self=True,
                                  allow_forward=True,
                                  allow_backward=True,
                                  frames_up=1)
    forward_only = ugp4.make_parameter(ugp4.parameter.LocalReference,
                                       allow_self=False,
                                       allow_forward=True,
                                       allow_backward=False,
                                       frames_up=1)
    forward_loose = ugp4.make_parameter(ugp4.parameter.LocalReference,
                                        allow_self=False,
                                        allow_forward=True,
                                        allow_backward=False,
                                        frames_up=1)
    backward_only = ugp4.make_parameter(ugp4.parameter.LocalReference,
                                        allow_self=False,
                                        allow_forward=False,
                                        allow_backward=True,
                                        frames_up=1)
    backward_loose = ugp4.make_parameter(ugp4.parameter.LocalReference,
                                         allow_self=True,
                                         allow_forward=False,
                                         allow_backward=True,
                                         frames_up=1)
    # Categorical
    variable = ugp4.make_parameter(ugp4.parameter.Categorical, alternatives=['foo', 'bar', 'baz'])
    # Integer
    int256 = ugp4.make_parameter(ugp4.parameter.Integer, min=0, max=256)

    # define macros
    assign = ugp4.Macro("{var} := {val}", {'var': variable, 'val': int256})
    jmps = ugp4.Macro(
        "back {back}\nback_loose {back_loose}\ngeneric {generic}\nforward {forward}\nforward_loose {forward_loose}", {
            'back': backward_only,
            'back_loose': backward_loose,
            'generic': generic,
            'forward': forward_only,
            'forward_loose': forward_loose
        })
    filler = ugp4.make_section({assign}, size=(2, 5), instances=(0, 10))

    # library
    library = ugp4.Constraints()
    library['main'] = ["\t; BEGIN", filler, jmps, filler, "\t; END"]

    def f(individual):
        return 42

    library.evaluator = ugp4.fitness.make_evaluator(evaluator=f, fitness_type=ugp4.fitness.Simple)

    # Create a list of operators with their arities_____________________________________________________________________
    operators = ugp4.Operators()
    operators += ugp4.GenOperator(ugp4.create_random_individual, 0)
    operators += ugp4.GenOperator(ugp4.macro_pool_uniform_crossover, 2)

    # Create the object that will manage the evolution__________________________________________________________________
    mu = 10
    nu = 20
    strength = 0.5
    lambda_ = 7
    max_age = 10

    for _ in range(1):
        darwin = ugp4.Darwin(
            constraints=library,
            operators=operators,
            mu=mu,
            nu=nu,
            lambda_=lambda_,
            strength=strength,
            max_age=max_age,
        )

        # Evolve____________________________________________________________________________________________________________
        darwin.evolve()
        logging.bare("This is the final population:")
        for individual in darwin.population:
            ugp4.print_individual(individual)
            ugp4.logging.bare(individual.fitness)
            ugp4.logging.bare("")

        # Print best individuals
        logging.bare("These are the best ever individuals:")
        ugp4.print_individual(darwin.archive.individuals, plot=True)

    ugp4.logging.log_cpu(ugp4.logging.INFO, "Program completed")
    sys.exit(0)
