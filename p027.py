#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import calc

def num_primes(a, b):
    primes = 0
    n = 0
    while True:
        if not calc.isprime(n ** 2 + a * n + b):
            break
        else:
            primes += 1
        n += 1

    return primes


if __name__ == '__main__':
    print num_primes(-79, 1601)

    primes = [n for n in xrange(1, 1000) if calc.isprime(n)]
    b_domain = primes + [-n for n in primes]
    results = []
    for a in xrange(-999, 1000):
        for b in b_domain:
            results.append((num_primes(a, b), a, b))

    results.sort(key=operator.itemgetter(0))
    print results[-1]
    print results[-1][1] * results[-1][2]
