#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isprime(n):
    for i in xrange(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    c = 0
    for i in xrange(1, 10000000):
        if isprime(i):
            c += 1
            print c, i
            if c == 10001:
                print i