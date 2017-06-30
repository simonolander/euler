"""
sum(2 * 2**i for i in range(i)) == 2 * (2**i - 1) == n
i == log_2(n // 2 + 1)
"""
from math import ceil, log

import time


def count_ways(n, current_power=None, memo=None):
    if memo is None:
        memo = {}
    if current_power is None:
        current_power = ceil(log(n // 2 + 1, 2))
    key = (n, current_power)
    if key in memo:
        return memo[key]

    current_term = 2 ** current_power
    max_available = 2 * (2 ** (current_power + 1) - 1)
    assert n <= max_available
    next_max_available = 2 * (2 ** current_power - 1)

    ans = 0
    if n >= 2 * current_term:
        if n == 2 * current_term:
            ans += 1
        else:
            ans += count_ways(n - 2 * current_term, current_power - 1, memo)
    if n >= current_term:
        if n == current_term:
            ans += 1
        elif n - current_term <= next_max_available:
            ans += count_ways(n - current_term, current_power - 1, memo)
    if n <= next_max_available:
        ans += count_ways(n, current_power - 1, memo)

    memo[key] = ans
    return ans


t0 = time.time()
print(count_ways(10 ** 25))
t1 = time.time()

print('Total time:', (t1 - t0) * 1000, 'ms')
