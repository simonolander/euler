from sympy import divisors
from sympy.ntheory import isprime

count = 0
for n in range(100_000_000 + 1):
    special = True
    for divisor in divisors(n, True):
        if not isprime(divisor + n // divisor):
            special = False
            break
    if special:
        count += n
        print(n)

print(count)
