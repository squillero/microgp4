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

# Copyright 2019 Giovanni Squillero and Alberto Tonda
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

import sys
import argparse

import microgp as ugp

from microgp.utils import logging

if __name__ == "__main__":
    ugp.banner()

    # Set the arguments parser _________________________________________________________________________________________
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

    ugp.logging.cpu_info("Program started")

    # Define parameters ________________________________________________________________________________________________
    registers = ugp.make_parameter(ugp.parameter.Categorical, alternatives=['ax', 'bx', 'cx', 'dx'])
    # cat_sor = ugp.make_parameter(ugp.parameter.CategoricalSorted,
    #                              alternatives=['e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'])
    int256 = ugp.make_parameter(ugp.parameter.Integer, min=0, max=256)
    # word8 = ugp.make_parameter(ugp.parameter.Bitstring, len_=8)
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

    # Define macros ____________________________________________________________________________________________________
    epilogue = ugp.Macro("; That's all folks")
    add = ugp.Macro("    add {reg}, 0{num:x}h  \t; ie. {reg} += {num}", {'reg': registers, 'num': int256})
    # add = ugp.Macro("    add {reg}, {num}b  \t; ie. {reg} += {num}", {'reg': cat_sor, 'num': bitstring8})
    sub = ugp.Macro("    sub {reg}, 0{num:x}h  \t; ie. {reg} -= {num}", {'reg': registers, 'num': int256})
    # sub = ugp.Macro("    sub {reg}, {num}b  \t; ie. {reg} -= {num}", {'reg': cat_sor, 'num': bitstring8})
    jmp1 = ugp.Macro("    jmp {jmp_ref} \t\t; jump forward", {'jmp_ref': ref_fwd})
    jmp2 = ugp.Macro("    jmp {jmp_ref} \t\t; jump backward", {'jmp_ref': ref_bcw})

    # That's the library

    # Assigning to the library calls `make_section` to all elements, in more details:
    # a sequence of sections is transformed in a SubsectionsSequence
    # a set of sections, in a SubsectionsAlternative
    # a set of macros, in a MacroPool
    # a macro, in a MacroPool containing only the very same macro
    # a string, in a parameter-less macro -- ie. string -> macro -> macro pool
    # make_section can still be useful to tweak the number of macros eg. size=(min, max)
    # or to customize the label format eg. label_format="[label_{node}]\n"

    # Define sections __________________________________________________________________________________________________
    sec2a = ugp.make_section({add}, size=(2, 5), name='sec2a', instances=(0, 1))
    sec2b = ugp.make_section({sub}, size=(4, 10), name='sec2b', instances=(0, 1))
    sec_jmp = ugp.make_section({jmp1, jmp2}, size=(5, 5), name='sec_jmp')
    # sec2a = ugp.make_section({add}, size=(1, 3), name='sec2a', instances=(0, 1))
    # sec2b = ugp.make_section({sub}, size=(2, 3), name='sec2b', instances=(0, 1))
    # sec_jmp = ugp.make_section({jmp1, jmp2}, size=(2, 3), name='sec_jmp')

    # Note the wickedness: there can be ONLY ONE sec2a and ONE sec2b, but the library specifies
    # { sec2a OR sec2b } THEN sec_jmp THEN { sec2a OR sec2b }
    # ... we are going to create quite a number of illegal individuals :-)

    # Set the created sections in the special section ('main') _________________________________________________________
    library = ugp.Constraints()
    library['main'] = [
        "; Prologue\n; Created on: {info:now} by {info}",
        [{sec2a, sec2b}, sec_jmp, {sec2a, sec2b}],  # framing is useful: sec_jmp references specify frames_up=1
        "; That's all folks"
    ]
    library['proc'] = []
    # Create a new checker function ____________________________________________________________________________________
    library.global_properties.add_checker(lambda **v: True)

    # Delete old solutions
    ugp.delete_solutions()

    if sys.platform != "win32":
        script = "./evaluator.sh"
    else:
        script = "evaluator.bat"
    library.evaluator = ugp.fitness.make_evaluator(evaluator=script, fitness_type=ugp.fitness.Lexicographic)

    # let's get weird
    # also note that there is only a limited number of instances that can be ==
    # sec2a.properties.add_cumulative_builder(lambda num_nodes, **v: {'sec2a': num_nodes})
    # sec2b.properties.add_cumulative_builder(lambda **v: {'sec2b': v['num_no des']})
    # library.global_properties.add_check(lambda sec2a, sec2b, **v: sec2a == sec2b)

    # Create a list of operators with their arities_____________________________________________________________________
    operators = ugp.Operators()

    # Add initialization operators
    init_op1 = ugp.GenOperator(ugp.create_random_individual, 0)
    operators += init_op1

    # Add mutation operators
    mutation_op1 = ugp.GenOperator(ugp.remove_node_mutation, 1)
    mutation_op2 = ugp.GenOperator(ugp.add_node_mutation, 1)
    mutation_op3 = ugp.GenOperator(ugp.flat_mutation, 1)
    mutation_op4 = ugp.GenOperator(ugp.hierarchical_mutation, 1)
    operators += mutation_op1
    operators += mutation_op2
    operators += mutation_op3
    operators += mutation_op4

    # Add crossover operators
    crossover_op1 = ugp.GenOperator(ugp.switch_proc_crossover, 2)
    crossover_op2 = ugp.GenOperator(ugp.macro_pool_uniform_crossover, 2)
    crossover_op3 = ugp.GenOperator(ugp.macro_pool_one_cut_point_crossover, 2)
    operators += crossover_op1
    operators += crossover_op2
    operators += crossover_op3

    # Create the object that will manage the evolution__________________________________________________________________
    mu = 10
    nu = 20
    sigma = 0.5
    lambda_ = 10
    max_age = 5

    darwin = ugp.Darwin(
        constraints=library,
        operators=operators,
        mu=mu,
        nu=nu,
        lambda_=lambda_,
        sigma=sigma,
        max_age=max_age
    )

    # Evolve____________________________________________________________________________________________________________
    darwin.evolve()
    logging.bare("This is the population:")
    for individual in darwin.population:
        ugp.print_individual(individual, plot=True)
        ugp.logging.bare(individual.fitness)

    # Print best individuals
    logging.bare("These are the best ever individuals:")
    ugp.print_individual(darwin.archive)

    # bests = darwin.archive.individuals
    # for best in bests:
    #     print(best.fitness)

    ugp.delete_solutions()

    ugp.logging.verbose(library.stats)
    ugp.logging.cpu_info("Program completed")
    ugp.delete_solutions()
    sys.exit(0)
