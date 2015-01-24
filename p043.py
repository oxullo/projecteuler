#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import utils


coercions = [
        (1, 4, 2),
        (2, 5, 3),
        (3, 6, 5),
        (4, 7, 7),
        (5, 8, 11),
        (6, 9, 13),
        (7, 10, 17)]

pandigitals = itertools.permutations(list(xrange(10)))


total = 0
for pandigital in pandigitals:
    good = True
    for c in coercions:
        if utils.digits_to_num(pandigital[c[0]:c[1]]) % c[2] != 0:
            good = False
            break

    if good:
        print pandigital
        total += utils.digits_to_num(pandigital)

print total
