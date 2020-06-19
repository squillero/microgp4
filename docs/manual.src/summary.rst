| *Truth emerges more readily from error than from confusion.*
|       ---  Francis Bacon (1561--1626)
|

""""""""""""""""
What is MicroGP?
""""""""""""""""

MicroGP is an :ref:`evolutionary optimizer <Natural and Artificial Evolution>`: given a problem, it first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information. MicroGP is extremely versatile: it is able to tackle problem those solutions are simple fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines; moreover, candidate solutions can be evaluated using proprietary external tools.

MicroGP routinely outperforms both human experts and conventional heuristics, and over the years has been exploited as a coverage-driven `fuzzer <https://en.wikipedia.org/wiki/Fuzzing>`_, as a general-purpose `optimizer <https://en.wikipedia.org/wiki/Engineering_optimization>`_, and as a framework for prototyping and testing new ideas. `Several papers <https://scholar.google.com/scholar?q=%28+MicroGP+OR+%C2%B5GP+OR+ugp3+%29+AND+%28+Squillero+OR+Tonda+OR+Sanchez+OR+Schillaci+%29>`_ discussing possible applications can be found in the scientific literature.

Audience
========

The expected audience for MicroGP4 includes computer scientists, engineers and practitioners.

* MicroGP4 is available as a `PyPi package <https://pypi.org/project/microgp/>`_ and it can be easily installed using `pip <https://en.wikipedia.org/wiki/Pip_%28package_manager%29>`_.
* MicroGP4 can be used interactively from a Jupyter notebook --- just like `scikit-learn <https://scikit-learn.org/>`_ and `keras <https://keras.io/>`_ --- allowing to quickly assess new ideas and build prototypes.
* An external tool can be used as evaluator, allowing to handle virtually any problem.
* The evolutionary code can be tweaked injecting user-defined Python functions, without the need to hack the package itself.
* The modular design allows scholars to exploit MicroGP4 for testing new ideas and novel algorithms.

In the past, due to its ability to handle realistic assembly programs and to exploit commercial simulators, MicroGP has been extensively used for the test, verification and validation of programmable cores and sequential circuits.

History
=======

The MicroGP project :ref:`started around the year 2000 <The story so far...>`, with the creation of a collection of scripts for optimizing assembly-language programs. A fully working program was first coded in C in 2002, and then re-engineered in C++ in 2006; the design of a Python version started in 2018. MicroGP4 would not have been possible without the help and support of :ref:`several people <µCredits>`.

Alternatives
============

Among the remarkable alternatives to MicroGP are:

- `ECJ <https://cs.gmu.edu/~eclab/projects/ecj/>`_ --- A Java-based Evolutionary Computation Research System
- `DEAP <https://deap.readthedocs.io/en/master/>`_ --- Distributed Evolutionary Algorithms in Python
- `inspyred  <https://aarongarrett.github.io/inspyred/>`_ --- A framework for creating bio-inspired computational intelligence algorithms in Python
- `Jenetics <https://jenetics.io/>`_ --- A Genetic Algorithm, Evolutionary Algorithm, Genetic Programming, and Multi-objective Optimization library, written in modern-day Java
- `Open BEAGLE <http://chgagne.github.io/beagle/>`_ --- A generic C++ framework for evolutionary computation

