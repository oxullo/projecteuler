#!/usr/bin/env python
# -*- coding: utf-8 -*-

powlist = set()
for a in xrange(2, 101):
	for b in xrange(2, 101):
		powlist.add(a**b)

print len(powlist)
