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

    b = zeros((100,100))
    c = zeros((100,100))
    b2 = zeros((30,30))
    c2 = zeros((30,30))
    
    d = zeros((1000))
    e = zeros((1000))
    
    @bench('builtin_tri')
    def run(bm):
        for i in bm:
            tri(100)
