from collections import Counter

from Progress import Progress


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inv(n, mod):
    g, x, y = egcd(n % mod, mod)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % mod


def product(gen, mod=None):
    ans = 1
    for g in gen:
        ans *= g
        if mod:
            ans %= mod
    return ans


def factorial(n, mod=None):
    return product(range(1, n + 1), mod)


class Primer:
    def __init__(self, max_n, verbose=False):
        self._max_n = max_n
        init_progress = Progress(title='Initializing Primer(%d): ' % max_n)
        if verbose:
            init_progress.print_progress('Creating factor list...')
        self._factors = list(range(max_n + 1))
        self._primes = []
        for n in range(2, len(self._factors)):
            p = self._factors[n]
            if n == p:
                self._primes.append(n)
                if verbose:
                    init_progress.print_progress(n)
                pp = p*2
                while pp < len(self._factors):
                    self._factors[pp] = p
                    pp += p

        self._factors[0] = -1
        self._factors[1] = -1
        if verbose:
            print('Primer(%d) initialized.' % max_n)

    def __len__(self):
        return len(self._factors)

    def primes(self):
        return self._primes

    def factor_int(self, n, distinct=False):
        while n != 1:
            p = self._factors[n]
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
