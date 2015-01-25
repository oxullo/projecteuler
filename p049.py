#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

primes_4dig = [p for p in utils.get_primes() if p > 999 and p < 10000]
primes_4dig_set = set(primes_4dig)

for p2 in primes_4dig:
    for p1 in [p for p in primes_4dig if p < p2]:
        p3 = 2 * p2 - p1
        if (p3 in primes_4dig_set and
                set(utils.num_to_digits(p1)) ==
                set(utils.num_to_digits(p2)) ==
                set(utils.num_to_digits(p3))):
            print '%d%d%d' % (p1, p2, p3)
