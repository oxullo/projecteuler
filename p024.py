#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

idx = int(1E06)
print ''.join([str(dgt) for dgt in list(itertools.permutations(xrange(10), 10))[idx-1]])