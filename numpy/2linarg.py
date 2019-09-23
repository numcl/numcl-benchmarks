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

    a = zeros((100,100))
    b = zeros((100,100))
    c = zeros((100,100))

    a2 = zeros((1000,1000))
    b2 = zeros((1000,1000))
    c2 = zeros((1000,1000))
    
    d = zeros((100))
    e = zeros((100))
    
    @bench('2linarg/diag/einsum')
    def run(bm):
        for i in bm:
            einsum('ii->i',a)
    
    @bench('2linarg/diag/builtin')
    def run(bm):
        for i in bm:
            diag(a)

    @bench('2linarg/eye/naive')
    def run(bm):
        for i in bm:
            a = zeros((100,100))
            for j in range(100):
                a[j,j] = 1
            
    @bench('2linarg/eye/builtin')
    def run(bm):
        for i in bm:
            eye(100)

    @bench('2linarg/gemm/einsum')
    def run(bm):
        for i in bm:
            einsum('ij,jk->ik',a,b,out=c)
    
    @bench('2linarg/gemm/builtin')
    def run(bm):
        for i in bm:
            matmul(a,b,out=c)
            
    @bench('2linarg/gemm-large/einsum')
    def run(bm):
        for i in bm:
            einsum('ij,jk->ik',a2,b2,out=c2)
    
    @bench('2linarg/gemm-large/builtin')
    def run(bm):
        for i in bm:
            matmul(a2,b2,out=c2)

    @bench('2linarg/inner/einsum')
    def run(bm):
        for i in bm:
            einsum('i,i->',d,e)
    
    @bench('2linarg/inner/builtin')
    def run(bm):
        for i in bm:
            inner(d,e)

    @bench('2linarg/kron/einsum', tag="slow")
    def run(bm):
        for i in bm:
            einsum('ij,kl->ikjl',a,b)
    
    @bench('2linarg/kron/builtin', tag="slow")
    def run(bm):
        for i in bm:
            kron(a,b)

    @bench('2linarg/outer/einsum')
    def run(bm):
        for i in bm:
            einsum('i,j->ij',d,e)
    
    @bench('2linarg/outer/builtin')
    def run(bm):
        for i in bm:
            outer(d,e)

    @bench('2linarg/tri/builtin')
    def run(bm):
        for i in bm:
            tri(100)

    @bench('2linarg/tril/builtin')
    def run(bm):
        for i in bm:
            tril(b)

    @bench('2linarg/triu/builtin')
    def run(bm):
        for i in bm:
            triu(b)

    @bench('2linarg/vander/builtin')
    def run(bm):
        for i in bm:
            vander(d)

    @bench('2linarg/vdot/einsum')
    def run(bm):
        for i in bm:
            einsum('i,i->',conjugate(d),e)
    
    @bench('2linarg/vdot/builtin')
    def run(bm):
        for i in bm:
            vdot(d,e)
