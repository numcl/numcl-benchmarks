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

loop = 100

with Benchmarker(loop) as bench:

    a = zeros((100,100))
    b = zeros((100,100))
    c = zeros((100,100))

    a2 = zeros((1000,1000))
    b2 = zeros((1000,1000))
    c2 = zeros((1000,1000))
    
    d = zeros((100))
    e = zeros((100))
    
    @bench('diag/einsum')
    def run(bm):
        for i in bm:
            einsum('ii->i',a)
    
    @bench('diag/builtin')
    def run(bm):
        for i in bm:
            diag(a)

    @bench('eye/numpy')
    def run(bm):
        for i in bm:
            a = zeros((100,100))
            for j in range(100):
                a[j,j] = 1
            
    @bench('eye/builtin')
    def run(bm):
        for i in bm:
            eye(100)

    @bench('gemm/einsum')
    def run(bm):
        for i in bm:
            einsum('ij,jk->ik',a,b,out=c)
    
    @bench('gemm/builtin')
    def run(bm):
        for i in bm:
            matmul(a,b,out=c)
            
    @bench('gemm-large/einsum', tag="slow")
    def run(bm):
        for i in bm:
            einsum('ij,jk->ik',a2,b2,out=c2)
    
    @bench('gemm-large/builtin')
    def run(bm):
        for i in bm:
            matmul(a2,b2,out=c2)

    @bench('inner/einsum')
    def run(bm):
        for i in bm:
            einsum('i,i->i',d,e)
    
    @bench('inner/builtin')
    def run(bm):
        for i in bm:
            inner(d,e)

    @bench('einsum_kron', tag="slow")
    def run(bm):
        for i in bm:
            einsum('ij,kl->ikjl',a,b)
    
    @bench('builtin_kron', tag="slow")
    def run(bm):
        for i in bm:
            kron(a,b)

    @bench('einsum_outer')
    def run(bm):
        for i in bm:
            einsum('i,j->ij',d,e)
    
    @bench('builtin_outer')
    def run(bm):
        for i in bm:
            outer(d,e)

    @bench('builtin_tri')
    def run(bm):
        for i in bm:
            tri(100)

    @bench('builtin_tril')
    def run(bm):
        for i in bm:
            tril(b)

    @bench('builtin_triu')
    def run(bm):
        for i in bm:
            triu(b)

    @bench('builtin_vander')
    def run(bm):
        for i in bm:
            vander(d)

    @bench('einsum_vdot')
    def run(bm):
        for i in bm:
            einsum('i,i->',d,e)
    
    @bench('builtin_vdot')
    def run(bm):
        for i in bm:
            vdot(d,e)
