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

    @bench('ones/bool')
    def run(bm):
        for i in bm:
            a = ones(1000000,bool)
            a[0] = 1
            a[-1] = 1
    @bench('ones/int8')
    def run(bm):
        for i in bm:
            a = ones(1000000,int8)
            a[0] = 1
            a[-1] = 1
    @bench('ones/int16')
    def run(bm):
        for i in bm:
            a = ones(1000000,int16)
            a[0] = 1
            a[-1] = 1
    @bench('ones/int32')
    def run(bm):
        for i in bm:
            a = ones(1000000,int32)
            a[0] = 1
            a[-1] = 1
    @bench('ones/int64')
    def run(bm):
        for i in bm:
            a = ones(1000000,int64)
            a[0] = 1
            a[-1] = 1
    @bench('ones/float32')
    def run(bm):
        for i in bm:
            a = ones(1000000,float32)
            a[0] = 1
            a[-1] = 1
    @bench('ones/float64')
    def run(bm):
        for i in bm:
            a = ones(1000000,float64)
            a[0] = 1
            a[-1] = 1

    @bench('zeros/bool')
    def run(bm):
        for i in bm:
            a = zeros(1000000,bool)
            a[0] = 1
            a[-1] = 1
    @bench('zeros/int8')
    def run(bm):
        for i in bm:
            a = zeros(1000000,int8)
            a[0] = 1
            a[-1] = 1
    @bench('zeros/int16')
    def run(bm):
        for i in bm:
            a = zeros(1000000,int16)
            a[0] = 1
            a[-1] = 1
    @bench('zeros/int32')
    def run(bm):
        for i in bm:
            a = zeros(1000000,int32)
            a[0] = 1
            a[-1] = 1
    @bench('zeros/int64')
    def run(bm):
        for i in bm:
            a = zeros(1000000,int64)
            a[0] = 1
            a[-1] = 1
    @bench('zeros/float32')
    def run(bm):
        for i in bm:
            a = zeros(1000000,float32)
            a[0] = 1
            a[-1] = 1
    @bench('zeros/float64')
    def run(bm):
        for i in bm:
            a = zeros(1000000,float64)
            a[0] = 1
            a[-1] = 1
    @bench('empty/bool')
    def run(bm):
        for i in bm:
            a = empty(1000000,bool)
            a[0] = 1
            a[-1] = 1
    @bench('empty/int8')
    def run(bm):
        for i in bm:
            a = empty(1000000,int8)
            a[0] = 1
            a[-1] = 1
    @bench('empty/int16')
    def run(bm):
        for i in bm:
            a = empty(1000000,int16)
            a[0] = 1
            a[-1] = 1
    @bench('empty/int32')
    def run(bm):
        for i in bm:
            a = empty(1000000,int32)
            a[0] = 1
            a[-1] = 1
    @bench('empty/int64')
    def run(bm):
        for i in bm:
            a = empty(1000000,int64)
            a[0] = 1
            a[-1] = 1
    @bench('empty/float32')
    def run(bm):
        for i in bm:
            a = empty(1000000,float32)
            a[0] = 1
            a[-1] = 1
    @bench('empty/float64')
    def run(bm):
        for i in bm:
            a = empty(1000000,float64)
            a[0] = 1
            a[-1] = 1

    a = empty(1000000,bool)
    @bench('copy/bool')
    def run(bm):
        for i in bm:
            b = copy(a)
    a = empty(1000000,int8)
    @bench('copy/int8')
    def run(bm):
        for i in bm:
            b = copy(a)
    a = empty(1000000,int16)
    @bench('copy/int16')
    def run(bm):
        for i in bm:
            b = copy(a)
    a = empty(1000000,int32)
    @bench('copy/int32')
    def run(bm):
        for i in bm:
            b = copy(a)
    a = empty(1000000,int64)
    @bench('copy/int64')
    def run(bm):
        for i in bm:
            b = copy(a)
    a = empty(1000000,float32)
    @bench('copy/float32')
    def run(bm):
        for i in bm:
            b = copy(a)
    a = empty(1000000,float64)
    @bench('copy/float64')
    def run(bm):
        for i in bm:
            b = copy(a)
            
