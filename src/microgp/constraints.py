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

from typing import Any, Collection, Sequence, Set, List, Tuple, Dict, Callable, Optional
from itertools import combinations
from collections import Counter

from .abstract import Paranoid, Pedantic
from .macro import Macro
from .properties import Properties
from .fitness.base import Base
from . import default_builders, standard_checkers


class Section(Paranoid):
    """Base structural unit. A section can be composed by one or more macros,
    a set or a list of other subsections. See :mod:`microgp.constraints.make_section`."""

    _COUNTER = Counter()

    @staticmethod
    def anonymous(tag: str = 'x') -> str:
        Section._COUNTER[tag] += 1
        return "%s%d" % (tag, Section._COUNTER[tag])

    def __init__(self, name: str, instances: Optional[Tuple[int, int]] = None, label_format=None) -> None:
        assert name, "Invalid section name: '%s'" % (name,)
        self._name = name
        self._checkers = list()
        self.instances = instances  # using property to check
        self._properties = Properties()
        self._properties.add_base_builder(default_builders.default_base_builder)
        self._properties.add_cumulative_builder(default_builders.default_cumulative_builder)
        self._label_format = label_format

    @property
    def label_format(self) -> str:
        return self._label_format

    @label_format.setter
    def label_format(self, new_format: str) -> None:
        self._label_format = new_format

    @property
    def name(self) -> str:
        return self._name

    @property
    def properties(self) -> Properties:
        return self._properties

    @property
    def sub_sections(self) -> List['Section']:
        raise NotImplementedError

    @property
    def macros(self) -> List[Macro]:
        raise NotImplementedError

    @property
    def instances(self) -> Optional[Tuple[int, int]]:
        return self._instances

    @instances.setter
    def instances(self, new_val: Optional[Tuple[int, int]]) -> None:
        if new_val is not None:
            assert len(new_val) == 2, "instances should be a tuple(min, max)"
            assert isinstance(new_val[0], int) and new_val[0] >= 0, "min instances should be an integer >= 0"
            assert isinstance(new_val[1], int) and new_val[1] >= new_val[0], \
                "max instances should be an integer > min instances"
        self._instances = new_val

    def __str__(self):
        return "%s:???" % (self._name,)

    def run_paranoia_checks(self) -> bool:
        assert hasattr(self, "_name"), "Missing required attribute"
        assert hasattr(self, "_instances"), "Missing required attribute"
        return True

    def make_default_checkers(self):
        """Make the list of default checkers, based on section properties"""

        checkers = set()
        # logging.debug(f"Adding instance check: {self.instances} ({self.name})")
        # checkers.add(lambda **values: values['num_frames_same_section'] >= self.instances[0])
        # checkers.add(lambda **values: values['num_frames_same_section'] <= self.instances[1])
        # The following check is only added in debug mode
        # assert checkers.add(lambda **values: sabbath(values['num_nodes'] == 0 or values['num_subframes'] == 0)) or True, "PANIC: This should never fail..."
        if hasattr(self, "size"):
            checkers.add(standard_checkers.check_frame_size(self.size))
        return checkers


class RootSection(Section):
    """The ROOT section of an individual. Each individual have one and only
    one root section."""

    def __init__(self) -> None:
        super().__init__('<ROOT>')


class SubsectionsSequence(Section):
    """A sequence of subsections. This class contains a tuple of sub sections
    """

    def __init__(self, sub_sections: Sequence[Section] = None, name: str = None, **kwargs) -> None:
        if not name:
            name = Section.anonymous('ss')
        super().__init__(name, **kwargs)
        self.sub_sections = sub_sections

    @property
    def sub_sections(self) -> List[Section]:
        if self._sub_sections:
            return list(self._sub_sections)
        else:
            return list()

    @sub_sections.setter
    def sub_sections(self, new_sequence: Sequence[Section]) -> None:
        if new_sequence:
            self._sub_sections = tuple(new_sequence)
        else:
            self._sub_sections = None
        assert self.run_paranoia_checks()

    def run_paranoia_checks(self) -> bool:
        super().run_paranoia_checks()
        assert not self._sub_sections or all([isinstance(s, Section) for s in self._sub_sections
                                             ]), "Section content should be a sequence of Sections"
        return True

    def __add__(self, other):
        if isinstance(other, Macro):
            other = MacroPool([other])
        self.sub_sections = self.sub_sections + [other]
        return self

    def __str__(self):
        if self._sub_sections:
            return "%s:[%s]" % (
                self._name,
                ", ".join([str(_) for _ in self._sub_sections]),
            )
        else:
            return "%s:[,]" % (self._name,)


