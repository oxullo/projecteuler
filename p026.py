#!/usr/bin/env python
# -*- coding: utf-8 -*-

# n=1
# d=7
# 
# 1 / 7 n < d
# n*10
# 10 / 7 = 1
# 10 % 7 = 3
# 
# 0.1 r=3
# 30 / 7 = 4
# 30 % 7 = 2
# 
# 0.14 r=3,2


def period_length(d):
    assert d > 0 and d > 1
    rems = []
    n = 1
    while True:
        n *= 10
        rem = n % d
        if rem in rems:
            break

        rems.append(rem)
        n = rem

    # no period
    if 0 in rems:
        return 0
    else:
        return len(rems)

if __name__ == '__main__':
    import operator

    lengths = []
    for i in xrange(2, 1000):
        plen = period_length(i)
        if plen > 0:
            lengths.append((i, plen))

    lengths.sort(key=operator.itemgetter(1))
    print lengths[-1]