#!/usr/bin/env python
# -*- coding: utf-8 -*-

units = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tenths = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

def toliteral(n):
    if n in units.keys():
        return units[n]
    elif n < 100:
        if n % 10 == 0:
            return tenths[n / 10]
        else:
            return '%s%s' % (tenths[n / 10], units[n % 10])
    elif n < 1000:
        if n % 100 == 0:
            return '%s hundred' % units[n / 100]
        else:
            return '%s hundred and %s' % (units[n / 100], toliteral(n % 100))
    elif n == 1000:
        return 'one thousand'

tot = 0
for i in xrange(1, 1001):
    print toliteral(i).replace(' ', '')
    tot += len(toliteral(i).replace(' ', ''))

print tot

