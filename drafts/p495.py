#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://stackoverflow.com/questions/4568378/loop-through-different-sets-of-unique-permutations
def combinations(source, n):
  def combinations_helper(source, subsets, p=0, nonempty=0):
    if p == len(source):
      yield subsets[:]
    elif len(source) - p == len(subsets) - nonempty:
      empty = [subset for subset in subsets if not subset]
      for subset in empty:
        subset.append(source[p])
        for combination in combinations_helper(source, subsets, p+1, nonempty+1):
          yield combination
        subset.pop()
    else:
      for subset in subsets:
        newfilled = not subset
        subset.append(source[p])
        for combination in combinations_helper(source, subsets, p+1, nonempty+newfilled):
          yield combination
        subset.pop()

  assert len(source) >= n, "Not enough items"
  subsets = [[] for _ in xrange(n)]
  for combination in combinations_helper(source, subsets):
    yield combination

def factorize(n):
    fl = [1]
    d = 2
    while n >= d:
        if n % d == 0:
            fl.append(d)
            n /= d
        else:
            d += 1

    return fl


if __name__ == '__main__':
    import sys

    source = eval(sys.argv[1])
    p = int(sys.argv[2])

    allres = set()
    for combination in combinations(source, p):
        mul_vec = sorted([reduce(lambda x,y: x*y, block) for block in combination])
        if len(set(mul_vec)) == p:
            allres.add(tuple(mul_vec))
    
    print len(allres) % 1000000007
    
