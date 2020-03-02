"""""""
Fitness
"""""""

.. toctree::
    :caption: Fitness
    :maxdepth: 2

The library allows the use two main types of fitnesses (FitnessTuple,
FitnessTupleMultiobj), both inherit from the Base class.

Base fitness class
==================

:mod:`microgp.fitness.base`

.. automodule:: microgp.fitness.base
    :members:

The method calling the correspondent ``Base.sort()`` is:

.. autoclass:: microgp.individual_operators.order_by_fitness

Fitness Tuple
=============
.. image:: fitnesstuple_class_schema.jpg
  :width: 800
  :alt: Class schema

:mod:`microgp.fitness.fitnesstuple`

.. automodule:: microgp.fitness.fitnesstuple
    :members:

:mod:`microgp.fitness.simple`

.. automodule:: microgp.fitness.simple
    :members:

:mod:`microgp.fitness.lexicographic`

.. automodule:: microgp.fitness.lexicographic
    :members:

Fitness Tuple Multiobjective
============================
.. image:: fitnesstuplemultiobj_class_schema.jpg
  :width: 800
  :alt: Class schema

:mod:`microgp.fitness.fitnesstuplemultiobj`

.. automodule:: microgp.fitness.fitnesstuplemultiobj
    :members:
Sorting example considering an input of type List[Individual, FitnessTupleMultiobj].

    .. code:: python

        real_order[
            {ind3, ind2},
            {ind5, ind1, ind7},
            {ind4},
            {ind6, ind8},
            {ind9}
        ]
        ranking = {
            (ind1, ind1.fitness): 2,
            (ind2, ind2.fitness): 1,
            (ind3, ind3.fitness): 1,
            (ind4, ind4.fitness): 3,
            (ind5, ind5.fitness): 2,
            (ind6, ind6.fitness): 4,
            (ind7, ind7.fitness): 2,
            (ind8, ind8.fitness): 4,
            (ind9, ind9.fitness): 5
        }
        returned_value = [
            (ind2, ind2.fitness)
            (ind3, ind3.fitness)
            (ind1, ind1.fitness)
            (ind5, ind5.fitness)
            (ind7, ind7.fitness)
            (ind4, ind4.fitness)
            (ind6, ind6.fitness)
            (ind8, ind8.fitness)
            (ind9, ind9.fitness)
        ]

:mod:`microgp.fitness.lexicase`

.. automodule:: microgp.fitness.lexicase
    :members:

:mod:`microgp.fitness.aggregate`

.. automodule:: microgp.fitness.aggregate
    :members:

:mod:`microgp.fitness.chromatic`

.. automodule:: microgp.fitness.chromatic
    :members:

Evaluator
=========

:mod:`microgp.fitness.evaluator`

.. automodule:: microgp.fitness.evaluator
    :members: