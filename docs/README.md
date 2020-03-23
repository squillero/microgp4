MicroGP is an evolutionary optimizer able to outperform both human experts and conventional heuristics in finding good solution of hard problems. It first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information. Different techniques --- some inspired by the mechanisms of natural evolution --- are used to explore efficiently the search space.

MicroGP is extremely versatile: it is able to tackle problem those solutions are simple fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines; candidate solutions can be evaluated using independent, proprietary external tools.  The first prototype was created around 2000, a fully working version was coded in C in 2002 and then re-engineered in C++ in 2006. MicroGP4 is in Python, redesigned from scratch to take advantage of the peculiar features of the language and to exploit its huge standard library. 

The latest version is available as a [PyPi package](https://pypi.org/project/microgp/):

```shell script
$ pip install microgp
```

### Documentation

* The documentation for MicroGP4 is available from [https://microgp4.readthedocs.io/](https://microgp4.readthedocs.io/)
* The documentation for MicroGP3 (v3.1 "Bluebell"), together with the old design rationale, can be found in the book Evolutionary Optimization: the µGP toolkit, Springer Science & Business Media (2011), [10.1007/978-0-387-09426-7](https://www.doi.org/10.1007/978-0-387-09426-7)
* MicroGP2 is described in the paper "MicroGP — An Evolutionary Assembly Program Generator", Genetic Programming and Evolvable Machines, vol. 6, 247–263 (2005), [10.1007/s10710-005-2985-x](http://dx.doi.org/10.1007/s10710-005-2985-x)
* MicroGP1 (i.e., an unnamed evolutionary tool able to generate real assembly programs), has been presented in the paper "Efficient machine-code test-program induction", Proceedings of the 2002 Congress on Evolutionary Computation, 2002, [10.1109/CEC.2002.1004462](http://dx.doi.org/10.1109/CEC.2002.1004462)

###### MicroGP4 is [free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software) and it is distributed under the permissive [Apache License 2.0](https://www.tldrlegal.com/l/apache2)

