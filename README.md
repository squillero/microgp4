MicroGP v4
==========

[![License: Apache 2.0](https://img.shields.io/badge/license-apache--2.0-green.svg)](https://opensource.org/licenses/Apache-2.0) 
[![Status: Actrive](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/squillero/microgp3)
![Language: Python](https://img.shields.io/badge/language-python-blue.svg)
![Version: 4.0.0β](https://img.shields.io/badge/version-4.0.0--beta-orange.svg)
![Codename: Kiwi](https://img.shields.io/badge/codename-Kiwi-orange.svg)

MicroGP (µGP, `&micro;GP`) is an evolutionary optimizer able to outperform both human experts and conventional heuristics in finding the optimal solution of generic problems. It is extremely versatile, being able to tackle problem those solutions are fixed-length bit strings, as well as to optimize realistic assembly programs including loops, interrupts and recursive sub routines.

MicroGP first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information; [several different techniques](https://scholar.google.com/scholar?q=%28+squillero+OR+tonda+%29+AND+microgp) are used to explore efficiently the search space, and eventually pinpoint the best solution. The project started [around Y2K](HISTORY.md) and benefited of the effort of [several people](CONTRIBUTORS.md). MicroGP has been first [coded in C in 2002](https://github.com/squillero/microgp2) and then [re-engineered in C++ in 2006](https://github.com/squillero/microgp3). This version is in Python, it has been redesigned from scratch once again to take advantage of the peculiar features of the language and to exploit its huge standard library. 

**Copyright © 2019 Giovanni Squillero and Alberto Tonda**  
MicroGP v4 is [free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software), and it is distributed under the permissive [Apache-2.0 license](https://tldrlegal.com/license/apache-license-2.0-%28apache-2.0%29).
