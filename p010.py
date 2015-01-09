#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Archimedes Exhibitions GmbH,
# Saarbrücker Str. 24b, Berlin, Germany
#
# This file contains proprietary source code and confidential
# information. Its contents may not be disclosed or distributed to
# third parties unless prior specific permission by Archimedes
# Exhibitions GmbH, Berlin, Germany is obtained in writing. This applies
# to copies made in any form and using any medium. It applies to
# partial as well as complete copies.

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

s = 0
for i in xrange(2, int(2E06)):
    if i % 10000 == 0:
        print i

    if isprime(i):
        s += i

print s
