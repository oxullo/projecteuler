#!/usr/bin/env python
# -*- coding: utf-8 -*-

allsum = 0
for i in xrange(1000):
    if i / 3 == i / 3.0 or i / 5 == i / 5.0:
        allsum += i

print allsum