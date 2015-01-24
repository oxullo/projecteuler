#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

results = set()

for a in xrange(1, 10000):
    for b in xrange(1, 10000):
        m = a * b
        s = str(a) + str(b) + str(m)
        if len(s) == 9 and utils.ispandigital(s):
            results.add(m)

print sum(results)
