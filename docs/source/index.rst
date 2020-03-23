.. MicroGP4 documentation master file, created by
   sphinx-quickstart on Thu Dec 12 15:32:24 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

""""""""""""""""""""
Overview of MicroGP4
""""""""""""""""""""

MicroGP is an evolutionary optimizer able to outperform both human experts and conventional heuristics in finding good solution of generic, hard problems. It first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information; `several different techniques <https://scholar.google.com/scholar?q=%28+squillero+OR+tonda+%29+AND+microgp>`_ --- some inspired by the mechanisms of `natural evolution <https://en.wikipedia.org/wiki/Evolutionary_computation>`_ --- are used to explore efficiently the search space, and eventually pinpoint the best solution.

MicroGP is extremely versatile, being able to tackle problem those solutions are fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines. Moreover the tool used to evaluate candidate solutions can be loosely it is not bound to any specific  It provides:

MicroGP4 is `free and open-source software <https://en.wikipedia.org/wiki/Free_and_open-source_software>`_, and it is distributed under the permissive `Apache License 2.0 <https://www.tldrlegal.com/l/apache2>`_.

- foo
- bar
- baz

Audience
========

The expected audience for MicroGP includes computer scientists, engineers and practitioners. The simple Pythonic interface allows modern data scientist and industrial users to exploit it from an interactive notebooks; the modular design allows scholars to exploit it for testing new ideas and novel algorithms. Due to its ability to handle realistic assembly programs and exploit an external, commercial evaluator, MicroGP has been extensively used by engineers during the test, verification and validation of programmable cores and sequential circuits.

History
=======

MicroGP first prototype was created around `Y2K <https://github.com/squillero/microgp4/blob/pre-alpha/docs/history.rst>`_, a fully working version was `coded in C in 2002 <https://github.com/squillero/microgp2>`_ and then `re-engineered in C++ in 2006 <https://github.com/squillero/microgp3>`_. This is |ugp_name| (|ugp_version|), redesigned from scratch in Python to take advantage of the peculiar features of the language and to exploit its huge standard library.


See :doc:`summary` for more information.

Alternatives
============

Among the remarkable alternatives to MicroGP are:

- `DEAP <https://deap.readthedocs.io/en/master/>`_ --- Distributed Evolutionary Algorithms in Python
- `inspyred  <https://aarongarrett.github.io/inspyred/>`_ --- A framework for creating bio-inspired computational intelligence algorithms in Python
- `Jenetics <https://jenetics.io/>`_ --- a Genetic Algorithm, Evolutionary Algorithm, Genetic Programming, and Multi-objective Optimization library, written in modern-day Java


"""""""""""""""""
Table of Contents
"""""""""""""""""

.. toctree::
   :caption: User Guide
   :maxdepth: 4

   summary.rst
   modules/examples/exp01.rst
   modules/examples/exp02.rst


.. toctree::
   :caption: API reference
   :maxdepth: 4

   modules/microgp/individual
   modules/microgp/constraints
   modules/microgp/darwin
   modules/microgp/individual_operators
   modules/microgp/fitness/fitness
   modules/microgp/parameter/parameters
   modules/microgp/abstract

.. toctree::
   :caption: Copyright
   :maxdepth: 1

   authors
   contributors
   license

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

