.. MicroGP4 documentation master file, created by
   sphinx-quickstart on Thu Dec 12 15:32:24 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

"""""""""""""""""""
Welcome to MicroGP4
"""""""""""""""""""

What is MicroGP v4?
===================

**microGP** is an evolutionary optimizer able to outperform both human experts and
conventional heuristics in finding the optimal solution of generic problems.
It is extremely versatile, being able to tackle problem those solutions are
fixed-length bit strings, as well as to optimize realistic assembly programs
including loops, interrupts and recursive sub routines.

Installation guide
------------------
You can install microGPv4 along with all its dependencies from `PyPI`_

.. code:: bash

   $ pip install microgp

.. _PyPI: https://pypi.org/project/microgp/#description

Source code
___________

The source code and minimal working examples can be found on `GitHub`_ or you
can just clone here

.. code:: bash

    $ git clone https://github.com/squillero/microgp4.git

.. _GitHub: https://github.com/squillero/microgp4


.. toctree::
   :caption: User Guide
   :maxdepth: 4

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
   license

| **Copyright 2020 Giovanni Squillero and Alberto Tonda**
| MicroGP v4 is `free and open-source software`_, and it is distributed under the permissive `Apache-2.0 license`_.

.. _free and open-source software: https://en.wikipedia.org/wiki/Free_and_open-source_software
.. _Apache-2.0 license: https://tldrlegal.com/license/apache-license-2.0-%28apache-2.0%29

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
