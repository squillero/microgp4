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

# MEMO
# python .\setup.py sdist
# twine upload dist/*

import setuptools
from microgp import __version__ as ugp_version

with open("description.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()
for r in ['m2r']:
    if r in requirements:
        del requirements[requirements.index(r)]

setuptools.setup(
    name="microgp",
    version=ugp_version,
    author="Giovanni Squillero",
    author_email="squillero@polito.it",
    license='Apache-2.0',
    description="A multi-purpose extensible self-adaptive evolutionary algorithm",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://squillero.github.io/microgp4/",
    project_urls={
        "Bug Tracker": "https://github.com/squillero/microgp4/issues",
        "Documentation": "https://microgp4.readthedocs.io/en/pre-alpha/",
        "Source Code": "https://github.com/squillero/microgp4/tree/pre-alpha",
    },
    keywords='optimization evolutionary-algorithm computational-intelligence',
    packages=setuptools.find_packages(),
    package_data={'': ['requirements.txt']},
    data_files=[('.', ['requirements.txt'])],
    classifiers=[
        "Programming Language :: Python :: 3", "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha", "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=requirements,
)
