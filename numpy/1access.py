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

    a = zeros((100,100,100,100))
    b = zeros((100,100,100))
    c = zeros((100,100))
    d = zeros((100))
    tmp = 0.0

    @bench('1access/write/0')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[i,i,i,i] = 1
    @bench('1access/write/1')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[i,i,i,:] = 1
    @bench('1access/write/2')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[i,i,:,i] = 1
    @bench('1access/write/3')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[i,:,i,i] = 1
    @bench('1access/write/4')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[:,i,i,i] = 1
    @bench('1access/read/0')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[i,i,i,i]
    @bench('1access/read/1')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[i,i,i,:]
    @bench('1access/read/2')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[i,i,:,i]
    @bench('1access/read/3')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[i,:,i,i]
    @bench('1access/read/4')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[:,i,i,i]
    
    @bench('1access/write-range/0')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[i,20:50,i,i] = 1
    @bench('1access/write-range/1')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[i,20:50,i,:] = 1
    @bench('1access/write-range/2')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[i,20:50,:,i] = 1
    @bench('1access/write-range/3')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[i,:,20:50,i] = 1
    @bench('1access/write-range/4')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[:,i,20:50,i] = 1
    @bench('1access/read-range/0')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[i,20:50,i,i]
    @bench('1access/read-range/1')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[i,20:50,i,:]
    @bench('1access/read-range/2')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[i,20:50,:,i]
    @bench('1access/read-range/3')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[i,:,20:50,i]
    @bench('1access/read-range/4')
    def run(bm):
        for i in bm:
            for i in range(100):
                tmp = a[:,i,20:50,i]

    @bench('1access/write-batch/0')
    def run(bm):
        for i in bm:
            for i in range(100):
                a[i] = b
    @bench('1access/write-batch/1')
    def run(bm):
        for i in bm:
            for i in range(100):
                for j in range(100):
                    a[i,j] = b[j]
