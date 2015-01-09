#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibo(n - 1) +  fibo(n - 2)

allsum = 0
i = 1
while True:
    f = fibo(i)
    if f >= 4E06:
        break
    elif f % 2 == 0:
        allsum += f
    i += 1

print allsum