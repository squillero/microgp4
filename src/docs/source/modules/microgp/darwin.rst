"""""""
Darwin
"""""""

.. toctree::
    :caption: Darwin
    :maxdepth: 4

The :mod:`microgp.darwin.Darwin` class is in charge of handling the whole
evolutionprocess. It contains:

- :doc:`constraints` (:mod:`microgp.constraints.Constraints`) that must be the same for each individual managed by Darwin;

- `Population`_ (:mod:`microgp.population.Population`) that manages the set of individuals present in the current generation;

- `Archive`_ (:mod:`microgp.archive.Archive`) that manages the best individuals ever contained in the population;

- `Operators`_ (:mod:`microgp.operators.Operators`) that wraps all the `GenOperator`_ (:mod:`microgp.genoperator.GenOperator`), manages statistics, and operator selection;

- other evolution parameters such as selection pressure, population size, number of operators to use for the first generation, maximum age of an individual, etc;


:mod:`microgp.darwin`

.. autoclass:: microgp.darwin.Darwin
    :members:

Population
==========

:mod:`microgp.population`

.. autoclass:: microgp.population.Population
    :members:


Archive
=======

:mod:`microgp.archive`

.. autoclass:: microgp.archive.Archive
    :members:

Operators
=========

:mod:`microgp.operators`

.. automodule:: microgp.operators
    :members:

GenOperator
***********

:mod:`microgp.genoperator`

.. automodule:: microgp.genoperator
    :members:

    .. automethod:: __init__
