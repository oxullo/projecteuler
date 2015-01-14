#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import calc

nprod = 1
dprod = 1
for n in xrange(11, 50):
	for d in xrange(50, 100):
		nd = set(utils.num_to_digits(n))
		dd = set(utils.num_to_digits(d))

		if len(nd) == 1 or len(dd) == 1 or nd == dd or n % 10 == 0 or d % 10 == 0:
			continue

		common = nd.intersection(dd)

		if common:
			q = float(n) / d
			nsing = list(nd-common)[0]
			dsing = list(dd-common)[0]

			if dsing:
				qsem = float(nsing) / dsing
				if q == qsem:
					print nsing, dsing
					nprod *= nsing
					dprod *= dsing

print dprod / calc.gcd(nprod, dprod)
