from math import gcd


def coprimes_brute(n):
    return sum(1 for x in range(1, n) for y in range(1, n - x + 1) if gcd(x, y) == 1)


def coprimes_euler(n):
    fs = [i for i in range(n + 1)]
    for p in range(2, n+1):
        if fs[p] == p:
            pp = 2*p
            while pp <= n:
                fs[pp], pp = p, pp + p
    coprimes = 0
    for k in range(1, n + 1):
        phi = 1
        while k != 1:
            p, q = fs[k], 0
            while k % p == 0: k, q = k // p, q + 1
            phi *= (p - 1) * pow(p, q-1)
        coprimes += phi
    coprimes -= 1
    return coprimes


def h(n, coprime_func):
    return 6 * (n * (n - 1)//2 - coprime_func(n) + n - 1)


print(h(5, coprimes_brute))
print(h(10, coprimes_brute))
print(h(1000, coprimes_brute))
print(h(5, coprimes_euler))
print(h(10, coprimes_euler))
print(h(1000, coprimes_euler))

print(h(10**8, coprimes_euler))
