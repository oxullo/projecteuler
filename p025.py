#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fn = Fn-1 + Fn-2
# F1 = 1, F2 = 1

import calc

def find_brute(target_len):
    n = 3
    fn = 2
    fn2 = 1
    fn1 = 1

    while True:
        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn
        if len(str(fn)) == target_len:
            return n
        n += 1

def step_to_fib_len(n):
    return len(str(calc.fibonacci_iter(n)))

def find_guess(target_len):
    step_low = target_len / 4
    step_high = 3 * target_len / 4
    p1 = calc.Vec2D(step_to_fib_len(step_low), step_low)
    p2 = calc.Vec2D(step_to_fib_len(step_high), step_high)

    m = float(p2.y - p1.y) / (p2.x - p1.x)
    q = p1.y - p1.x * m

    start_guessed = int(m * target_len + q)

    tlen = step_to_fib_len(start_guessed)

    if tlen > target_len:
        rng = xrange(start_guessed, 0, -1)
    else:
        rng = xrange(start_guessed, start_guessed * 2)

    for i in rng:
        if step_to_fib_len(i) == target_len:
            return i

    return None

if __name__ == '__main__':
    print find_brute(1000)
    print find_guess(1000)

    import timeit
    TARGET = 1000
    for f in ('find_brute', 'find_guess'):
        statement = '%s(%s)' % (f, TARGET)
        print statement
        t = timeit.timeit(statement, setup='from __main__ import %s' % f, number=5)
        print 'Time: %.2f' % t
