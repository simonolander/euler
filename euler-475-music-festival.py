from Primer import fac


def f(n):
    divs = fac(3 * n) // fac(3) ** n // fac(n)
    ways = 24**2
    ans = ways**divs
    return ans % 1_000_000_007, ans


print(f(1))
print(f(2))
