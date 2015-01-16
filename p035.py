#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calc
import utils

def all_rotations(nd):
	results = []
	for i in xrange(len(nd) - 1):
		nd.append(nd.pop(0))
		results.append(nd[:])

	return results

def count_circular(numbers):
	totals = 0

	while numbers:
		nd = numbers.pop(0)
		# Exclude numbers with even and 5 digits
		if any([(i%2==0 or i%5==0) for i in nd]):
			continue

		if nd == ([nd[0]] * len(nd)):
			totals += 1
		else:
			flag = True
			for rot in all_rotations(nd):
				if rot in numbers:
					numbers.remove(rot)
				else:
					flag = False
					break

			if flag:
				totals += len(nd)

	return totals


if __name__ == '__main__':
	primes = utils.get_primes()

	totals = len([n for n in primes if n < 10 and n > 1])
	for i in xrange(2, 7):
		print 'Processing %d-length digits' % i
		series = [utils.num_to_digits(n) for n in primes if n >= 10**(i-1) and n < 10**i]
		totals += count_circular(series)

	print totals
