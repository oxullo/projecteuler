#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import operator

def test(p):
	solutions = 0
	for a in xrange(1, p/2):
		for b in xrange(1, p/2):
			c = math.sqrt(a**2 + b**2)
			if a + b + c == p:
				solutions += 1

	return solutions

if __name__ == '__main__':
	all_solutions = []
	for i in xrange(3, 1001):
		solutions = test(i)
		if solutions:
			all_solutions.append((i, solutions))

	all_solutions.sort(key=operator.itemgetter(1))
	print all_solutions[-1]
