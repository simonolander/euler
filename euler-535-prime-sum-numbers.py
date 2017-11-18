from Primer import primer_10_000_000
from math import log, sqrt

print('Initializing primer...')
primer = primer_10_000_000()
print('...done')


def p(n, k, memo=None):
    global primer
    if memo is None:
        memo = {}
    if k < 1:
        return 0
    if (n, k) in memo:
        return memo[(n, k)]
    if k == 1:
        ans = 1 if primer.is_prime(n) else 0
    else:
        ans = 0
        for prime in primer.primes():
            if prime > n:
                break
            if p(n - prime, k - 1, memo) == 1:
                ans = 1
                break
    memo[(n, k)] = ans
    return ans


def s(n, memo=None, p_memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if p_memo is None:
        p_memo = {}
    if n < 1:
        return 0
    ans = s(n-1, p_memo, memo)
    for k in range(1, n // 2 + 2):
        ans += p(n, k, p_memo)
    memo[n] = ans
    return ans


print('p(10, 2):', p(10, 2), 1)
print('p(11, 2):', p(11, 2), 0)
print('p(11, 1):', p(11, 1), 1)

print('s(10):', s(10), 20)
print('s(100):', s(100), 2402)
# print('s(1000):', s(1000), 248838)

memo = {}
p_memo = {}
last = 0
for i in range(701408734):
    prime_count = 0 if i < 3 else int(i/log(i) - 1)
    actual = s(i, memo, p_memo)
    guess = last + i // 2 - 1
    # print(i, s(i, memo, p_memo), s(i, memo, p_memo) - s(i - 1, memo, p_memo), i // 2 - 1)
    print(i, actual, guess, actual - guess + prime_count, prime_count)
    last = guess
