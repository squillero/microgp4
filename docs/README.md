MicroGP is an evolutionary optimizer able to outperform both human experts and conventional heuristics in finding good solution of hard problems. It first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information. Different techniques --- some inspired by the mechanisms of natural evolution --- are used to explore efficiently the search space.

MicroGP is extremely versatile: it is able to tackle problem those solutions are simple fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines; moreover, candidate solutions can be evaluated using independent, proprietary external tools. 

* MicroGP4 is available as a [PyPi package](https://en.wikipedia.org/wiki/Python_Package_Index) and using it is as simple as [`pip install microgp`](https://pypi.org/project/microgp/)
* The user guide and API reference are hosted on [Read tThe Docs](https://en.wikipedia.org/wiki/Read_the_Docs) at [https://microgp4.readthedocs.io/](https://microgp4.readthedocs.io/). 

MicroGP first prototype was created around 2000, a fully working version was coded in C in 2002 and then re-engineered in C++ in 2006. The forth version is in Python, redesigned from scratch to take advantage of the peculiar features of the language and to exploit its huge standard library. 

MicroGP4 is [free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software) and it is distributed under the permissive [Apache License 2.0](https://www.tldrlegal.com/l/apache2).
