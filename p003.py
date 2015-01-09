#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import calc

t = time.time()

n = 600851475143

for i in xrange(1, 100000):
    if n % i == 0 and calc.isprime(i):
        print i, n / i, calc.isprime(n / i)
