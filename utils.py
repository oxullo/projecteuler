#!/usr/bin/env python
# -*- coding: utf-8 -*-

def num_to_digits(n):
	return [int(ns) for ns in str(n)]

def digits_to_num(digits):
	return int(''.join([str(d) for d in digits]))
