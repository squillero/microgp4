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

import warnings
from typing import Type, Any
from collections import Iterable
import scipy.stats as stats
import microgp as ugp
from .base import Parameter
from microgp import random_generator

WARN_DEPR_ACTIVE = "sigma_choice() is deprecated and should be replaced with microgp.random_generator.choice"


def make_parameter(base_class: Type[Parameter], **attributes: Any) -> Type:
    """Binds a Base parameter class, fixing some of its internal attributes.

    Args:
        base_class (Parameter): Base class for binding parameter.
        **attributes (dict): Attributes.

    Returns:
        Bound parameter.

    **Examples:**

        >>> register = ugp.make_parameter(ugp.parameter.Categorical, alternatives=['ax', 'bx', 'cx', 'dx'])
        >>> int8 = ugp.make_parameter(ugp.parameter.Integer, min_=-128, max_=128)
        >>> p1, p2 = register(), int8()
    """
    signature = ", ".join([str(k) + "=" + str(v) for k, v in attributes.items()])
    return type("{}({})".format(base_class.__name__, signature), (base_class,), attributes)


def sigma_choice(seq, previous_index=None, sigma=None):
    warnings.warn(WARN_DEPR_ACTIVE, DeprecationWarning, stacklevel=2)
    assert previous_index < len(seq), 'Previous index out of range'
    assert 0 < sigma < 1, 'Sigma must be 0 < sigma < 1'

    if isinstance(seq, range):
        # seq is range!
        print(type(seq))
        print(seq)
        return 42
        #exit(0)
    elif isinstance(seq, Iterable):
        # sequence is iterable
        print(type(seq))
        print(seq)
        exit(0)
        # seq is a list
        # original_sigma = sigma
        mean = previous_index
        # sigma = - math.log(sigma, 1.4)
        sigma = (10**(sigma**2))
        x = range(len(seq))
        probs = stats.norm.pdf(x, mean, sigma)
        probs += probs[previous_index]
        assert sum(probs) > 0, f"Some probabilities must be non-zero: seq={seq} probs={probs}"
        probs = probs / sum(probs)
        weights = probs
        weights[previous_index] = 0
        return random_generator.choices(seq, weights, k=1)[0]
    else:
        assert not isinstance(seq, range) and not isinstance(seq, Iterable), \
            "Seq must be either a range or an iterable collection"

    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # # ax.plot(x, probs, color='tab:blue')
    # ax.plot(x, weights, color='tab:orange')
    # plt.title("Sigma = " + str(original_sigma) + ", new_sigma = " + str(sigma))
    # plt.show()

    # print(sum(weights))
    # return rnd.choices(seq, weights, k=1)[0]
