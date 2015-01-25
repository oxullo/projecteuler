#!/usr/bin/env python
# -*- coding: utf-8 -*-


import operator
import utils

primes = utils.get_primes()
primes_set = set(primes)


def find_max_addenda(top):
    sums = [primes[0]]

    for p in primes[1:]:
        last = p + sums[-1]
        # This is a dangerous assumption
        if last > top:
            break
        sums.append(last)

    addenda = []
    for i in xrange(len(sums) - 1, -1, -1):
        if sums[i] in primes_set:
            addenda.append((sums[i], i + 1))
            break
        else:
            for j in xrange(0, i):
                if (sums[i] - sums[j]) in primes_set:
                    addenda.append((sums[i] - sums[j], i-j))
                    break

    addenda.sort(key=operator.itemgetter(1))

    return addenda[-1]

def test():
    print find_max_addenda(100)
    print find_max_addenda(1000)

if __name__ == '__main__':
    test()
    print find_max_addenda(1E6)
