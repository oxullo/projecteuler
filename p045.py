#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Another TnE
MAX_N = 100000

def tri_number(n):
    return n * (n + 1) / 2

def pent_number(n):
    return n * (3 * n - 1) / 2

def hex_number(n):
    return n * (2 * n - 1)

def test():
    tri = [tri_number(n) for n in xrange(1, 6)]
    pent = [pent_number(n) for n in xrange(1, 6)]
    hex = [hex_number(n) for n in xrange(1, 6)]

if __name__ == '__main__':
    test()

    tris = set([tri_number(n) for n in xrange(1, MAX_N)])
    penties = set([pent_number(n) for n in xrange(1, MAX_N)])
    hexies = set([hex_number(n) for n in xrange(1, MAX_N)])

    print tris.intersection(penties).intersection(hexies)
