.. MicroGP4 documentation master file, created by
   sphinx-quickstart on Thu Dec 12 15:32:24 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _MicroGP2: https://github.com/squillero/microgp2
.. _MicroGP3: https://github.com/squillero/microgp3
.. _MicroGP4: https://github.com/squillero/microgp4/tree/pre-alpha
.. _FOSS: https://en.wikipedia.org/wiki/Free_and_open-source_software
.. _Apache2: https://www.tldrlegal.com/l/apache2

.. _contents:

    *Truth emerges more readily from error than from confusion*

    -- Francis Bacon, c. 1610


Overview
========

MicroGP (µGP, ``ugp``) is an evolutionary optimizer able to outperform both human experts and conventional heuristics in finding the optimal solution of generic problems. It is extremely versatile, being able to tackle problem those solutions are fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines.

MicroGP first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information; `several different techniques <https://scholar.google.com/scholar?q=%28+squillero+OR+tonda+%29+AND+microgp>`__ --- some `inspired by the mechanisms of natural evolution <https://en.wikipedia.org/wiki/Evolutionary_computation>`__ --- are used to explore efficiently the search space, and eventually pinpoint the best solution.

Blah blah

Audience
--------

The audience for MicroGP includes ...

Free software
-------------

MicroGP4 is `free and open-source software </FOSS>`_, and it is distributed under the permissive `Apache License 2.0 </_Apache2>`_. We welcome contributions.

History
-------

MicroGP was designed around y2k; the first fully working version was `coded in C in 2002 </MicroGP2/MicroGP2>`_, then `re-engineered in C++ in 2006 </MicroGP3>`_. MicroGP4 has been re-designed in Python to simply its use and exploit the vibrant ecosystem of packages available.

MicroGP would not have been possible without the help and support of `several people <contributors>`__.

Documentation
-------------

 :Release: |version|
 :Date: |today|

.. toctree::

   :caption: API reference
   :maxdepth: 1

   install
   tutorial

   modules/microgp/individual
   modules/microgp/constraints
   modules/microgp/darwin
   modules/microgp/individual_operators
   modules/microgp/fitness/fitness
   modules/microgp/parameter/parameters
   modules/microgp/abstract

   news
   license
   credits
   citing
   bibliography
   auto_examples/index

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* :ref:`glossary`
