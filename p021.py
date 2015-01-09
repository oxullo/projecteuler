#!/usr/bin/env python
# -*- coding: utf-8 -*-

def divisors(n):
    dv = []
    d = n - 1
    while d >= 1:
        if n % d == 0:
            dv.append(d)
        d -= 1

    return dv

def d(n):
    return sum(divisors(n))

if __name__ == '__main__':
    print d(220), d(284)

    amicable = set()
    for i in xrange(10000):
        sd = d(i)
        if sd > i and d(sd) == i:
            amicable.add(i)
            amicable.add(sd)

    print sum(amicable)