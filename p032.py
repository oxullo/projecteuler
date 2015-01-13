#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ispandigital(ns):
	return list(xrange(1, 10)) == sorted([int(digit) for digit in ns])

if __name__ == '__main__':
	results = set()

	for a in xrange(1, 10000):
		for b in xrange(1, 10000):
			m = a * b
			s = str(a) + str(b) + str(m)
			if len(s) == 9 and ispandigital(s):
				results.add(m)

	print sum(results)
