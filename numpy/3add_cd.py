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
