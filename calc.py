#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Vec2D(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return '<%s(%.2f, %.2f)>' % (self.__class__.__name__, self.x, self.y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

# http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
def isprime(n):
   """Returns True if n is prime"""
   if n == 2: return True
   if n == 3: return True
   if n % 2 == 0: return False
   if n % 3 == 0: return False

   i = 5
   w = 2
   while i * i <= n:
      if n % i == 0:
         return False

      i += w
      w = 6 - w

   return True

# http://rosettacode.org/wiki/Fibonacci_sequence#Python
def fibonacci_iter(n):
    if n in (0, 1):
        return 1

    fn1 = fn = 1
    for i in xrange(2, n):
        fn1, fn = fn, fn1 + fn

    return fn
