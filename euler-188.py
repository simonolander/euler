from sympy.ntheory import totient
from sys import setrecursionlimit


setrecursionlimit(2000)


def tetrate_mod_n(base, exponent, modulo):
    if exponent == 2:
        return pow(base, base, modulo)

    tot = totient(modulo)
    e = tetrate_mod_n(base, exponent - 1, tot)
    return pow(base, e, modulo)


print(tetrate_mod_n(1777, 1855, 10**8))
