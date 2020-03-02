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

# Copyright 2019 Giovanni Squillero and Alberto Tonda
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

from typing import Tuple, Callable

from .macro import Macro


def check_frame_size(size: Tuple[int, int]) -> Callable:
    def check_size(nodes, sub_sections, **v):
        assert isinstance(nodes, list), "nodes list is not a list but a '%s'" % (type(nodes),)
        assert isinstance(sub_sections, list), "sub_sections list is not a list but a '%s'" % (type(sub_sections),)
        assert not (nodes and
                    sub_sections), "A section cannot hold both nodes and sub_sections: %s vs. %s" % (nodes,
                                                                                                     sub_sections)
        if len(nodes) + len(sub_sections) < size[0]:
            return False
        if len(nodes) + len(sub_sections) > size[1]:
            return False
        return True

    return check_size


def check_macro_count(macro: Macro, size: Tuple[int, int]):
    pass
