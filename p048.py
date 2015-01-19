#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ssum(n):
	total = 1
	for i in xrange(2, n+1):
		total += i**i
	
	return total

if __name__ == '__main__':
	print str(ssum(1000))[-10:]
