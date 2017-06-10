import itertools
import numpy

s6 = {11, 18, 19, 20, 22, 25}
s7 = {20, 31, 38, 39, 40, 42, 45}
s7 = {19, 30, 37, 38, 39, 41, 44}
# s7 = {a, 11+a, 18+a, 19+a, 20+a, 22+a, 25+a}


def is_special(s):
    count = 0
    for a_size in range(1, len(s)):
        for a in itertools.combinations(s, a_size):
            print(a)
            remaining = s.difference(a)
            for b_size in range(1, len(remaining) + 1):
                for b in itertools.combinations(remaining, b_size):
                    print(a, b)
                    setstrings = {'a': str(a), 'b': str(b)}
                    if sum(a) == sum(b):
                        # print('sum({a}) == sum({b})'.format(**setstrings))
                        return False
                    if len(a) < len(b) and not sum(a) < sum(b):
                        # print('len({a}) < len({b}) and not sum({a}) < sum({b})'.format(**setstrings))
                        return False
                    if len(b) < len(a) and not sum(b) < sum(a):
                        # print('len({a}) < len({b}) and not sum({a}) < sum({b})'.format(**setstrings))
                        return False
                    count += 1
    print(count)
    return True


def set_string(set):
    return ''.join(map(str, sorted(list(set))))


print(s7, sum(s7), is_special(s7))

# s7 = [20, 31, 38, 39, 40, 42, 45]
# min = sum(s7) + 1
# for nd in numpy.ndindex(7, 7, 7, 7, 7, 7, 7):
#     s = {a + b - 3 for (a, b) in zip(s7, nd)}
#     if len(s) is not 7:
#         continue
#     if is_special(s):
#         if sum(s) < min:
#             min = sum(s)
#             print(set_string(s), min)

