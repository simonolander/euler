from collections import Counter


def product(gen):
    ans = 1
    for g in gen:
        ans *= g
    return ans


class Primer:
    def __init__(self, max_n):
        self.max_n = max_n
        self.factors = list(range(max_n + 1))
        for n in range(2, len(self.factors)):
            p = self.factors[n]
            if n == p:
                for i in range(2, (len(self.factors) + 1) // p):
                    self.factors[i*p] = p
        self.factors[0] = -1
        self.factors[1] = -1

    def __len__(self):
        return len(self.factors)

    def primes(self):
        return (p for i, p in enumerate(self.factors) if i == p)

    def factor_int(self, n, distinct=False):
        while n != 1:
            p = self.factors[n]
            while n % p == 0:
                yield p
                n //= p
                while distinct and n % p == 0:
                    n //= p

    def factor_counter(self, n):
        return Counter(self.factor_int(n))

    def totient(self, n):
        ans = n
        for p in self.factor_int(n, True):
            ans *= p - 1
            ans //= p
        return ans

    def count_divisors(self, n):
        factors = self.factor_counter(n)
        return product(p + 1 for p in factors.values())

if __name__ == '__main__':
    primer = Primer(1000)
    print('Distinct factors of 1000:', list(primer.factor_int(1000, True)))
    print('Factors and power for 1000:', primer.factor_counter(1000))
    print('Euler totient for 14:', primer.totient(14))
    print('Euler totient for 15:', primer.totient(15))
    print('Divisor count for 14:', primer.count_divisors(14))
    print('Divisor count for 15:', primer.count_divisors(15))
    print('Divisor count for 16:', primer.count_divisors(16))
