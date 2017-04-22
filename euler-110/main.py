from numpy import ndindex


def count_solutions(es):
    ans = 1
    for e in es:
        ans *= 2*e + 1
    return ans // 2 + 1


def product(f):
    ans = 1
    for p, e in f.items():
        ans *= p**e
    return ans

min = 9350130049860600
factorization = {
    2: 3,
    3: 3,
    5: 2,
    7: 2,
    11: 1,
    13: 1,
    17: 1,
    19: 1,
    23: 1,
    29: 1,
    31: 1,
    37: 1,
    41: 0,
    43: 0,
    47: 0
}

print(product(factorization))
print(count_solutions(factorization.values()))
