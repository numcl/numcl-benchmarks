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

    @bench('1allocation/ones/bool')
    def run(bm):
        for i in bm:
            a = ones(1000000,bool)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/ones/int8')
    def run(bm):
        for i in bm:
            a = ones(1000000,int8)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/ones/int16')
    def run(bm):
        for i in bm:
            a = ones(1000000,int16)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/ones/int32')
    def run(bm):
        for i in bm:
            a = ones(1000000,int32)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/ones/int64')
    def run(bm):
        for i in bm:
            a = ones(1000000,int64)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/ones/float32')
    def run(bm):
        for i in bm:
            a = ones(1000000,float32)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/ones/float64')
    def run(bm):
        for i in bm:
            a = ones(1000000,float64)
            a[0] = 1
            a[-1] = 1

    @bench('1allocation/zeros/bool')
    def run(bm):
        for i in bm:
            a = zeros(1000000,bool)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/zeros/int8')
    def run(bm):
        for i in bm:
            a = zeros(1000000,int8)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/zeros/int16')
    def run(bm):
        for i in bm:
            a = zeros(1000000,int16)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/zeros/int32')
    def run(bm):
        for i in bm:
            a = zeros(1000000,int32)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/zeros/int64')
    def run(bm):
        for i in bm:
            a = zeros(1000000,int64)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/zeros/float32')
    def run(bm):
        for i in bm:
            a = zeros(1000000,float32)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/zeros/float64')
    def run(bm):
        for i in bm:
            a = zeros(1000000,float64)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/empty/bool')
    def run(bm):
        for i in bm:
            a = empty(1000000,bool)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/empty/int8')
    def run(bm):
        for i in bm:
            a = empty(1000000,int8)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/empty/int16')
    def run(bm):
        for i in bm:
            a = empty(1000000,int16)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/empty/int32')
    def run(bm):
        for i in bm:
            a = empty(1000000,int32)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/empty/int64')
    def run(bm):
        for i in bm:
            a = empty(1000000,int64)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/empty/float32')
    def run(bm):
        for i in bm:
            a = empty(1000000,float32)
            a[0] = 1
            a[-1] = 1
    @bench('1allocation/empty/float64')
    def run(bm):
        for i in bm:
            a = empty(1000000,float64)
            a[0] = 1
            a[-1] = 1

    a = empty(1000000,bool)
    @bench('1allocation/copy/bool')
    def run(bm):
        for i in bm:
            copy(a)
    a = empty(1000000,int8)
    @bench('1allocation/copy/int8')
    def run(bm):
        for i in bm:
            copy(a)
    a = empty(1000000,int16)
    @bench('1allocation/copy/int16')
    def run(bm):
        for i in bm:
            copy(a)
    a = empty(1000000,int32)
    @bench('1allocation/copy/int32')
    def run(bm):
        for i in bm:
            copy(a)
    a = empty(1000000,int64)
    @bench('1allocation/copy/int64')
    def run(bm):
        for i in bm:
            copy(a)
    a = empty(1000000,float32)
    @bench('1allocation/copy/float32')
    def run(bm):
        for i in bm:
            copy(a)
    a = empty(1000000,float64)
    @bench('1allocation/copy/float64')
    def run(bm):
        for i in bm:
            copy(a)

    @bench('1allocation/arange/int8')
    def run(bm):
        for i in bm:
            arange(127,dtype=int8)
    @bench('1allocation/arange/int16')
    def run(bm):
        for i in bm:
            arange(127,dtype=int16)
    @bench('1allocation/arange/int32')
    def run(bm):
        for i in bm:
            arange(127,dtype=int32)
    @bench('1allocation/arange/int64')
    def run(bm):
        for i in bm:
            arange(127,dtype=int64)
    @bench('1allocation/arange/float32')
    def run(bm):
        for i in bm:
            arange(127.0,dtype=float32)
    @bench('1allocation/arange/float64')
    def run(bm):
        for i in bm:
            arange(127.0,dtype=float64)
            
    
