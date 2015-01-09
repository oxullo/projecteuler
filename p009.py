#!/usr/bin/env python
# -*- coding: utf-8 -*-

for a in xrange(1, 1001):
    for b in xrange(1, 1001):
        for c in xrange(1, 1001):
            if a < b and b < c and a + b + c == 1000:
                if a ** 2 + b ** 2 == c ** 2:
                    print a, b, c
                    break

