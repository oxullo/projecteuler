#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import utils

max_digits = 3
while len(utils.num_to_digits(math.factorial(9) * max_digits)) > max_digits:
	max_digits += 1

top = math.factorial(9) * max_digits

results = []
for i in xrange(3, top + 1):
	idg = utils.num_to_digits(i)
	if i == sum([math.factorial(d) for d in idg]):
		print i
		results.append(i)

print sum(results)
