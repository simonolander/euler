import itertools
import numpy
import math


def ncr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def subset_pairs(s):
    for a_size in range(1, len(s)):
        for a in itertools.combinations(s, a_size):
            remaining = s.difference(a)
            for b_size in range(1, len(remaining) + 1):
                for b in itertools.combinations(remaining, b_size):
                    yield a, b



[11, 18, 19, 20, 22, 25]
