#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

def concat_product(n, factors):
	result = ''
	for factor in factors:
		result += str(n*factor)

	return result


if __name__ == '__main__':
	results = []

	# given m>1 n can't have more than 5 digits
	for n in xrange(9, 9999):
		for m in xrange(2, 10):
			cr = concat_product(n, xrange(1, m+1))
			if utils.ispandigital(cr):
				results.append(cr)

	print max(results)
