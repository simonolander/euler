from sympy.ntheory import factorint
from itertools import count

# 1/x + 1/y = 1/n
# n = xy / ( x + y )
# n = p0^e0*p1^e1...
# f(p^k) = 2*k + 1


def count_solutions(n):
    ans = 1
    for p, e in factorint(n).items():
        ans *= 2*e + 1
    return ans // 2 + 1


for n in count(1):
    if count_solutions(n) > 1000:
        print(n)
        break
