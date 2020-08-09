# -*- coding: utf-8 -*-
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0 "Kiwi"     #
#  / / / / / __/ /_/ / // /   (!) by Giovanni Squillero and Alberto Tonda   #
# / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         #
# \__  /\____/_/   /__  __/                                                 #
#   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!!" #
#                                                                           #
#############################################################################

# Copyright 2020 Giovanni Squillero and Alberto Tonda
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

"""MicroGP 4!1.0α "Kiwi" <https://squillero.github.io/microgp4/>

A versatile evolutionary optimizer able to outperform both human experts and
conventional heuristics in finding the optimal solution of difficult problems.

Copyright © 2020 Giovanni Squillero and Alberto Tonda.
Distributed under Apache-2.0.
"""

import sys
import os
import warnings
from collections import namedtuple

VersionInfo = namedtuple('VersionInfo', ['epoch', 'major', 'minor', 'tag', 'micro', 'codename', 'dev'])
version_info = VersionInfo(4, 1, 0, 'a', 0, 'Kiwi', 24)

# hard code
__name__ = "microgp"
__version__ = f"{version_info.epoch}!{version_info.major}.{version_info.minor}{version_info.tag}{version_info.micro}.dev{version_info.dev}"
__author__ = "Giovanni Squillero and Alberto Tonda"
__copyright__ = """Copyright (c) 2002-2006 Giovanni Squillero.
All Rights Reserved. Licensed under GPL2.

Copyright (c) 2006-2016 Giovanni Squillero.
All Rights Reserved. Licensed under GPL3.

Copyright (c) 2020 Giovanni Squillero and Alberto Tonda.
All Rights Reserved. Licensed under Apache-2.0.
"""

##############################################################################
# Almost human-readable infos

name = f"MicroGP{version_info.epoch}"
if version_info.tag == "a" and version_info.micro == 0:
    version = f"v{version_info.major}.{version_info.minor}_{version_info.dev} pre-alpha \"{version_info.codename}\""
elif version_info.tag == "a" and version_info.micro > 0:
    version = f"v{version_info.major}.{version_info.minor}α{version_info.micro}_{version_info.dev} \"{version_info.codename}\""
elif version_info.tag == "b" and version_info.micro > 0:
    version = f"v{version_info.major}.{version_info.minor}β{version_info.micro}_{version_info.dev} \"{version_info.codename}\""
elif version_info.tag == "rc" and version_info.micro > 0:
    version = f"v{version_info.major}.{version_info.minor}rc{version_info.micro}_{version_info.dev} \"{version_info.codename}\""
elif version_info.tag == "":
    version = f"v{version_info.major}.{version_info.minor}.{version_info.micro}_{version_info.dev} \"{version_info.codename}\""
else:
    version = "unknown"
author = __author__

##############################################################################
# Standard warnings
if sys.version_info < (3,):
    warnings.warn("The code is quite probably not compatible with Python 2", Warning, stacklevel=2)
elif sys.version_info < (3,7):
    warnings.warn("The code has never been tested with Python prior to v3.7", Warning, stacklevel=2)
if sys.version_info < (3, 7):
    warnings.warn(
        "Dictionary order is not guaranteed to be insertion order: Results are likely to be not reproducible",
        Warning,
        stacklevel=2)

##############################################################################
# MicroGP stuff
from .utils import logging, random_generator
from .parameter import make_parameter
from .macro import Macro
from .constraints import make_section, Constraints, Section
from .darwin import Darwin
from .operators import Operators
from .genoperator import GenOperator
from .properties import Properties
from .individual import Individual
from .genetic_operators import flat_mutation, hierarchical_mutation, add_node_mutation, remove_node_mutation, \
    print_individual, macro_pool_uniform_crossover, macro_pool_one_cut_point_crossover, switch_proc_crossover, \
    create_random_individual
from . import fitness


##############################################################################
# Helpers
def show_banner() -> None:
    """Shows the "official" MicroGP banner"""
    sys.stderr.flush()
    logging.bare(f"This is {name} {version}")
    logging.bare("Copyright © 2020 by Giovanni Squillero and Alberto Tonda")
    sys.stderr.flush()

def copyright():
    """Lists contributors and copyright notices."""
    sys.stderr.flush()
    logging.bare(__copyright__)
    sys.stderr.flush()

##############################################################################
# Welcome!

#show_banner()

if sys.flags.optimize == 0:
    warnings.warn("Paranoia checks are active; performances can be significantly impaired (consider using '-O')",
                  UserWarning,
                  stacklevel=2)

if version_info.tag == 'a' and not sys.warnoptions and 'PYTHONWARNINGS' not in os.environ:
    warnings.filterwarnings('default', category=DeprecationWarning, module='microgp')
    warnings.warn("Showing all Deprecation Warnings (tweak with '-W' or PYTHONWARNINGS)", UserWarning, stacklevel=2)
    # hint: try using "-W error:microgp:DeprecationWarning"
