# -*- coding: utf-8 -*-
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0a1 "Kiwi"   #
#  / / / / / __/ /_/ / // /   A versatile evolutionary optimizer & fuzzer   #
# / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         #
# \__  /\____/_/   /__  __/                                                 #
#   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!"  #
#                                                                           #
#############################################################################

# Copyright 2020-2021 Giovanni Squillero and Alberto Tonda
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

import os
from datetime import datetime

from .. import version_info
from .abstract import Special
from ..node import NodeID
from ..utils import microgp4_process_time


class Information(Special):
    """This is a dummy Parameter whose purpose is to insert information about
    the state of the system into the individual. The available information are
    provided through the ``__format__`` method:

    - **ugp4**: provides textual information about MicroGP version number and version name;

    - **version**: provides information about the package version number;

    - **node**: provides the NodeID of the node that contains the Information Parameter;

    - **time** or **now**: provides date and time;

    - **cpu_time**: provides the time spent running;

    - **pid**: provides the Process ID (PID);

    - **path**: provides the path in the frame tree of the node that contains the Information Parameter;

    - **cwd**: provides the current working directory.
    """

    VALID_INFO = sorted(['node', 'thread_time', 'now', 'path', 'cwd', 'pid', 'version', 'ugp4'])

    def __str__(self):
        return f"{self}"

    def __format__(self, format_spec: str):
        assert format_spec in Information.VALID_INFO + [''], "Requested information '%s' not in %s" % (
            format_spec, Information.VALID_INFO)
        if not format_spec or format_spec == 'ugp4':
            return f"MicroGP v{version_info.epoch}.{version_info.major}.{version_info.minor}.{version_info.tag}{version_info.micro} \"{version_info.codename}\""
        elif format_spec == 'version':
            return f"{version_info.epoch}.{version_info.major}.{version_info.minor}.{version_info.tag}{version_info.micro}"
        elif format_spec == 'node':
            return str(self.node)
        elif format_spec == 'time' or format_spec == 'now':
            return str(datetime.now())
        elif format_spec == 'cpu_time':
            return str(microgp4_process_time)
        elif format_spec == 'pid':
            return str(os.getpid())
        elif format_spec == 'path':
            return self._individual.get_node_fullpath(self._node)
        elif format_spec == 'cwd':
            return os.getcwd()
        else:
            raise NameError
