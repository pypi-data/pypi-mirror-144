#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Linear time-variant model predictive control in Python.
"""

from .build_mpcqp import build_mpcqp
from .mpcqp import MPCQP
from .problem import Problem
from .solution import Solution
from .solve_mpc import solve_mpc
from .solve_mpcqp import solve_mpcqp

__all__ = [
    "MPCQP",
    "Problem",
    "Solution",
    "build_mpcqp",
    "solve_mpc",
    "solve_mpcqp",
]

__version__ = "0.6.0"
