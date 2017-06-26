from numpy import ndindex

from Primer import totient_from_primes, prime_product
from sympy import Rational, oo, N

power = 3
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
sought = Rational(15499, 94744)
min_n = oo
for indices in ndindex(*([power] * len(primes))):
    indices = [i + 1 for i in indices]
    prime_powers = {p: e for p, e in zip(primes, indices)}
    n = prime_product(prime_powers)
    tot = totient_from_primes(prime_powers)
    rat = Rational(tot, n - 1)
    if rat < sought and n < min_n:
        min_n = n
        print(n, tot, rat, N(rat), prime_powers)
