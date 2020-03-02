.. MicroGPv4 documentation master file, created by
   sphinx-quickstart on Thu Dec 12 15:32:24 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

"""""""""""""""
OneMax Assembly
"""""""""""""""

See :doc:`exp01`.


The following code produces assembly code that can be run on x86 processors.
The goal is to generate an assembly function that writes 0xFFFFFFFF (32 1's
bit) to register eax. The secondary goal is to minimize the size of the
function.

The evaluator.........................

.. code:: python

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

       prologue_macro = ugp.Macro("	.text\n" +
                                  "    .globl	evolved_function\n" +
                                  "    .type	evolved_function, @function\n" +
                                  " evolved_function:\n" +
                                  " .LFB0:\n" +
                                  "    .cfi_startproc\n" +
                                  "    pushq %rbx\n" +
                                  "    pushq %rcx\n" +
                                  "    pushq %rdx\n" +
                                  "    movl $0x00000505, %eax\n" +
                                  "    movl $0x00050500, %ebx\n" +
                                  "    movl $0x00050500, %ecx\n" +
                                  "    movl $0x05050000, %edx")

       epilogue_macro = ugp.Macro("    popq %rdx " +
                                  "    popq %rcx\n" +
                                  "    popq %rbx\n" +
                                  "    ret\n" +
                                  "    .cfi_endproc\n" +
                                  ".LFE0:\n" +
                                  "    .size	evolved_function, .-evolved_function\n" +
                                  ".ident	\"MicroGP\"\n" +
                                  ".section	.note.GNU-stack,"",@progbits\n")

       # sec1 = ugp.make_section([direct_macro, ], size=(1, 1), name='sec1')
       prologue_sec = ugp.make_section(prologue_macro, size=(1, 1), name='pro_sec')
       epilogue_sec = ugp.make_section(epilogue_macro, size=(1, 1), name='epi_sec')

       # Create a constraints library
       library = ugp.Constraints()
       library['main'] = [prologue_sec, [direct_macro, const_macro, instr_op_macro, branch_macro], epilogue_sec]

       # Define the evaluator and the fitness type
       if sys.platform != "win32":
           script = "./evaluator_exp_02.sh"
       else:
           script = "./evaluator_exp_02.bat"
       library.evaluator = ugp.fitness.make_evaluator(evaluator=script, fitness_type=ugp.fitness.Lexicographic)

       # Create a list of operators with their arities
       operators = ugp.Operators()
       # Add initialization operators
       operators += ugp.GenOperator(ugp.create_random_individual, 0)
       # Add mutation operators
       operators += ugp.GenOperator(ugp.hierarchical_mutation, 1)
       operators += ugp.GenOperator(ugp.flat_mutation, 1)
       # Add crossover operators
       operators += ugp.GenOperator(ugp.macro_pool_one_cut_point_crossover, 2)
       operators += ugp.GenOperator(ugp.macro_pool_uniform_crossover, 2)

       # Create the object that will manage the evolution
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

           # Evolve
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
