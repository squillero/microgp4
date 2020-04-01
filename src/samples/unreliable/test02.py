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

import argparse
import sys

import microgp as ugp
from microgp.utils import logging

if __name__ == "__main__":
    ugp.show_banner()

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
        ugp.logging.DefaultLogger.setLevel(level=ugp.logging.INFO)
    elif args.verbose == 1:
        ugp.logging.DefaultLogger.setLevel(level=ugp.logging.VERBOSE)
    elif args.verbose > 1:
        ugp.logging.DefaultLogger.setLevel(level=ugp.logging.DEBUG)
        ugp.logging.debug("Verbose level set to DEBUG")

    ugp.logging.log_cpu(ugp.logging.INFO, "Program started")

    ref_fwd = ugp.make_parameter(ugp.parameter.LocalReference,
                                 allow_self=False,
                                 allow_forward=True,
                                 allow_backward=False,
                                 frames_up=1)
    ref_bcw = ugp.make_parameter(ugp.parameter.LocalReference,
                                 allow_self=False,
                                 allow_forward=False,
                                 allow_backward=True,
                                 frames_up=1)

    # define parameters
    registers = ugp.make_parameter(ugp.parameter.Categorical, alternatives=['ax', 'bx', 'cx', 'dx'])
    # registers_ordered = ugp.make_parameter(ugp.parameter.CategoricalSorted, alternatives=['a', 'a', 'a', 'd'])
    int256 = ugp.make_parameter(ugp.parameter.Integer, min=0, max=256)
    proc1 = ugp.make_parameter(ugp.parameter.ExternalReference, section_name='proc1', min=5, max=5)
    proc2 = ugp.make_parameter(ugp.parameter.ExternalReference, section_name='proc2', min=5, max=5)
    proc3 = ugp.make_parameter(ugp.parameter.ExternalReference, section_name='proc3', min=5, max=5)
    proc4 = ugp.make_parameter(ugp.parameter.ExternalReference, section_name='proc4', min=5, max=5)

    # define macros
    add = ugp.Macro("    add {reg}, 0{num:x}h  \t; ie. {reg} += {num}", {'reg': registers, 'num': int256})
    sub = ugp.Macro("    sub {reg}, 0{num:x}h  \t; ie. {reg} -= {num}", {'reg': registers, 'num': int256})
    call1 = ugp.Macro("    call {reference}", {'reference': proc1})
    # call2 = ugp.Macro("    call {reference}", {'reference': proc2})
    call3 = ugp.Macro("    call {reference}", {'reference': proc3})
    call4 = ugp.Macro("    call {reference}", {'reference': proc4})
    call2 = ugp.Macro("    call {reference} and then call {reference2}", {'reference': proc2, 'reference2': proc3})
    jmp1 = ugp.Macro("    jmp {jmp_ref} \t\t; jump forward", {'jmp_ref': ref_fwd})
    jmp2 = ugp.Macro("    jmp {jmp_ref} \t\t; jump backward", {'jmp_ref': ref_bcw})

    # define sections
    generic_math = ugp.make_section({add, sub}, size=(2, 5), instances=(0, 10))
    # generic_math = ugp.make_section({add, sub}, size=(1, 2), instances=(0, 10))

    # Create a constraints library
    library = ugp.Constraints()

    sec_jmp = ugp.make_section(jmp1, size=(1, 4), name='sec_jmp')
    sec2_jmp = ugp.make_section({jmp1, jmp2}, size=(3, 5), name='sec_jmp2')
    library['main'] = [generic_math, sec_jmp, {call1, call2}, {call3, call4}, call2, "\t; ----", generic_math, ""]
    # library['main'] = [generic_math, [jmp1, add, call1, jmp2], sec_jmp, {jmp1, jmp1}, call2, "\t; ----", generic_math, ""]
    # library['main'] = ["; main starts here", add, sub, call1, ""]

    library['proc1'] = ["proc {info:node} near", generic_math, call2, "endp", ""]
    library['proc2'] = ["proc {info:node} near", generic_math, add, "endp", ""]
    # library['proc2'] = ["proc {info:node} near", {add, sub}, jmp2, "endp", ""]
    library['proc3'] = ["proc {info:node} near", call4, {call2, add}, "endp", ""]
    library['proc4'] = ["proc {info:node} near", call3, "endp", ""]

    if sys.platform != "win32":
        script = "./evaluator.sh"
    else:
        script = "evaluator.bat"
    library.evaluator = ugp.fitness.make_evaluator(evaluator=script, fitness_type=ugp.fitness.Lexicographic)

    # let's get weird
    # also note that there is only a limited number of instances that can be ==
    # sec2a.properties.add_cumulative_builder(lambda num_nodes, **v: {'sec2a': num_nodes})
    # sec2b.properties.add_cumulative_builder(lambda **v: {'sec2b': v['num_nodes']})
    # library.global_properties.add_check(lambda sec2a, sec2b, **v: sec2a == sec2b)

    # Create a list of operators with their arities_____________________________________________________________________
    operators = ugp.Operators()

    # Add initialization operators
    init_op1 = ugp.GenOperator(ugp.create_random_individual, 0)
    operators += init_op1

    # Add mutation operators
    mutation_op1 = ugp.GenOperator(ugp.remove_node_mutation, 1)
    mutation_op2 = ugp.GenOperator(ugp.add_node_mutation, 1)
    mutation_op3 = ugp.GenOperator(ugp.hierarchical_mutation, 1)
    mutation_op4 = ugp.GenOperator(ugp.flat_mutation, 1)
    operators += mutation_op1
    operators += mutation_op2
    operators += mutation_op3
    operators += mutation_op4

    # Add crossover operators
    crossover_op1 = ugp.GenOperator(ugp.switch_proc_crossover, 2)
    crossover_op2 = ugp.GenOperator(ugp.macro_pool_one_cut_point_crossover, 2)
    crossover_op3 = ugp.GenOperator(ugp.macro_pool_uniform_crossover, 2)
    operators += crossover_op1
    # operators += crossover_op2
    # operators += crossover_op3

    # Create the object that will manage the evolution__________________________________________________________________
    mu = 10
    nu = 20
    sigma = 0.5
    lambda_ = 7
    max_age = 10

    for _ in range(1):
        darwin = ugp.Darwin(
            constraints=library,
            operators=operators,
            mu=mu,
            nu=nu,
            lambda_=lambda_,
            sigma=sigma,
            max_age=max_age,
        )

        # Evolve____________________________________________________________________________________________________________
        darwin.evolve()
        logging.bare("This is the final population:")
        for individual in darwin.population:
            ugp.print_individual(individual, plot=True)
            ugp.logging.bare(individual.fitness)
            ugp.logging.bare("")

        # Print best individuals
        logging.bare("These are the best ever individuals:")
        ugp.print_individual(darwin.archive.individuals)

    ugp.logging.log_cpu(ugp.logging.INFO, "Program completed")
    sys.exit(0)
