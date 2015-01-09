#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sq = sum(xrange(1, 101)) ** 2
    ssq = 0
    for i in xrange(1, 101):
        ssq += i ** 2

    print sq - ssq

