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


class NodeID(int):
    """A node in the directed MultiGraph describing the individual. It is, a
    positive integer used as unique id in the MultiDiGraph.
    """
    _LAST_ID = 0  # global counter of nodes

    def __init__(self):
        self._canonical = int(self)

    def __new__(cls):
        NodeID._LAST_ID += 1
        return super(NodeID, cls).__new__(cls, NodeID._LAST_ID)

    def __str__(self):
        return "n%d" % (self._canonical,)

    # Overriding __repr__ is necessary as we inherited from int but we do not
    # want repr(Node()) to look like an int (eg. '42')...
    def __repr__(self):
        return str(self)

    def run_paranoia_checks(self) -> bool:
        assert self > 0, "Illegal node id: %d" % (self,)
        return True
