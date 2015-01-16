#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

if __name__ == '__main__':
    lst = []
    for f1 in xrange(1000, 100, -1):
        for f2 in xrange(1000, 100, -1):
            p = f1 * f2
            if utils.ispalindromic(p):
                print f1, f2, p
                lst.append(p)

    print sorted(lst)[-1]
