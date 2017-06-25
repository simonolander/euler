from itertools import count

from sympy import factorint

from Primer import Primer
from Progress import Progress

primer = Primer(10**8)


def s_naive(n):
    fac = 1
    ans = 0
    while fac % n != 0:
        ans += 1
        fac *= ans
    return ans


def count_divs(n, p):
    ans = 0
    while n % p == 0:
        ans += 1
        n //= p
    return ans


def s(n):
    ans = 0
    for prime, power in primer.factor_counter(n).items():
        has = 0
        for i in count(1):
            has += count_divs(i, prime) + 1
            if has >= power:
                ans = max(ans, i*prime)
                break
    return ans

# for i in range(1, 100):
#     print(i, s_naive(i), s(i))
#
# assert s_naive(10) == 5
# assert s_naive(25) == 10
# assert s_naive(10**8) == 35
# assert s(10) == 5
# assert s(25) == 10
# assert s(10**8) == 35

progress = Progress()

ans = 0
for i in range(2, 10**8 + 1):
    ans += s(i)
    progress.print_progress("%s: %s" % (i, ans))

print()
print(ans)
