#! /usr/bin/env python3

# This file is a part of NUMCL project.
# Copyright (c) 2019 IBM Corporation
# SPDX-License-Identifier: LGPL-3.0-or-later
# 
# NUMCL is free software: you can redistribute it and/or modify it under the terms
# of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any
# later version.
# 
# NUMCL is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# NUMCL.  If not, see <http://www.gnu.org/licenses/>.

from numpy import *
from benchmarker import Benchmarker, Reporter

class Short(Reporter):
    def __init__(self):
        super().__init__(20)
    def report_ranking(self, benchmarks):
        return ''
    def report_matrix(self, benchmarks):
        return ''

with Benchmarker(loop=100, filter="tag!=slow", reporter=Short()) as bench:

    a = zeros((100,100,100))
    b = ones ((100,100,100))

    @bench('5math/sin/0')
    def run(bm):
        for i in bm:
            sin(a)
    @bench('5math/cos/0')
    def run(bm):
        for i in bm:
            cos(a)
    @bench('5math/tan/0')
    def run(bm):
        for i in bm:
            tan(a)
    @bench('5math/sinh/0')
    def run(bm):
        for i in bm:
            sinh(a)
    @bench('5math/cosh/0')
    def run(bm):
        for i in bm:
            cosh(a)
    @bench('5math/tanh/0')
    def run(bm):
        for i in bm:
            tanh(a)
    @bench('5math/asin/0')
    def run(bm):
        for i in bm:
            arcsin(a)
    @bench('5math/acos/0')
    def run(bm):
        for i in bm:
            arccos(a)
    @bench('5math/atan/0')
    def run(bm):
        for i in bm:
            arctan(a)
    @bench('5math/exp/0')
    def run(bm):
        for i in bm:
            exp(a)
    @bench('5math/log/0')
    def run(bm):
        for i in bm:
            log(b)
