#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isprime(n):
    for i in xrange(2, n):
        if n % i == 0:
            return False
    return True


import time

t = time.time()

n = 600851475143

# for i in xrange(n, 0, -1):
#     if i % 1000000 == 0:
#         print '>>>',i
# 
#     if n % i == 0 and isprime(i):
#         print i
#         break

if __name__ == '__main__':
    for i in xrange(1, 100000):
        if n % i == 0 and isprime(i):
            print i, n / i, isprime(n / i)
