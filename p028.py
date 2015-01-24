#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sequence: 1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49..
# f: corners
# f(0) = 1
# f(1) = 3 = f(0) + 2*1 = f(0) + 2((n-1)/4 +1)
# f(2) = 5 = f(1) + 2*1
# f(3) = 7 = f(2) + 2*1
# f(4) = 9 = f(3) + 2*1
# f(5) = 13 = f(4) + 2*2
# f(6) = 17 = f(5) + 2*2
# ..
# f(9) = 31 = f(8) + 2*3
#

def f(n):
    if n == 0:
        return 1
    else:
        return f(n-1) + 2 * ((n-1)/4+1)

def f_iter(n):
    csum = 1
    for i in xrange(n+1):
        csum += 2 * ((i-1)/4+1)

    return csum

def ringsum(n):
    if n == 0:
        return f(0)
    else:
        return sum([f_iter(i) for i in xrange(4*(n-1) + 1, 4*n + 1)])

def spiralsum(size):
    return sum([ringsum(i) for i in xrange(size / 2 + 1)])

if __name__ == '__main__':
    print spiralsum(5)
    print spiralsum(1001)