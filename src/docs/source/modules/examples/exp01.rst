.. MicroGPv4 documentation master file, created by
   sphinx-quickstart on Thu Dec 12 15:32:24 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

"""""""""""
OneMax Base
"""""""""""

.. _`OneMax problem`: https://link.springer.com/chapter/10.1007/978-3-540-24854-5_98

We will consider the `OneMax problem`_ as an example of a simple problem
solvable with Genetic Algorithms. Given a sequence `N` of random bits
composing a word (i.e. `10001010` 8 bits), the fitness score is given based on
the number of `ones` present (higher is better). The algorithm must generate a
random set of individuals (strings of bits), evolve them till they will
contain only ones.


OneMax Base version 1
*********************

In version one an individual is composed by a ``word_section`` which contains
a single macro (``word_macro``) with a parameter (``bit``) of type
:mod:`microgp.parameter.bitstring.Bitstring` of length 8 bits. The main
section contains a simple prologue and epilogue.

The evaluator in both versions is a Python method (``my_script``) returning an ``int`` value
that is the sum of `1` in the individual's phenotype.

.. code:: python

   import argparse
   import sys

   import microgp as ugp
   from microgp.utils import logging

   if __name__ == "__main__":
       ugp.banner()
       parser = argparse.ArgumentParser()
       parser.add_argument("-v", "--verbose", action="count", default=0, help="increase log verbosity")
       parser.add_argument("-d", "--debug", action="store_const", dest="verbose", const=2,
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


       # Define a parameter of type ugp.parameter.Bitstring and length = 8
       word8 = ugp.make_parameter(ugp.parameter.Bitstring, len_=8)
       # Define a macro that contains a parameter of type ugp.parameter.Bitstring
       word_macro = ugp.Macro("{word8}", {'word8': word8})
       # Create a section containing a macro
       word_section = ugp.make_section(word_macro, size=(1, 1), name='word_sec')

       # Create a constraints library
       library = ugp.Constraints()
       # Define the sections in the library
       library['main'] = ["Bitstring:", word_section]

       # Define the evaluator method and the fitness type
       def my_script(data: str):
           count = data.count('1')
           return list(str(count))

       library.evaluator = ugp.fitness.make_evaluator(evaluator=my_script, fitness_type=ugp.fitness.Lexicographic)

       # Create a list of operators with their aritiy
       operators = ugp.Operators()
       # Add initialization operators
       operators += ugp.GenOperator(ugp.create_random_individual, 0)
       # Add mutation operators
       operators += ugp.GenOperator(ugp.hierarchical_mutation, 1)
       operators += ugp.GenOperator(ugp.flat_mutation, 1)

       # Create the object that will manage the evolution
       mu = 10
       nu = 20
       sigma = 0.7
       lambda_ = 7
       max_age = 10

       darwin = ugp.Darwin(
           constraints=library,
           operators=operators,
           mu=mu,
           nu=nu,
           lambda_=lambda_,
           sigma=sigma,
           max_age=max_age,
       )

       # Evolve and print individuals in population
       darwin.evolve()
       logging.bare("This is the final population:")
       for individual in darwin.population:
           msg = f"Solution {str(individual.id)} "
           ugp.print_individual(individual, msg=msg, plot=True)
           ugp.logging.bare(f"Fitness: {individual.fitness}")
           ugp.logging.bare("")

       # Print best individuals
       ugp.print_individual(darwin.archive.individuals, msg="These are the best ever individuals:", plot=True)

       ugp.logging.cpu_info("Program completed")
       sys.exit(0)



OneMax Base version 2
*********************

In version two an individual is composed by a ``word_section`` which contains
exactly 8 macros (``word_macro``) with a parameter (``bit``) of type
:mod:`microgp.parameter.categorical.Categorical` that can assume as value: 1 or
0. The main section contains a simple prologue and epilogue.

.. code:: python

   import argparse
   import sys

   import microgp as ugp
   from microgp.utils import logging

   if __name__ == "__main__":
       ugp.banner()
       parser = argparse.ArgumentParser()
       parser.add_argument("-v", "--verbose", action="count", default=0, help="increase log verbosity")
       parser.add_argument("-d", "--debug", action="store_const", dest="verbose", const=2,
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

       # Define a parameter of type ugp.parameter.Categorical that can take two values: 0 or 1
       bit = ugp.make_parameter(ugp.parameter.Categorical, alternatives=[0, 1])

       # Define a macro that contains a parameter of type ugp.parameter.Categorical
       word_macro = ugp.Macro("{bit}", {'bit': bit})

       # Create a section containing 8 macros
       word_section = ugp.make_section(word_macro, size=(8, 8), name='word_sec')

       # Create a constraints library
       library = ugp.Constraints()
       library['main'] = ["Bitstring:", word_section]

       # Define the evaluator method and the fitness type
       def my_script(data: str):
           count = data.count('1')
           return list(str(count))
       library.evaluator = ugp.fitness.make_evaluator(evaluator=my_script, fitness_type=ugp.fitness.Lexicographic)

       # Create a list of operators with their arity
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

       darwin = ugp.Darwin(
           constraints=library,
           operators=operators,
           mu=mu,
           nu=nu,
           lambda_=lambda_,
           sigma=sigma,
           max_age=max_age,
       )

       # Evolve and print individuals in population
       darwin.evolve()
       logging.bare("This is the final population:")
       for individual in darwin.population:
           msg = f"Solution {str(individual.id)} "
           ugp.print_individual(individual, msg=msg, plot=True, score=True)

       # Print best individuals
       ugp.print_individual(darwin.archive.individuals, msg="These are the best ever individuals:", plot=True)

       ugp.logging.cpu_info("Program completed")
       sys.exit(0)
