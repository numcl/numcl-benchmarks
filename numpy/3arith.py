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

    v_s   = zeros(10000,float32)
    v_d   = zeros(10000,float64)
    v_cs  = zeros(10000,complex64)
    v_cd  = zeros(10000,complex128)
    v_i1  = zeros(10000,bool)
    v_i8  = zeros(10000,int8)
    v_i16 = zeros(10000,int16)
    v_i32 = zeros(10000,int32)
    v_i64 = zeros(10000,int64)

    @bench('3arith/add_i1_i1')
    def run(bm):
        for i in bm:
            v_i1+v_i1

    @bench('3arith/add_i8_i8')
    def run(bm):
        for i in bm:
            v_i8+v_i8

    @bench('3arith/add_i16_i16')
    def run(bm):
        for i in bm:
            v_i16+v_i16

    @bench('3arith/add_i32_i32')
    def run(bm):
        for i in bm:
            v_i32+v_i32

    @bench('3arith/add_i64_i64')
    def run(bm):
        for i in bm:
            v_i64+v_i64

    @bench('3arith/add_s_s')
    def run(bm):
        for i in bm:
            v_s+v_s

    @bench('3arith/add_d_d')
    def run(bm):
        for i in bm:
            v_d+v_d
    @bench('3arith/add_cd_cd')
    def run(bm):
        for i in bm:
            v_cd+v_cd

    @bench('3arith/add_cs_cs')
    def run(bm):
        for i in bm:
            v_cs+v_cs

    @bench('3arith/add_s_d')
    def run(bm):
        for i in bm:
            v_s+v_d

    @bench('3arith/add_s_i32')
    def run(bm):
        for i in bm:
            v_s+v_i32

    @bench('3arith/add_d_i32')
    def run(bm):
        for i in bm:
            v_d+v_i32
    ################################################################
    @bench('3arith/mul_i1_i1')
    def run(bm):
        for i in bm:
            v_i1*v_i1

    @bench('3arith/mul_i8_i8')
    def run(bm):
        for i in bm:
            v_i8*v_i8

    @bench('3arith/mul_i16_i16')
    def run(bm):
        for i in bm:
            v_i16*v_i16

    @bench('3arith/mul_i32_i32')
    def run(bm):
        for i in bm:
            v_i32*v_i32

    @bench('3arith/mul_i64_i64')
    def run(bm):
        for i in bm:
            v_i64*v_i64

    @bench('3arith/mul_s_s')
    def run(bm):
        for i in bm:
            v_s*v_s

    @bench('3arith/mul_d_d')
    def run(bm):
        for i in bm:
            v_d*v_d
    @bench('3arith/mul_cd_cd')
    def run(bm):
        for i in bm:
            v_cd*v_cd

    @bench('3arith/mul_cs_cs')
    def run(bm):
        for i in bm:
            v_cs*v_cs

    @bench('3arith/mul_s_d')
    def run(bm):
        for i in bm:
            v_s*v_d

    @bench('3arith/mul_s_i32')
    def run(bm):
        for i in bm:
            v_s*v_i32

    @bench('3arith/mul_d_i32')
    def run(bm):
        for i in bm:
            v_d*v_i32

    ################################################################
    @bench('3arith/fma_i1_i1_i1')
    def run(bm):
        for i in bm:
            v_i1*v_i1+v_i1

    @bench('3arith/fma_i8_i8_i8')
    def run(bm):
        for i in bm:
            v_i8*v_i8+v_i8

    @bench('3arith/fma_i16_i16_i16')
    def run(bm):
        for i in bm:
            v_i16*v_i16+v_i16

    @bench('3arith/fma_i32_i32_i32')
    def run(bm):
        for i in bm:
            v_i32*v_i32+v_i32

    @bench('3arith/fma_i64_i64_i64')
    def run(bm):
        for i in bm:
            v_i64*v_i64+v_i64
            
    @bench('3arith/fma_s_s_s')
    def run(bm):
        for i in bm:
            v_s*v_s+v_s

    @bench('3arith/fma_d_d_d')
    def run(bm):
        for i in bm:
            v_d*v_d+v_d
    @bench('3arith/fma_cs_cs_cs')
    def run(bm):
        for i in bm:
            v_cs*v_cs+v_cs
    @bench('3arith/fma_cd_cd_cd')
    def run(bm):
        for i in bm:
            v_cd*v_cd+v_cd
    @bench('3arith/fma_d_i32_d')
    def run(bm):
        for i in bm:
            v_d*v_i32+v_d

    @bench('3arith/fma_s_i32_s')
    def run(bm):
        for i in bm:
            v_s*v_i32+v_s
    @bench('3arith/fma_s_i32_d')
    def run(bm):
        for i in bm:
            v_s*v_i32+v_d
