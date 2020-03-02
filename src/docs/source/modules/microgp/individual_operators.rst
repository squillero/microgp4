""""""""""""""""""""
Individual Operators
""""""""""""""""""""

.. toctree::
    :caption: Individual Operators
    :maxdepth: 2

.. _`crossover operators`: https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)
.. _`mutation operators`: https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm)

MicroGPv4 package offers some basic operators that can be found in
:mod:`microgp.individual_operators`. Three of them are `crossover operators`_,
four are `mutation operators`_ and one has the goal to create a random individual.
As you can see in :doc:`darwin`, the methods that are listed in this module can be
passed to the constructor of a `GenOperator` an then added to the list of
operators used by the :mod:`microgp.darwin.Darwin` object.

:mod:`microgp.individual_operators`

Initialization operator
=======================

This kind of operator doesn't receive any individual as input and returns a
new individual.

Create random individual
************************

.. automethod:: microgp.individual_operators.create_random_individual

fgh jMutation operators
==================

This kind of operator change one or more genes that describe an individual. The
intensity of the change and the probability that it takes place depend on
**sigma**. This is a parameter specified during the creation of the
:doc:`darwin` object and it can assume values in [0, 1].

The available `mutation operators`_ are:

- :mod:`microgp.individual_operators.remove_node_mutation`

- :mod:`microgp.individual_operators.add_node_mutation`

- :mod:`microgp.individual_operators.hierarchical_mutation`

- :mod:`microgp.individual_operators.flat_mutation`

Remove node mutation
********************

.. automethod:: microgp.individual_operators.remove_node_mutation

Add node mutation
*****************

.. automethod:: microgp.individual_operators.add_node_mutation

Hierarchical mutation
*********************

.. automethod:: microgp.individual_operators.hierarchical_mutation

Flat mutation
*************

.. automethod:: microgp.individual_operators.flat_mutation

Crossover operators
===================
.. _`OneCut crossover`: https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)#Single-point_crossover
.. _`Uniform crossover`: https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)#Uniform_crossover

The available `crossover operators`_ are:

- Switch procedure crossover: :mod:`microgp.individual_operators.switch_proc_crossover`

- MacroPool `OneCut crossover`_: :mod:`microgp.individual_operators.macro_pool_one_cut_point_crossover`

- MacroPool `Uniform crossover`_: :mod:`microgp.individual_operators.macro_pool_uniform_crossover`


Switch procedure crossover
**************************

.. automethod:: microgp.individual_operators.switch_proc_crossover

MacroPool OneCut crossover
**************************

.. automethod:: microgp.individual_operators.macro_pool_one_cut_point_crossover

MacroPool Uniform crossover
***************************

.. automethod:: microgp.individual_operators.macro_pool_uniform_crossover
