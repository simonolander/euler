from numpy import ndindex

print("Initializing array...")
factors = [n for n in range(100_000_000 + 2)]
print("Computing primes...")
for n in range(2, len(factors)):
    p = factors[n]
    if p == n:
        print(p)
        for i in range(2, len(factors) // p):
            factors[i * p] = p


def product(gen):
    ans = 1
    for g in gen:
        ans *= g
    return ans


def is_prime(n):
    return factors[n] == n


def factor_int(n):
    while n != 1:
        p = factors[n]
        while n % p == 0:
            yield p
            n //= p


def divisors(n):
    prime_powers = {}
    for p in factor_int(n):
        if p in prime_powers:
            prime_powers[p] += 1
        else:
            prime_powers[p] = 2
    primes = prime_powers.keys()
    powers = prime_powers.values()
    for indices in ndindex(*powers):
        yield product([p ** index for (p, index) in zip(primes, indices)])


print("Counting special numbers...")
count = 0
for n in range(1, 100_000_000 + 1):
    special = True
    for divisor in divisors(n):
        if not is_prime(divisor + n // divisor):
            special = False
            break
    if special:
        count += n
        print(n)

print(count)
