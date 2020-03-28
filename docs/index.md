MicroGP is an [evolutionary optimizer](evolution.html) able to outperform both human experts and conventional heuristics in finding good solution of hard problems. It first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information. Different techniques are used to explore efficiently the search space.

MicroGP is extremely versatile: it is able to tackle problem those solutions are simple fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines; moreover, candidate solutions can be evaluated using independent, proprietary external tools. [Several papers](https://scholar.google.it/scholar?q=%28+MicroGP+OR+%C2%B5GP+%29+AND+%28+Squillero+OR+Tonda+%29) reporting possible applications can be found in the scientific literature.

* MicroGP4 is available as a [PyPi package](https://en.wikipedia.org/wiki/Python_Package_Index) and using it is as simple as  
[`pip install microgp`](https://pypi.org/project/microgp/) 
* The user guide and API reference are hosted on [Read the Docs](https://en.wikipedia.org/wiki/Read_the_Docs) at [https://microgp4.readthedocs.io/](https://microgp4.readthedocs.io/)

The project [started around the year 2000](history.html), with the creation of a collection of scripts for optimizing assembly-language programs. A fully working version was coded in C in 2002, and then re-engineered in C++ in 2006; the design of a Python version started in 2018. MicroGP4 would not have been possible without the help and support of [several people](contributors.html).

MicroGP4 is [free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software) and it is distributed under the permissive [Apache License 2.0](https://www.tldrlegal.com/l/apache2).

