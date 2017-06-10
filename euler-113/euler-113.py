from tabulate import tabulate
from sys import setrecursionlimit


setrecursionlimit(10000)


def get_digits(n, radix=10):
    ans = []
    while n > 0:
        ans.append(n % radix)
        n //= radix
    ans.reverse()
    return ans


def is_ascending(n):
    digits = get_digits(n)
    for d0, d1 in zip(digits, digits[1:]):
        if d0 > d1:
            return False
    return True


def is_descending(n):
    digits = get_digits(n)
    for d0, d1 in zip(digits, digits[1:]):
        if d0 < d1:
            return False
    return True


def is_bouncy(n):
    return not is_ascending(n) and not is_descending(n)


def count_naive(m, start=1):
    return len([n for n in range(start, m) if not is_bouncy(n)])


def print_naive(m, start=1):
    asc = len([n for n in range(start, m) if is_ascending(n)])
    desc = len([n for n in range(start, m) if is_descending(n)])
    non_bouncy = len([n for n in range(start, m) if not is_bouncy(n)])
    print(tabulate([[
        m - start,
        asc,
        desc,
        desc - asc,
        non_bouncy
    ]], ['Total', 'Ascending', 'Descending', 'Desc - Asc', 'Not bouncy']))


def print_naive_complete(m, start=1):
    print(tabulate([[
                        n,
                        is_ascending(n),
                        is_descending(n),
                        not is_bouncy(n)
                    ] for n in range(start, m)], ['n', 'Ascending', 'Descending', 'Not bouncy']))


def count_descending_naive(m, start=1):
    return len([n for n in range(start, m) if is_descending(n)])


def count_ascending_naive(m, start=1):
    return len([n for n in range(start, m) if is_ascending(n)])


def count_descending_clever_recursive(current_digit, remaining_digits, memo=None):
    if memo is None:
        memo = {}
    if (current_digit, remaining_digits) in memo:
        return memo[(current_digit, remaining_digits)]
    if current_digit is 0:
        ans = 1
    elif remaining_digits is 0:
        ans = 1
    else:
        ans = sum([count_descending_clever_recursive(next_digit, remaining_digits - 1, memo) for next_digit in range(current_digit + 1)])
    memo[(current_digit, remaining_digits)] = ans
    return ans


def count_ascending_clever_recursive(current_digit, remaining_digits, memo=None):
    if memo is None:
        memo = {}
    if (current_digit, remaining_digits) in memo:
        return memo[(current_digit, remaining_digits)]
    if current_digit is 9:
        ans = 1
    elif remaining_digits is 0:
        ans = 1
    else:
        ans = sum([count_ascending_clever_recursive(next_digit, remaining_digits - 1, memo) for next_digit in range(current_digit, 10)])
    memo[(current_digit, remaining_digits)] = ans
    return ans


def count_descending_clever(digits):
    return sum(count_descending_clever_recursive(9, r) for r in range(1, digits + 1)) - digits


def count_ascending_clever(digits):
    return sum(count_ascending_clever_recursive(1, r) for r in range(1, digits + 1))


def count_non_bouncy_clever(digits):
    return count_ascending_clever(digits) + count_descending_clever(digits) - digits * 9


# print_naive(10000)
# print(count_descending_naive(1000, 1))
# print(count_descending_clever(3))

# print(count_ascending_naive(100000, 1))
# print(count_ascending_clever(5))

# print_naive(1000000)

print(count_non_bouncy_clever(1000))
