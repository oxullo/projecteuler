#!/usr/bin/env python
# -*- coding: utf-8 -*-

solutions = []
for i in xrange(2, sum([d**5 for d in [9]*5]) + 1):
    powers = [int(d)**5 for d in str(i)]
    if i == sum(powers):
        print '  ', i
        solutions.append(i)

print sum(solutions)
