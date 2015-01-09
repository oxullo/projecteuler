#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ispalindromic(n):
    sp = [int(a) for a in str(n)]
    for i in xrange(0, len(sp) / 2):
        if sp[i] != sp[len(sp) - i - 1]:
            return False
    return True

if __name__ == '__main__':
    lst = []
    for f1 in xrange(1000, 100, -1):
        for f2 in xrange(1000, 100, -1):
            p = f1 * f2
            if ispalindromic(p):
                print f1, f2, p
                lst.append(p)

    print sorted(lst)[-1]
