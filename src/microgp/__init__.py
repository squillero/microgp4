# -*- coding: utf-8 -*-
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0a1 "Kiwi"   #
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

"""MicroGP 4!1.0α "Kiwi" <https://github.com/squillero/microgp4>

A versatile optimizer able to outperform both human experts and conventional
heuristics in finding the optimal solution of difficult problems.

Copyright © 2020 Giovanni Squillero and Alberto Tonda.
Distributed under Apache-2.0.
"""

import sys
import warnings

from .version import version_info
from .utils import logging
from .parameter import make_parameter
from .macro import Macro
from .constraints import make_section, Constraints, Section
from .darwin import Darwin
from .operators import Operators
from .genoperator import GenOperator
from .properties import Properties
from .individual import Individual
from .individual_operators import flat_mutation, hierarchical_mutation, add_node_mutation, remove_node_mutation, \
    print_individual, macro_pool_uniform_crossover, macro_pool_one_cut_point_crossover, switch_proc_crossover, \
    create_random_individual
from . import fitness

# Standard messages
WARN_V27 = "The code is quite probably not compatible with Python v2"
WARN_V37 = "The code is only known to be compatible with Python v3.7+"
WARN_DBG = "Paranoia checks are active: performances can be significantly impaired (consider using '-O')"

if sys.version_info < (3,):
    warnings.warn(WARN_V27, Warning)
elif sys.version_info < (3, 7):
    warnings.warn(WARN_V37, Warning)

if sys.flags.optimize == 0:
    warnings.warn(WARN_DBG, UserWarning)


def banner() -> None:
    """Shows the "official" MicroGP banner"""
    logging.bare(
        f"This is MicroGP{version_info.epoch} v{version_info.major}.{version_info.minor}{version_info.tag}{version_info.micro} \"{version_info.codename}\""
    )
    logging.bare(f"(c) 2020 by Giovanni Squillero and Alberto Tonda")


name = "microgp"
__name__ = name
__version__ = f"{version_info.epoch}!{version_info.major}.{version_info.minor}{version_info.tag}{version_info.micro}"
