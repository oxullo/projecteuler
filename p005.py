#!/usr/bin/env python
# -*- coding: utf-8 -*-

def smmul(n, mx=20):
    for d in xrange(2, mx+1):
        if n % d != 0:
            return False
    return True

if __name__ == '__main__':
    for i in xrange(20, 1000000000):
        if smmul(i):
            print i
            break
