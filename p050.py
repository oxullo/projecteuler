#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is hacky and works just by coincidence
# in fact, the first test fails, returning a 5-addenda sum

import utils

primes = utils.get_primes()
primes_set = set(primes)

def find_max_addenda(top):
    sums = [primes[0]]

    for p in primes[1:]:
        last = p + sums[-1]
        if last > top:
            break
        sums.append(last)

    for i, s in enumerate(sums):
        candidate = sums[-1] - s
        if candidate in primes_set:
            return len(sums) - i - 1, candidate

def test():
    print find_max_addenda(100)
    print find_max_addenda(1000)

if __name__ == '__main__':
    print find_max_addenda(1E6)
