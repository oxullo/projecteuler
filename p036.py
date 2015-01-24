#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

result = 0
for i in xrange(1, int(1E6)):
    if utils.ispalindromic(i) and utils.ispalindromic(bin(i)[2:]):
        result += i

print result