class SubsectionsAlternative(Section):
    """A list of alternative (sub)sections. This type of section contains a
    sequence of sections."""

    def __init__(self, name: str, sub_sections: Sequence[Section] = None, **kwargs) -> None:
        if not name:
            name = Section.anonymous('sa')
        super().__init__(name, **kwargs)
        self.size = (1, 1)
        self._sub_sections = sub_sections

    @property
    def sub_sections(self) -> List[Section]:
        return list(self._sub_sections)

    @sub_sections.setter
    def sub_sections(self, new_sequence: Sequence[Section]) -> None:
        if new_sequence:
            self._sub_sections = tuple(new_sequence)
        else:
            self._sub_sections = None
        assert self.run_paranoia_checks()

    def run_paranoia_checks(self) -> bool:
        super().run_paranoia_checks()
        assert not self._sub_sections or all([isinstance(s, Section) for s in self._sub_sections
                                             ]), "Section content should be a sequence of Sections"
        return True

    def __or__(self, other):
        """Or may be used to build SubsectionsAlternative from Sections"""
        ns = SubsectionsAlternative(Section.anonymous('sa'))
        ns.sub_sections = self.sub_sections + [other]
        return ns

    def __str__(self):
        if self._sub_sections:
            return "%s:[%s]" % (
                self._name,
                " | ".join([str(_) for _ in self._sub_sections]),
            )
        else:
            return "%s:[|]" % (self._name,)


class MacroPool(Section):
    """A pool of macros."""

    def __init__(self, macro_pool: Collection[Macro] = None, name: str = None, size: Tuple[int, int] = (1, 1),
                 **kwargs) -> None:
        if not name:
            name = Section.anonymous('mp')
        super().__init__(name, **kwargs)
        self.macro_pool = macro_pool
        self._size = size

    @property
    def size(self) -> Tuple[int, int]:
        return self._size

    @size.setter
    def size(self, new_size: Tuple[int, int]) -> None:
        assert 0 <= new_size[0] <= new_size[1], "Illegal size"
        self._size = new_size

    @property
    def macro_pool(self) -> List[Macro]:
        return list(self._macro_pool)

    @macro_pool.setter
    def macro_pool(self, new_macro_pool: Collection[Macro]) -> None:
        if new_macro_pool:
            self._macro_pool = tuple(new_macro_pool)
        else:
            self._macro_pool = None
        assert self.run_paranoia_checks()

    def run_paranoia_checks(self) -> bool:
        super().run_paranoia_checks()
        assert not self._macro_pool or all([isinstance(s, Macro) for s in self._macro_pool
                                           ]), "Macro pool should be a sequence of macros"
        return True

    def __or__(self, other):
        self.macro_pool = self.macro_pool + [other]
        return self

    def __str__(self):
        if self._macro_pool:
            return "%s:{%s}" % (
                self._name,
                ", ".join([m.describe() for m in self._macro_pool]),
            )
        else:
            return "%s:{}" % (self._name,)


class Constraints(Paranoid, Pedantic):
    """Top class for managing constraints. This class contains the set of
    macros and sections of which an individual is composed, the
    microgp.properties.Properties and the function that will evaluate the
    individuals (microgp.constraints.Constraints._evaluator).

    Args:
        file_name (str): default file name of a solution, it must contain "{id}"
    """

    DEFAULT_LABEL_FORMAT = '{node}:\n'

    def __init__(self, file_name: str = "solution{id}.ugp") -> None:
        self._sections = {
            # 'main': SubsectionsSequence(name='main', sub_sections=None, label_format=Constraints.DEFAULT_LABEL_FORMAT)
        }
        self._macros = set()
        self._global_properties = Properties()
        self._stats = dict()
        self._stats['random_individuals'] = 0
        self._stats['valid_individuals'] = 0
        self._stats['valid_individuals_warn_threshold'] = 0.01
        assert file_name.find("{id}"), "file_name doesn't contain \"{id}\"."
        self._file_name = file_name
        self._evaluator = None

    def add_macro(self, macro: Macro) -> None:
        assert macro not in self._macros, "Macro already present in constraints"
        self._macros.add(macro)

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str) -> None:
        self._file_name = file_name

    @property
    def stats(self) -> Dict:
        return self._stats

    @property
    def global_properties(self) -> Properties:
        return self._global_properties

    @property
    def macros(self) -> Dict[str, Macro]:
        return dict(self._macros)

    def add_section(self, section: Section) -> None:
        assert section not in self._sections, "Section already present in constraints"
        self._sections.add(section)

    @property
    def sections(self) -> Set[Section]:
        return set(self._sections)

    @property
    def evaluator(self) -> Callable[['Individual'], Base]:
        return self._evaluator

    @evaluator.setter
    def evaluator(self, function: Callable[['Individual'], Base]) -> None:
        self._evaluator = function

    def __getitem__(self, section_name: str) -> Section:
        assert section_name in self._sections, "Unknown section name: '%s'" % (section_name,)
        return self._sections[section_name]

    def __setitem__(self, section_name: str, new_section_definition: Any) -> None:
        sec = make_section(new_section_definition, name=section_name)
        if section_name in self._sections:
            del self._sections[section_name]
        if sec.label_format is None:
            sec.label_format = Constraints.DEFAULT_LABEL_FORMAT
        self.add_section_recursive(sec, label_format=sec.label_format)
        assert self.run_paranoia_checks()

    def add_section_recursive(self, section: Section, label_format: str) -> None:
        if section.label_format is None:
            section.label_format = label_format
        if section.name in self.sections:
            assert section == self._sections[section.name], "Duplicate definition of %s" % (section,)
        else:
            self._sections[section.name] = section
            if isinstance(section, MacroPool):
                pass
            else:
                for sec in section.sub_sections:
                    self.add_section_recursive(sec, section.label_format)

    def run_paranoia_checks(self) -> bool:
        for sec in self._sections.values():
            sec.run_paranoia_checks()
        for name, sec in self._sections.items():
            assert name == sec.name, "Mismatched name: %s != %s" % (name, sec.name)
        for s1, s2 in combinations(self._sections.values(), 2):
            assert s1 != s2, "Duplicated sections: %s" % (s1,)
        return True

    def is_valid(self, obj) -> bool:
        return True


