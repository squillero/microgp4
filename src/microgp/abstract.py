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

"""Can you help me occupy my brain? Oh yeah."""

from typing import Any


class Paranoid:
    """Abstract class: Paranoid classes do implement `run_paranoia_checks()`."""

    def run_paranoia_checks(self) -> bool:
        """Checks the internal consistency of a "paranoid" object.

        The function should be overridden by the sub-classes to implement the
        required, specific checks. It always returns `True`, but throws an
        exception whenever an inconsistency is detected.

        **Notez bien**: Sanity checks may be computationally intensive,
        paranoia checks are not supposed to be used in production environments
        (i.e., when `-O` is used for compiling). Their typical usage is:
        `assert foo.run_paranoia_checks()`

        Returns:
            True (always)

        Raise:
            AssertionError if some internal data structure is incoherent
        """
        raise NotImplementedError


class Pedantic:
    """Abstract class: Pedantic classes do implement `is_valid()`."""

    def is_valid(self, obj: Any) -> bool:
        """Checks an object against a specification. The function may be used
        to check a value against a parameter definition, a node against a
        section definition).

        Returns:
            True if the object is valid, False otherwise
        """
        raise NotImplementedError


def sabbath(condition: bool) -> bool:
    assert condition, "Sabbath check fail: Can you help me occupy my brain?"
    return True
