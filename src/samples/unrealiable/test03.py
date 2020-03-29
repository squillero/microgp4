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
    ugp.logging.cpu_info("Program started")

    # Define parameters
    reg_alternatives = ['%eax', '%ebx', '%ecx', '%edx']
    reg_param = ugp.make_parameter(ugp.parameter.Categorical, alternatives=reg_alternatives)
    instr_alternatives = ['add', 'sub', 'and', 'or', 'xor', 'cmp']
    instr_param = ugp.make_parameter(ugp.parameter.Categorical, alternatives=instr_alternatives)
    shift_alternatives = ['shr', 'shl']
    shift_param = ugp.make_parameter(ugp.parameter.Categorical, alternatives=shift_alternatives)
    jmp_alternatives = ['ja', 'jz', 'jnz', 'je', 'jne', 'jc', 'jnc', 'jo', 'jno', 'jmp']
    jmp_instructions = ugp.make_parameter(ugp.parameter.Categorical, alternatives=jmp_alternatives)
    integer = ugp.make_parameter(ugp.parameter.Integer, min=-32768, max=32767)
    int8 = ugp.make_parameter(ugp.parameter.Integer, min=0, max=256)
    jmp_target = ugp.make_parameter(ugp.parameter.LocalReference,
                                    allow_self=False,
                                    allow_forward=True,
                                    allow_backward=False,
                                    frames_up=0)

    # Define the macros
    jmp1 = ugp.Macro("    {jmp_instr} {jmp_ref}", {'jmp_instr': jmp_instructions, 'jmp_ref': jmp_target})
    instr_op_macro = ugp.Macro("    {instr} {regS}, {regD}", {
        'instr': instr_param,
        'regS': reg_param,
        'regD': reg_param
    })
    instr_op_macro2 = ugp.Macro("    {instr} {regS}, {regD}", {
        'instr': instr_param,
        'regS': reg_param,
        'regD': reg_param
    })
    shift_op_macro = ugp.Macro("    {shift} ${int8}, {regD}", {'shift': shift_param, 'int8': int8, 'regD': reg_param})
    shift_op_macro2 = ugp.Macro("    {shift} ${int8}, {regD}", {'shift': shift_param, 'int8': int8, 'regD': reg_param})
    branch_macro = ugp.Macro("{branch} {jmp}", {'branch': jmp_instructions, 'jmp': jmp_target})

    init_macro = ugp.Macro(
        "    movl	${int_a}, %eax\n" + "    movl	${int_b}, %ebx\n" + "    movl	${int_c}, %ecx\n" +
        "    movl	${int_d}, %edx\n", {
            'int_a': integer,
            'int_b': integer,
            'int_c': integer,
            'int_d': integer
        })

    from microgp import random_generator

    # Define section
    #sec1 = ugp.make_section({jmp1, instr_op_macro, shift_op_macro}, size=(10, 10))
    sec1 = ugp.make_section({instr_op_macro, shift_op_macro}, size=(5, 50))

    # Create a constraints library
    library = ugp.Constraints(file_name="solution{id}.s")
    #library['main'] = ["prologue", {jmp1, init_macro, instr_op_macro, shift_op_macro}, "epilogue"]
    library['main'] = ["prologue", sec1, "epilogue"]

    def blackhole(*args):
        return [42]
    library.evaluator = ugp.fitness.make_evaluator(evaluator=blackhole, fitness_type=ugp.fitness.Lexicographic)


    # TODO: Separate from random_individual -> Individual and random_individual -> List[Individual]

    from tqdm import tqdm

    #for seed in tqdm(range(5000), ncols=78, dynamic_ncols=False, ascii=True, unit='t', unit_scale=False, bar_format='{n_fmt:>5s}/{total_fmt:5s}[{bar}]'):
    #'{percentage:3.0f}%|{bar}| {rate_fmt} {n_fmt}/{total_fmt} '
    for seed in tqdm(range(5000), ncols=78, dynamic_ncols=False, ascii=True, unit='t', unit_scale=False, bar_format='Testing: {percentage:3.2f}% completed @ {rate_fmt} ({remaining} remaining)'):
        ugp.random_generator.seed(seed)
        first = [f"{random_generator}"]
        for _ in range(5):
            i = ugp.create_random_individual(constraints=library)[0]
            first.append(f"{random_generator}")

        ugp.random_generator.seed(seed)
        second = [f"{random_generator}"]
        for _ in range(5):
            i = ugp.create_random_individual(constraints=library)[0]
            second.append(f"{random_generator}")

        assert first == second, "%d -> %s" % (seed, [(f, s) for f, s in zip(first, second) if f != s])

    sys.exit(0)
    # Evolve
    darwin.evolve()

    # Print best individuals
    logging.bare("These are the best ever individuals:")
    best_individuals = darwin.archive.individuals
    ugp.print_individual(best_individuals, plot=True, score=True)

    ugp.logging.cpu_info("Program completed")
    sys.exit(0)