def make_section(section_definition: Any,
                 name: str = None,
                 instances: Optional[Tuple[int, int]] = None,
                 size: Tuple[int, int] = None,
                 label_format: str = None) -> Section:
    """Builds a section from a human-readable description.

    Args:
        section_definition: macro, list of macros or set of macros that will be translated into MacroPool / SubsectionsSequence / SubsectionsAlternative
        name (str): Name of the section to build
        instances (tuple(int,int)): (None or (int >=0, int >0)) How many times the section can appear inside an individual
        size (tuple(int,int): ((int >=0, int >0)) number of macro that the section can contain
        label_format (str): define how to translate a node into string

    Returns:
        The section just built

    **Examples**:

    - Create a section of name `word_sec` containing a macro (word_macro), it will appear once inside the individual

        >>> word_section = ugp.make_section(word_macro, size=(1, 1), name='word_sec')

    - Create a section of name `sec_jmp` that contains 1 to 4 macros (jmp1), it will appear once inside the individual

        >>> sec_jmp = ugp.make_section(jmp1, size=(1, 4), name='sec_jmp')

    - Create a section with a default unique name that contains 2 to 5 macros chosen in {add, sub} and it can appear 0 to 10 times inside the individual

        >>> generic_math = ugp.make_section({add, sub}, size=(2, 5), instances=(0, 10))

    - Build the **main** section with 3 sections, the second one is a `SubsectionsSequence`_ that contains 3 sections:

        - A `SubsectionsAlternative`_ {sec2a, sec2b}
        - A simple section sec_jmp (`MacroPool`_)
        - A simple section containing a Macro without parameters (`MacroPool`_)

        >>> library['main'] = [
        >>>     'Prologue...'
        >>>     [{sec2a, sec2b}, sec_jmp, '; this is a comment'],
        >>>     'Epilogue...'
        >>> ]

    The **main** section is contained inside the `RootSection`_.

    """
    section = None
    if isinstance(section_definition, Section):
        if name:
            section_definition._name = name
        section = section_definition
    elif isinstance(section_definition, Macro):
        section = MacroPool(macro_pool=[section_definition], name=name, label_format=label_format)
    elif isinstance(section_definition, str):
        section = MacroPool(macro_pool=[Macro(text=section_definition)],
                            label_format=label_format,
                            name=Section.anonymous('str'))
    elif isinstance(section_definition, list) or isinstance(section_definition, tuple):
        section = SubsectionsSequence(sub_sections=[make_section(s) for s in section_definition],
                                      name=name,
                                      label_format=label_format)
    elif isinstance(section_definition, set):
        tmp = list(section_definition)
        if isinstance(tmp[0], Macro):
            section = MacroPool(macro_pool=tmp, name=name, label_format=label_format)
        else:
            section = SubsectionsAlternative(sub_sections=tmp, name=name, label_format=label_format)
    else:
        raise TypeError("Unknown section type")

    assert isinstance(section, Section), "Panic: Invalid type"
    section.instances = instances
    if size:
        section.size = size
        assert isinstance(section.size[0], int) and section.size[0] >= 0, "minimum size should be an integer >= 0"
        assert isinstance(section.size[1], int) and section.size[1] > 0, "maximum size should be an integer > 0"
    return section
