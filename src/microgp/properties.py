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

import inspect
import sys
from typing import Dict, Set, Callable, Union

from .utils import logging


class Properties:
    """Updates a dictionary of `values` and runs `checks` against them.

    Properties are used to check if a frame (ie. the portion of the individual
    implementing a given section) is valid. First, all functions registered as
    `values builders` are called, then all functions registered as `check` are
    evaluated; if all succeeded, then True is turned.

    `Values` are divided in `custom` and `base`. User's builders build custom
    ones. Values can be retrieved through property `values` that merge the
    two, alternatively they can be retrieved through properties `base_values`
    and `custom_values`.

    `Values builders` are functions returning a dictionary of values
    `{'value_name': value}` that is added to the current value-bag. Values
    cannot be shadowed.

    `Checks` are called when the value bag is complete and get getting all
    values as parameters, i.e. `check(**values)`

    **Examples**: create two cumulative (custom) builders and add a checker that test that two sections have the same number of nodes

    >>> sec2a.properties.add_cumulative_builder(lambda num_nodes, **v: {'sec2a': num_nodes})
    >>> sec2b.properties.add_cumulative_builder(lambda **v: {'sec2b': v['num_nodes']})
    >>> library.global_properties.add_check(lambda sec2a, sec2b, **v: sec2a == sec2b)
    """

    def __init__(self):
        """Properties builder"""
        self._cumulative_values = dict()
        self._base_values = dict()
        self._cumulative_builders = set()
        self._base_builders = set()
        self._checkers = set()
        if sys.flags.optimize == 0:
            # hook run_check to a slower, verbose version
            self.run_checks = self._run_checks_debug

    @property
    def values(self) -> Dict:
        """Read-only dictionary of all values (both custom and base)"""
        return dict(**self._base_values, **self._cumulative_values)

    @property
    def cumulative_values(self) -> Dict:
        """Read-only dictionary of custom values"""
        return dict(self._cumulative_values)

    @property
    def base_values(self) -> Dict:
        """Read-only dictionary of base values"""
        return dict(self._base_values)

    @property
    def checkers(self) -> Set[Callable]:
        return self._checkers

    @property
    def cumulative_builders(self) -> Set[Callable]:
        return self._cumulative_builders

    @property
    def base_builders(self) -> Set[Callable]:
        return self._base_builders

    def update(self, properties: 'Properties'):
        self._base_builders.update(properties._base_builders)
        self._cumulative_builders.update(properties._cumulative_builders)
        # self._checkers.update(properties._checkers)
        for c in properties._checkers:
            self.add_checker(c)
        assert all(inspect.Parameter.VAR_KEYWORD in (p.kind
                                                     for p in inspect.signature(c).parameters.values())
                   for c in self._checkers), "Missing **values from a checker signature"

    def __bool__(self):
        return bool(self._base_builders) or bool(self._cumulative_builders) or bool(self._checkers)

    def __str__(self) -> str:
        s = "%r" % (self,)
        s = "\nBase builders: %d / Cumulative builders: %d" % (len(self._base_builders), len(self._cumulative_builders))
        s += "\nBASE VALUES:\n\t" + "\n\t".join([f"{k}: {v}" for k, v in self._base_values.items()])
        if self._cumulative_values:
            s += "\nCUMULATIVE VALUES:\n\t" + "\n\t".join([f"{k}: {v}" for k, v in self._cumulative_values.items()])
        s += "\nCHECKERS (%d):" % (len(self.checkers),)
        for f in self.checkers:
            s += "\n\t" + inspect.getsource(f).strip()
        return s

    def add_cumulative_builder(self, new_properties_builder: Callable[..., Dict]) -> None:
        self._cumulative_builders.add(new_properties_builder)

    def add_base_builder(self, new_properties_builder: Callable[..., Dict]) -> None:
        self._base_builders.add(new_properties_builder)

    def add_checker(self, new_checker: Callable) -> None:
        assert inspect.Parameter.VAR_KEYWORD in (
            p.kind for p in inspect.signature(new_checker).parameters.values()
        ), "Missing **values from method's signature: checker%s" % (inspect.signature(new_checker),)
        self._checkers.add(new_checker)

    def update_values(self, cumulative_values: Union[dict, None] = None, **kwargs):
        """Runs properties builders and collect the results into `values` dictionary."""

        # base builders
        self._base_values = dict()
        for f in self._base_builders:
            for k, v in f(**kwargs).items():
                assert isinstance(
                    f(**kwargs),
                    dict), "Base builder <%s> does not return a dictionary but %s" % (inspect.getsource(f).strip(),
                                                                                      type(f(**kwargs)))
                assert k not in self._base_values, f"Duplicate property value '{k}'"
                self._base_values[k] = v

        # cumulative builders
        if cumulative_values:
            assert all(k not in self._base_values
                       for k in cumulative_values.keys()), f"Cumulative value '{k}' would shadow a base builder"
            self._cumulative_values = dict(cumulative_values)
        else:
            self._cumulative_values = dict()
        # logging.debug("self._cumulative_values: %s" % (self._cumulative_values,))

        kwargs = {**kwargs, **self._base_values}
        for f in self._cumulative_builders:
            assert isinstance(
                f(**kwargs),
                dict), "Cumulative builder <%s> does not return a dictionary but %s" % (inspect.getsource(f).strip(),
                                                                                        type(f(**kwargs)))
            for k, v in f(**kwargs).items():
                assert k not in self._base_values, f"Cumulative value '{k}' would shadow a base builder"
                if k not in self._cumulative_values:
                    # logging.debug("%s: %s" % (k, v))
                    self._cumulative_values[k] = v
                else:
                    # logging.debug("(merge offspring) %s: %s + %s -> %s" % (k, self._cumulative_values[k], v, self._cumulative_values[k] + v))
                    self._cumulative_values[k] = self._cumulative_values[k] + v

    def run_checks(self):
        """Runs all checks against current values; returns True if all succeed."""
        values = {**self.values}
        try:
            return all(f(**values) for f in self._checkers)
        except Exception as e:
            logging.error("run_checks failed: %s" % (e,))
            exit(10)

    def _run_checks_debug(self):
        import inspect
        values = {**self.values}
        for f in self._checkers:
            if not f(**values):
                logging.debug("FAILED CHECK: %s", inspect.getsource(f).strip())
                logging.debug("> parameters: %s", values)
                return False
        return True

    def __deepcopy__(self, memo):
        return self
