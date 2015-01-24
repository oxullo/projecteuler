#!/usr/bin/env python
# -*- coding: utf-8 -*-

coins = [100, 50, 20, 10, 5, 2, 1]

def test(coeff):
    return sum(map(lambda a: a[0]*a[1], zip(coins, coeff))) == 200

if __name__ == '__main__':
    successes = 0
    coeff = [0] * len(coins)

    run = True
    while run:
        if test(coeff):
            print coeff
            successes += 1

        for i in xrange(len(coins)):
            coeff[i] += 1
            if coins[i] * coeff[i] > 200:
                coeff[i] = 0
                if i == len(coins) - 1:
                    run = False
            else:
                break

    # Add the sole 200p to the number of results
    print successes + 1
