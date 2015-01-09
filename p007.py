#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calc

c = 0
for i in xrange(1, 10000000):
    if calc.isprime(i):
        c += 1
        if c == 10001:
            print i
            break