#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calc

def find_dpf(target, top):
    found = []
    for n in xrange(9, top):
        if not calc.isprime(n):
            if len(set(calc.prime_factors(n))) == target:
                if found:
                    if n - max(found) > 1:
                        found = []

                found.append(n)

                if len(found) == target:
                    return found

def test():
    print find_dpf(2, 100)
    print find_dpf(3, 700)

if __name__ == '__main__':
    test()

    # Another TnE
    print find_dpf(4, 1000000)
