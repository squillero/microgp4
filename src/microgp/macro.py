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

import copy
from string import Formatter
from typing import Type, Dict
import warnings

from .abstract import Paranoid
from .parameter import Structural
from .parameter.base import Parameter
from .parameter.special import Information
from .properties import Properties


class Macro(Paranoid):
    """The blueprint of macro.

    A "macro" is a fragment of text with zero or more variable parameters. it
    is the building block of a solution. A macro is associated with the node
    in the DAG encoding the individual.

    Notes:
        Attributes are read-only and can only be set when the macro is created.
        Some parameters are by default available to all macros, the list is in
        Macro.MAGIC_PARAMETERS
    """
    MAGIC_PARAMETERS = ['info']

    def __init__(self, text: str, parameters_type: dict = None):
        """Macro builder

        Args:
            text: the constant part of the macro
            parameters_type: a dictionary containing the names of the
             parameters and their types (classes, not objects)
        """
        if parameters_type is None:
            parameters_type = dict()
        assert isinstance(parameters_type, dict), "Parameters type must be a dictionary"
        assert all([p not in Macro.MAGIC_PARAMETERS for p in parameters_type]), "Parameter name is reserved"
        assert all([p[:1] != '$' for p in parameters_type]), "Parameter name can't start with '$'"
        # magic parameters
        parameters_type['info'] = Information
        # sanity check
        assert all([p is None or p in parameters_type for _, p, _, _ in Formatter().parse(text)
                   ]), "A parameter in macro's text is missing from the dictionary of parameters' types"

        self._text = text
        self._parameters_type = parameters_type
        self._properties = Properties()

    @property
    def properties(self) -> Properties:
        return self._properties

    @property
    def parameters_type(self) -> Dict[str, Type[Parameter]]:
        return dict(self._parameters_type)

    @property
    def text(self) -> str:
        return self._text

    def add_parameter(self, name: str, parameter_type: Parameter) -> None:
        """Add parameters to the macro

        Args:
            name: name of the parameter
            parameter_type: type of the parameter
        """

        warnings.warn("add_parameter is deprecated. Parametrs should be set on creation.", DeprecationWarning)
        assert isinstance(name, str), "Name must be a string"
        assert isinstance(parameter_type, type), "Parameter type should be a 'type' (d'ho!?)"
        assert isinstance(parameter_type(), Parameter), "Parameter type must be of type 'Parameter' (d'ho!?)"
        assert name not in Macro.MAGIC_PARAMETERS, "Parameter '" + name + "' is reserved for internal use"
        self._parameters_type[name] = parameter_type

    def run_paranoia_checks(self) -> None:
        for name, parameter_type in self._parameters_type.elem():
            assert isinstance(name, str), "Name must be a string"
            assert isinstance(parameter_type, type), "Parameter type should be a 'type' (d'ho!?)"
            assert isinstance(parameter_type(), Parameter), "Parameter type must be of type 'Parameter' (d'ho!?)"
            assert name not in Macro.MAGIC_PARAMETERS, "Parameter '" + name + "' is reserved for internal use"

    def describe(self) -> str:
        desc = "%r" % (self._text,)
        desc = desc.replace(" ", "")
        if len(desc) > 20:
            desc = desc[:20 - 4] + "...'"
        return desc

    def __str__(self):
        params = ", ".join([n + "=" + t.__name__ for n, t in self._parameters_type.items()])
        return "%r %% (%s)" % (self._text.strip(), params)

    def __or__(self, other):
        from .constraints import MacroPool
        return MacroPool([self, other])

    def __add__(self, other):
        from .constraints import MacroPool, SubsectionsSequence
        return SubsectionsSequence([MacroPool([self]), MacroPool([other])])
