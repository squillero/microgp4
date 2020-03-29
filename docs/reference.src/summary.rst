| *Truth emerges more readily from error than from confusion.*
|       ---  Francis Bacon (1561--1626)
|

""""""""""""""""
What is MicroGP?
""""""""""""""""

MicroGP is an :ref:`evolutionary algorithm <Natural and Artificial Evolution>` able to outperform both human experts and conventional heuristics in finding good solution of hard problems. It first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information. Different techniques are used to explore efficiently the search space.

MicroGP is extremely versatile: it is able to tackle problem those solutions are simple fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines; moreover, candidate solutions can be evaluated using independent, proprietary external tools. `Several papers <https://scholar.google.it/scholar?q=%28+MicroGP+OR+%C2%B5GP+%29+AND+%28+Squillero+OR+Tonda+%29>`_ reporting possible applications can be found in the scientific literature.

The :ref:`history <The story so far...>` of MicroGP started around 2000 with the creation of a collection of scripts for optimizing assembly-language programs, a fully working version was coded in C in 2002 and then re-engineered in C++ in 2006. The design of a Python version started in 2018. MicroGP4 would not have been possible without the help and support of :ref:`several people <µCredits>`.

Audience
========

The expected audience for MicroGP4 includes computer scientists, engineers and practitioners.

* MicroGP4 can be used interactively from a Jupyter notebook --- just like `scikit-learn <https://scikit-learn.org/>`_ and `keras <https://keras.io/>`_ --- allowing to quickly assess new ideas and build prototypes.
* An external tool can be used as evaluator, allowing to optimize virtually any problem.
* The evolutionary code can be tweaked with user-defined Python functions without the need to hack the core package itself.
* The modular design allows scholars to exploit MicroGP4 for testing new ideas and novel algorithms.

In the past, due to its ability to handle realistic assembly programs and to exploit a commercial simulator as evaluator, MicroGP has been extensively used for the test, verification and validation of programmable cores and sequential circuits.

Alternatives
============

Among the remarkable alternatives to MicroGP are:

- `ECJ <https://cs.gmu.edu/~eclab/projects/ecj/>`_ --- A Java-based Evolutionary Computation Research System
- `DEAP <https://deap.readthedocs.io/en/master/>`_ --- Distributed Evolutionary Algorithms in Python
- `inspyred  <https://aarongarrett.github.io/inspyred/>`_ --- A framework for creating bio-inspired computational intelligence algorithms in Python
- `Jenetics <https://jenetics.io/>`_ --- A Genetic Algorithm, Evolutionary Algorithm, Genetic Programming, and Multi-objective Optimization library, written in modern-day Java
- `Open BEAGLE <http://chgagne.github.io/beagle/>`_ --- A generic C++ framework for evolutionary computation

