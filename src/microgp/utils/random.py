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

# MicroGP's own random generator.

import random as py_random
from . import logging

class MicroGP_Random():
    def __init__(self):
        self._py_random = py_random.Random()
        self._calls = 0
        self.seed(42)
        logging.info("Initialized random generator")

    def seed(self, *args, **kwargs):
        self._calls = 0
        return self._py_random.seed(*args, **kwargs)

    def randint(self, *args, **kwargs):
        old = f"{self}"
        self._calls += 1
        value = self._py_random.randint(*args, **kwargs)
        new = f"{self}"
        logging.debug(f"randint : {old} -> {new}")
        return value

    def random(self, *args, **kwargs):
        old = f"{self}"
        self._calls += 1
        value = self._py_random.random(*args, **kwargs)
        new = f"{self}"
        logging.debug(f"random : {old} -> {new}")
        return value

    def shuffle(self, *args, **kwargs):
        old = f"{self}"
        self._calls += 1
        value = self._py_random.shuffle(*args, **kwargs)
        new = f"{self}"
        logging.debug(f"shuffle : {old} -> {new}")
        return value

    def choice(self, *args, **kwargs):
        old = f"{self}"
        self._calls += 1
        value = self._py_random.choice(*args, **kwargs)
        new = f"{self}"
        logging.debug(f"choice : {old} -> {new}")
        return value

    def choices(self, *args, **kwargs):
        old = f"{self}"
        self._calls += 1
        value = self._py_random.choices(*args, **kwargs)
        new = f"{self}"
        logging.debug(f"choices : {old} -> {new}")
        return value

    def __str__(self):
        random_state = hex(abs(hash(self._py_random.getstate())))
        return f"{self._calls}:0x{random_state}"

random_generator = MicroGP_Random()
