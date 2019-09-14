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
from benchmarker import Benchmarker

loop = 1000

with Benchmarker(loop, width=20) as bench:

    v_s   = zeros(10000,float32)
    v_d   = zeros(10000,float64)
    v_cs  = zeros(10000,complex64)
    v_cd  = zeros(10000,complex128)
    v_i1  = zeros(10000,bool)
    v_i8  = zeros(10000,int8)
    v_i16 = zeros(10000,int16)
    v_i32 = zeros(10000,int32)
    v_i64 = zeros(10000,int64)

    @bench('add_cd')
    def run(bm):
        for i in bm:
            v_cd+v_cd

    @bench('add_cs')
    def run(bm):
        for i in bm:
            v_cs+v_cs

    @bench('add_d')
    def run(bm):
        for i in bm:
            v_d+v_d

    @bench('add_di32')
    def run(bm):
        for i in bm:
            v_d+v_i32

    @bench('add_i1')
    def run(bm):
        for i in bm:
            v_i1+v_i1

    @bench('add_i8')
    def run(bm):
        for i in bm:
            v_i8+v_i8

    @bench('add_i16')
    def run(bm):
        for i in bm:
            v_i16+v_i16

    @bench('add_i32')
    def run(bm):
        for i in bm:
            v_i32+v_i32

    @bench('add_i64')
    def run(bm):
        for i in bm:
            v_i64+v_i64

    @bench('add_s')
    def run(bm):
        for i in bm:
            v_s+v_s

    @bench('add_sd')
    def run(bm):
        for i in bm:
            v_s+v_d

    @bench('add_si32')
    def run(bm):
        for i in bm:
            v_s+v_i32


    @bench('mul_cd')
    def run(bm):
        for i in bm:
            v_cd*v_cd

    @bench('mul_cs')
    def run(bm):
        for i in bm:
            v_cs*v_cs

    @bench('mul_d')
    def run(bm):
        for i in bm:
            v_d*v_d

    @bench('mul_di32')
    def run(bm):
        for i in bm:
            v_d*v_i32

    @bench('mul_i1')
    def run(bm):
        for i in bm:
            v_i1*v_i1

    @bench('mul_i8')
    def run(bm):
        for i in bm:
            v_i8*v_i8

    @bench('mul_i16')
    def run(bm):
        for i in bm:
            v_i16*v_i16

    @bench('mul_i32')
    def run(bm):
        for i in bm:
            v_i32*v_i32

    @bench('mul_i64')
    def run(bm):
        for i in bm:
            v_i64*v_i64

    @bench('mul_s')
    def run(bm):
        for i in bm:
            v_s*v_s

    @bench('mul_sd')
    def run(bm):
        for i in bm:
            v_s*v_d

    @bench('mul_si32')
    def run(bm):
        for i in bm:
            v_s*v_i32
            

    @bench('fma_cd')
    def run(bm):
        for i in bm:
            v_cd*v_cd+v_cd

    @bench('fma_cs')
    def run(bm):
        for i in bm:
            v_cs*v_cs+v_cs

    @bench('fma_d')
    def run(bm):
        for i in bm:
            v_d*v_d+v_d

    @bench('fma_di32')
    def run(bm):
        for i in bm:
            v_d*v_i32+v_i32

    @bench('fma_i1')
    def run(bm):
        for i in bm:
            v_i1*v_i1+v_i1

    @bench('fma_i8')
    def run(bm):
        for i in bm:
            v_i8*v_i8+v_i8

    @bench('fma_i16')
    def run(bm):
        for i in bm:
            v_i16*v_i16+v_i16

    @bench('fma_i32')
    def run(bm):
        for i in bm:
            v_i32*v_i32+v_i32

    @bench('fma_i64')
    def run(bm):
        for i in bm:
            v_i64*v_i64+v_i64
            
    @bench('fma_s')
    def run(bm):
        for i in bm:
            v_s*v_s+v_s

    @bench('fma_si32')
    def run(bm):
        for i in bm:
            v_s*v_i32+v_i32
