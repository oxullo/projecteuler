#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calc

s = 0
for i in xrange(2, int(2E06)):
    if calc.isprime(i):
        s += i

print s
