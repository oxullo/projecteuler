#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fn = Fn-1 + Fn-2
# F1 = 1, F2 = 1

n = 3
fn = 2
fn2 = 1
fn1 = 1

while True:
    fn = fn1 + fn2
    fn2 = fn1
    fn1 = fn
    if len(str(fn)) == 1000:
        print n, len(str(fn))
        break
    n += 1
