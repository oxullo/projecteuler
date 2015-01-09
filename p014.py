#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

def collatz_iters(n):
    iters = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

        iters += 1

    return iters

if __name__ == '__main__':
    v = []
    for i in xrange(int(1E06)):
        v.append((i, collatz_iters(i)))

    v.sort(key=operator.itemgetter(1))
    print v[-1]