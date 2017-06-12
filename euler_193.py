import sympy


def square_less_naive(n):
    return len([i for i in range(1, n + 1) if not any(power for power in sympy.factorint(i).values() if power > 1)])


def square_less_naive_explicit(n):
    return [i for i in range(1, n + 1) if not any(power for power in sympy.factorint(i).values() if power > 1)]


def square_less(n):
    max_prime = sympy.floor(sympy.sqrt(n))
    used_primes = []
    ans = n
    for p in sympy.primerange(0, max_prime + 1):
        ans -= n // p**2
        for i0 in range(len(used_primes)):
            p0 = used_primes[i0]
            prod = p**2 * p0**2
            if prod > n:
                break
            ans += n // prod

            for i1 in range(i0 + 1, len(used_primes)):
                p1 = used_primes[i1]
                prod = p**2 * p0**2 * p1**2
                if prod > n:
                    break
                ans -= n // prod

                for i2 in range(i1 + 1, len(used_primes)):
                    p2 = used_primes[i2]
                    prod = p**2 * p0**2 * p1**2 * p2**2
                    if prod > n:
                        break
                    ans += n // prod

                    for i3 in range(i2 + 1, len(used_primes)):
                        p3 = used_primes[i3]
                        prod = p**2 * p0**2 * p1**2 * p2**2 * p3**2
                        if prod > n:
                            break
                        ans -= n // prod

                        for i4 in range(i3 + 1, len(used_primes)):
                            p4 = used_primes[i4]
                            prod = p**2 * p0**2 * p1**2 * p2**2 * p3**2 * p4**2
                            if prod > n:
                                break
                            ans += n // prod

                            for i5 in range(i4 + 1, len(used_primes)):
                                p5 = used_primes[i5]
                                prod = p**2 * p0**2 * p1**2 * p2**2 * p3**2 * p4**2 * p5**2
                                if prod > n:
                                    break
                                ans -= n // prod

                                for i6 in range(i5 + 1, len(used_primes)):
                                    p6 = used_primes[i6]
                                    prod = p**2 * p0**2 * p1**2 * p2**2 * p3**2 * p4**2 * p5**2 * p6**2
                                    if prod > n:
                                        break
                                    ans += n // prod

                                    for i7 in range(i6 + 1, len(used_primes)):
                                        p7 = used_primes[i7]
                                        prod = p**2 * p0**2 * p1**2 * p2**2 * p3**2 * p4**2 * p5**2 * p6**2 * p7**2
                                        if prod > n:
                                            break
                                        ans -= n // prod

                                        for i8 in range(i7 + 1, len(used_primes)):
                                            p8 = used_primes[i8]
                                            prod = p**2 * p0**2 * p1**2 * p2**2 * p3**2 * p4**2 * p5**2 * p6**2 * p7**2 * p8**2
                                            if prod > n:
                                                break
                                            ans += n // prod

                                            for i9 in range(i8 + 1, len(used_primes)):
                                                p9 = used_primes[i9]
                                                prod = p**2 * p0**2 * p1**2 * p2**2 * p3**2 * p4**2 * p5**2 * p6**2 * p7**2 * p8**2 * p9**2
                                                if prod > n:
                                                    break
                                                ans -= n // prod

        used_primes.append(p)
    return ans

n = 2**50

# print(square_less_naive(n))
print(square_less(n))
# print(21389533354941)
# print(sympy.factorint(n))
