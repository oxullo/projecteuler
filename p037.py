#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calc
import utils

def rtl_rr_test(prime, primes):
	sprimel = str(prime)
	sprimer = str(prime)

	for i in xrange(len(sprimel)-1):
		sprimel = sprimel[1:]
		sprimer = sprimer[:-1]
		if not int(sprimel) in primes or not int(sprimer) in primes:
			return False

	return True


if __name__ == '__main__':
	primes = utils.get_primes()

	occurrences = 0
	result = 0
	for prime in primes:
		if prime < 10:
			continue

		if rtl_rr_test(prime, primes):
			print prime
			occurrences += 1
			result += prime

		if occurrences == 11:
			print 'Stopped at %d' % prime
			break

	print result
