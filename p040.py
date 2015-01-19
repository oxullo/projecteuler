#!/usr/bin/env python
# -*- coding: utf-8 -*-

digits = ''

for i in xrange(int(1E7)):
	digits += str(i)

prod = 1
for i in xrange(7):
	dn = int(digits[10**i])
	prod *= dn

print prod
