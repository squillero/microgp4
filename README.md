[MicroGP4](https://squillero.github.io/microgp4/)
==========

[![License: Apache 2.0](https://img.shields.io/badge/license-apache--2.0-green.svg)](https://opensource.org/licenses/Apache-2.0) 
[![Status: Actrive](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/squillero/microgp3)
![Language: Python](https://img.shields.io/badge/language-python-blue.svg)
![Version: 4!1.0α](https://img.shields.io/badge/version-4!1.0α-orange.svg)
![Codename: kiwi](https://img.shields.io/badge/codename-kiwi-orange.svg)
[![Documentation Status](https://readthedocs.org/projects/microgp4/badge/?version=pre-alpha)](https://microgp4.readthedocs.io/en/pre-alpha/?badge=pre-alpha)
![](https://www.google-analytics.com/collect?v=1&t=pageview&tid=UA-28094298-6&cid=4f34399f-f437-4f67-9390-61c649f9b8b2&dp=1)

> :warning: MicroGP4 v1.0 is currently in [pre-alpha](https://en.wikipedia.org/wiki/Software_release_life_cycle#Pre-alpha) and under active development.

MicroGP (µGP, ``ugp``) is an evolutionary optimizer able to outperform both human experts and conventional heuristics in finding good solution of hard problems. It first creates a set of random solutions, then iteratively refines and enhances them using the result of their evaluations together with structural information. Different techniques are used to explore efficiently the search space.

#### Installation

MicroGP4 is on PyPi ([project/microgp](https://pypi.org/project/microgp/)) and can be installed using [`pip`](https://en.wikipedia.org/wiki/Pip_Pip_%28package_manager%29): 

```shell script
pip install coloredlogs matplotlib psutil   # optional
pip install microgp
```

The packages [`coloredlogs`](https://pypi.org/project/coloredlogs/), [`matplotlib`](https://pypi.org/project/matplotlib/) and [`psutil`](https://pypi.org/project/psutil/) are optional as they are exploited only if present.

#### Documentation

* The documentation for MicroGP4 is on https://microgp4.readthedocs.io/
* The documentation for MicroGP3 (v3.1 *"Bluebell"*), together with the old design rationale, can be found in the book *Evolutionary Optimization: the µGP toolkit*, Springer Science & Business Media (2011), [10.1007/978-0-387-09426-7](https://www.doi.org/10.1007/978-0-387-09426-7)
* MicroGP2 is described in the paper "MicroGP — An Evolutionary Assembly Program Generator", *Genetic Programming and Evolvable Machines*,  vol. 6, 247–263 (2005), [10.1007/s10710-005-2985-x](http://dx.doi.org/10.1007/s10710-005-2985-x)
* MicroGP1 (i.e., an unnamed evolutionary tool able to generate real assembly programs), has been presented in the paper "Efficient machine-code test-program induction", *Proceedings of the 2002 Congress on Evolutionary Computation*, 2002, [10.1109/CEC.2002.1004462](http://dx.doi.org/10.1109/CEC.2002.1004462)

### Contacts

* [Giovanni Squillero](https://github.com/squillero) [:email:](mailto:squillero@polito.it) [:house:](https://staff.polito.it/giovanni.squillero/)
* [Alberto Tonda](https://github.com/albertotonda/)  [:email:](mailto:alberto.tonda@inra.fr) [:house:](https://www.researchgate.net/profile/Alberto_Tonda)

### Acknowledgements

MicroGP would not have been possible without the help and support of [several people](https://squillero.github.io/microgp4/contributors.html). 

### Licence
Copyright © 2020 Giovanni Squillero and Alberto Tonda  
MicroGP4 is [free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software), and it is distributed under the permissive [Apache License 2.0](https://www.tldrlegal.com/l/apache2).
