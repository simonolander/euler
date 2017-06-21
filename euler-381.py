import sympy

from Primer import mod_inv
from Progress import Progress

progress = Progress()

max_p = 10**8

ans = 0
for p in sympy.primerange(5, 10**8):
    # p1 = p - 1
    # p2 = 1
    # p3 = p // 2
    # p4 = pow(6, p - 2, p)
    # p5 = pow(p - 24, p - 2, p)

    p1 = mod_inv(-1,                                         p)
    p2 = mod_inv(-1 * (p - 1),                               p)
    p3 = mod_inv(-1 * (p - 1) * (p - 2),                     p)
    p4 = mod_inv(-1 * (p - 1) * (p - 2) * (p - 3),           p)
    p5 = mod_inv(-1 * (p - 1) * (p - 2) * (p - 3) * (p - 4), p)
    ans += (p1 + p2 + p3 + p4 + p5) % p
    progress.print_progress('Prime: %d   Sum: %d' % (p, ans))

print()
print(ans)
