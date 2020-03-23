MicroGP is an evolutionary optimizer able to outperform both human experts and conventional heuristics in finding good solution of generic, hard problems. It first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information. [Several different techniques](https://scholar.google.com/scholar?q=%28+squillero+OR+tonda+%29+AND+microgp) -- some inspired by the mechanisms of [natural evolution](https://en.wikipedia.org/wiki/Evolutionary_computation) -- are used to explore efficiently the search space, and eventually pinpoint the best solution.

MicroGP is extremely versatile: it is able to tackle problem those solutions are fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines; candidate solutions can be evaluated using an independent, proprietary external tool. 

* Documentation on [ReadTheDocs](https://microgp4.readthedocs.io/)
* Package on [PyPi](https://pypi.org/project/microgp/)

###### MicroGP4 is [free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software) and it is distributed under the permissive [Apache License 2.0](https://www.tldrlegal.com/l/apache2).

