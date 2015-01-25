#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

primes = utils.get_primes()
primes_set = set(primes)

def test(n):
    primes_test = reversed([p for p in primes if p < n])
    for p in primes_test:
        # I admit, 100 is a random upper limit
        for t in xrange(1, 100):
            if n == (p + 2 * t ** 2):
                return True

    return False

if __name__ == '__main__':
    import sys

    for n in xrange(2, primes[-1]):
        if n % 2 == 1 and n not in primes_set:
            if not test(n):
                print n
                sys.exit(0)
