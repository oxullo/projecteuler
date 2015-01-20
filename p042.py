#!/usr/bin/env python
# -*- coding: utf-8 -*-

words = [w for w in eval('['+open('p042_words.txt').read()+']')]

def word_weight(word):
	total = 0
	for ch in word:
		total += ord(ch) - 64

	return total

def triangle_number(n):
	return n * (n + 1) / 2

def test():
	print word_weight('SKY')
	print [triangle_number(n) for n in xrange(1, 11)]


if __name__ == '__main__':
	all_weights = [word_weight(w) for w in words]

	max_weight = max(all_weights)

	all_tri_numbers = []
	r = 0
	n = 1
	while r < max_weight:
		r = triangle_number(n)
		all_tri_numbers.append(r)
		n += 1

	totals = 0
	for weight in all_weights:
		if weight in all_tri_numbers:
			totals += 1

	print totals