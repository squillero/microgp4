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

import argparse
import sys

import microgp as ugp
from microgp.utils import logging

if __name__ == "__main__":
    ugp.banner()

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

    # Delete old solutions
    ugp.delete_solutions()

    # Define parameters
    reg_alternatives = ['%eax', '%ebx', '%ecx', '%edx']
    instr_alternatives = ['add', 'sub', 'mov', 'and', 'or', 'xor', 'cmp']
    instr_op_alternatives = ['incl', 'decl', 'notl']
    branch_alternatives = ['ja', 'jz', 'jnz', 'je', 'jne', 'jc', 'jnc', 'jo', 'jno']
    reg_param = ugp.make_parameter(ugp.parameter.Categorical, alternatives=reg_alternatives)
    instr_param = ugp.make_parameter(ugp.parameter.Categorical, alternatives=instr_alternatives)
    bitstr_param = ugp.make_parameter(ugp.parameter.Bitstring, len_=32)  # {bitstr:02X}
    branch_param = ugp.make_parameter(ugp.parameter.Categorical, alternatives=branch_alternatives)
    jmp_param = ugp.make_parameter(ugp.parameter.LocalReference,
                                   allow_self=False,
                                   allow_forward=True,
                                   allow_backward=True,
                                   frames_up=0)
    instr_op_param = ugp.make_parameter(ugp.parameter.Categorical, alternatives=instr_op_alternatives)

    # Define the macros
    direct_macro = ugp.Macro("{instr} {regS}, {regD}", {'instr': instr_param, 'regS': reg_param, 'regD': reg_param})
    const_macro = ugp.Macro("{instr} %0x{bitstr}, {regD}",
                            {'instr': instr_param, 'bitstr': bitstr_param, 'regD': reg_param})
    instr_op_macro = ugp.Macro("{instr} {reg}", {'instr': instr_param, 'reg': reg_param})
    branch_macro = ugp.Macro("{branch} {jmp}", {'branch': branch_param, 'jmp': jmp_param})

    integer = ugp.make_parameter(ugp.parameter.Integer, min=-32768, max=32767)

    prologue_macro = ugp.Macro(""".text
	.globl	darwin
	.def	darwin;	.scl	2;	.type	32;	.endef
	.seh_proc	darwin
darwin:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	.seh_endprologue
""")

    init_macro = ugp.Macro("""
    movl	${int_a}, %eax
	movl	${int_b}, %ebx
	movl	${int_c}, %ecx
	movl	${int_d}, %edx
""", {'int_a': integer, 'int_b': integer, 'int_c': integer, 'int_d': integer})

    epilogue_macro = ugp.Macro("""
	popq	%rbp
	ret
	.seh_endproc
""")

    library = ugp.Constraints()
    library['main'] = [prologue_macro, init_macro, epilogue_macro]

    # Define the evaluator and the fitness type_________________________________________________________________________
    if sys.platform != "win32":
        script = "./evaluator_exp_02.sh"
    else:
        script = "./evaluator_exp_02.bat"
    library.evaluator = ugp.fitness.make_evaluator(evaluator=script, fitness_type=ugp.fitness.Lexicographic)

    # Create a list of operators with their arities_____________________________________________________________________
    operators = ugp.Operators()
    # Add initialization operators
    operators += ugp.GenOperator(ugp.create_random_individual, 0)
    # Add mutation operators
    operators += ugp.GenOperator(ugp.hierarchical_mutation, 1)
    operators += ugp.GenOperator(ugp.flat_mutation, 1)
    # Add crossover operators
    operators += ugp.GenOperator(ugp.macro_pool_one_cut_point_crossover, 2)
    operators += ugp.GenOperator(ugp.macro_pool_uniform_crossover, 2)

    # Create the object that will manage the evolution__________________________________________________________________
    mu = 10
    nu = 20
    sigma = 0.7
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
        ugp.print_individual(darwin.archive)

        ugp.delete_solutions()

    ugp.logging.cpu_info("Program completed")
    sys.exit(0)
