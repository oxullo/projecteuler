#!/usr/bin/env python
# -*- coding: utf-8 -*-

UPPER_LIMIT = 28123

def divisors(n):
    dv = []
    d = n - 1
    while d >= 1:
        if n % d == 0:
            dv.append(d)
        d -= 1

    return dv

def isabundant(n):
    divs_sum = sum(divisors(n))
    return divs_sum > n


if __name__ == '__main__':
    import itertools

    print 'Calculating abundants'
    abundants = [i for i in xrange(UPPER_LIMIT + 1) if isabundant(i)]
    print 'Calculating pairs sums'
    pairsums = set([sum(comb)
            for comb in itertools.combinations_with_replacement(abundants, 2)])

    s = 0
    for i in xrange(UPPER_LIMIT + 1):
        if not i in pairsums:
            s += i

    print s
