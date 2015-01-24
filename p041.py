#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import calc


def test_permutations(digits):
    for perm in itertools.permutations(digits):
        n = int(''.join(perm))
        if calc.isprime(n):
            return n

if __name__ == '__main__':
    for dn in xrange(9, 2, -1):
        digits = ''.join([str(d) for d in xrange(dn, 0, -1)])

        first_found = test_permutations(digits)
        if first_found:
            print first_found
            break
