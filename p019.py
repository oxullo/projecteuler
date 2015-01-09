#!/usr/bin/env python
# -*- coding: utf-8 -*-

DIM = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def isleap(year):
    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

sundays = 0
year = 1900
month = 1
day = 1
dow = 1

while True:
    day += 1
    dow += 1
    if dow > 7:
        dow = 1

    if month == 2 and isleap(year):
        dim = 29
    else:
        dim = DIM[month]

    if day > dim:
        day = 1
        month +=1

    if month > 12:
        month = 1
        day = 1
        year += 1
        print 'New year, %d %s' % (year, isleap(year))
        if year == 2001:
            break

    if year >= 1901 and dow == 7 and day == 1:
        print 'Sunday on first!'
        sundays += 1

    print '%d/%d/%d (%d) - %d' % (day, month, year, dow, sundays)

print sundays
