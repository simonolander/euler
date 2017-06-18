import numpy as np
from tabulate import tabulate


np.set_printoptions(linewidth=400, threshold=100000)


def product(gen):
    ans = 1
    for g in gen:
        ans *= g + 1
    return ans


def count_divs_pow(p):
    if p == 0 or p == 1:
        return 0
    else:
        full_size = 7**(p-1) * (7**(p-1) - 1) // 2
        fulls = 21 * full_size
        smalls = 28 * count_divs_pow(p-1)
        return fulls + smalls


def base7(n):
    ans = []
    while n > 0:
        ans.append(n % 7)
        n //= 7
    return ans


def num_not_divisible(i):
    return product(base7(i))


def pascal(n):
    pascal = np.zeros((n, n))
    for x, y in np.ndindex(n, n):
        if x == 0 or y == 0:
            pascal[x, y] = 1
        else:
            pascal[x, y] = (pascal[x-1, y] + pascal[x, y-1]) % 7
    print(pascal)


def pascal_zeroes(n):
    row = [1]
    zeroes = [[0, 0, 0]]
    for i in range(1, n):
        row = [1] + [(a + b) % 7 for a, b in zip(row, row[1::])] + [1]
        count = len([r for r in row if r == 0])
        zeroes.append([i, count, count - zeroes[i-1][1]])
    return tabulate(zeroes, ['Row index', 'Count Zeros'])


def c(n):
    ans = 0
    for i in range(n):
        ans += num_not_divisible(i)
        if i % 1000000 == 0:
            print(i, ans)
    return ans

print(c(1000000000))
