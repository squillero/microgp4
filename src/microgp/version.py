# -*- coding: utf-8 -*-
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0.a1 "Kiwi"  #
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

# Version History (see HISTORY.md)
#
# MicroGP v2: Copyright © 2002-2006 Giovanni Squillero
#   Licensed under GPL2
# MicroGP v3: Copyright © 2006-2016 Giovanni Squillero
#   Licensed under GPL3
# MicroGP v4: Copyright © 2019 Giovanni Squillero and Alberto Tonda
#   Licensed under Apache-2.0

from collections import namedtuple

VersionInfo = namedtuple('VersionInfo', ['epoch', 'major', 'minor', 'tag', 'micro', 'codename'])
version_info = VersionInfo(4, 1, 0, 'a', 4, 'Kiwi')
