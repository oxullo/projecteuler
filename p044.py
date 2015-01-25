#!/usr/bin/env python
# -*- coding: utf-8 -*-

# trial'n'error
MAX_N = 10000

def pent_number(n):
    return n * (3*n - 1) / 2

def test():
    print [pent_number(n) for n in xrange(1, 11)]

if __name__ == '__main__':
    import sys

    test()

    pent_numbers = [pent_number(n) for n in xrange(1, MAX_N)]
    pset = set(pent_numbers)

    for k in xrange(1, MAX_N):
        pk = pent_numbers[k]

        for j in xrange(k-1, 0, -1):
            pj = pent_numbers[j]
            if (pk + pj) in pset and (pk - pj) in pset:
                print k, j, pk, pj, pk - pj
                sys.exit(0)
