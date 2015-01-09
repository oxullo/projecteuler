#!/usr/bin/env python
# -*- coding: utf-8 -*-

def avalue(ch):
    assert isinstance(ch, str) and len(ch) == 1
    return ord(ch) - 64

def name_score(name):
    return sum([avalue(ch) for ch in name])

if __name__ == '__main__':
    f = open('p022_names.txt')
    snames = f.read()
    f.close()
    snames = '[%s]' % snames

    anames = sorted(eval(snames))

    total_score = 0
    for i, name in enumerate(anames):
        if name == 'COLIN':
            print i + 1
        total_score += (i+1) * name_score(name)

    print total_score