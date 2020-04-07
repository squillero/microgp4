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

from typing import Optional
from microgp.abstract import Pedantic
import warnings


class NodeID(int, Pedantic):
    """A node in the directed MultiDiGraph describing the individual.

    Use `n = NodeID()` to get a unique id.

    Use `n = NodeID(int)` to get a specific node id. This is deprecated as it could only be useful during debug.
    """

    _LAST_ID = 0  # global counter of nodes

    def __init__(self, value: Optional[int] = None) -> None:
        pass

    def __new__(cls, value: Optional[int] = None) -> None:
        if value is None:
            NodeID._LAST_ID += 1
            value = NodeID._LAST_ID
        else:
            value = int(value)
            warnings.warn("Cast from integer to NodeID is deprecated", DeprecationWarning, stacklevel=2)
        return super(NodeID, cls).__new__(cls, value)

    def __hash__(self):
        return int(self)

    def __eq__(self, other) -> bool:
        if not isinstance(other, NodeID):
            return False
        return int(self) == int(other)

    def __str__(self) -> str:
        return f"n{int(self)}"

    # Overriding __repr__ is necessary as we inherited from int but we do not
    # want repr(Node()) to look like an int (eg. '42')...
    def __repr__(self) -> str:
        return str(self)

    def run_paranoia_checks(self) -> bool:
        assert int(self) > 0, f"Illegal node id: {int(self)}"
        return True
