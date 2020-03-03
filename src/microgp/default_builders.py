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

from collections import Counter
from typing import Dict, Any

from .common_data_structures import Frame


def default_base_builder(individual: "Individual", frame: Frame, **kwargs) -> Dict[str, Any]:
    """Get base stats of the frame"""
    v = dict()

    # nodes
    nodes = individual.nodes(frame=frame, frame_path_limit=-1, data=True)
    v['nodes'] = list(nodes.keys())
    v['macro_counter'] = Counter([d['macro'] for d in nodes.values()])

    # sub sections
    v['sub_sections'] = [s.section.name for s in individual.frame_tree.get_sub_frames(frame)]

    # frame info
    v['current_frame'] = frame
    v['distance_from_root'] = individual.frame_tree.get_distance_from_root(frame)
    return v


def default_cumulative_builder(individual: "Individual", frame: Frame, **kwargs) -> Dict[str, Any]:
    """Get base cumulative stats of the frame"""
    v = dict()
    # nodes
    nodes = individual.nodes(frame=frame, frame_path_limit=-1, data=True)

    v['nodes_cumulative'] = list(nodes.keys())
    v['section_counter_cumulative'] = Counter([s.section.name for s in individual.frame_tree.get_sub_frames(frame)])
    v['macro_counter_cumulative'] = Counter([d['macro'] for d in nodes.values()])
    v['nodes_in_section_counter_cumulative'] = Counter({frame[-1].name: len(nodes)})

    # v['sub_sections'] = Counter([frame[-1].section])

    return v
