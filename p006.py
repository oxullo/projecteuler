#!/usr/bin/env python
# -*- coding: utf-8 -*-

sq = sum(xrange(1, 101)) ** 2
ssq = 0
for i in xrange(1, 101):
    ssq += i ** 2

print sq - ssq

