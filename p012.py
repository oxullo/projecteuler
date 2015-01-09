#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# slow!
def divisors(n):
    dv = 1
    d = n - 1
    while d >= 1:
        if n % d == 0:
            dv += 1
        d -= 1

    return dv

def trinum(n):
    return n * (n+1) / 2

#http://stackoverflow.com/questions/110344/algorithm-to-calculate-the-number-of-divisors-of-a-given-number
import operator
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2

# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d

def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)

if __name__ == '__main__':
    i = 0
    mx = 0
    t = 0
    while True:
        i += 1
        ln = NumberOfDivisors(trinum(i))
        mx = max(mx, ln)
        if time.time() - t > 1:
            print i, mx
            t = time.time()

        if ln > 500:
            print 'Tri: %d Divs: %d Trinum: %d' % (i, ln, trinum(i))
            break
