from tabulate import tabulate
from sympy.ntheory import primetest


def primes(n):
    for i in range(10**(n-1), 10**n):
        if primetest.isprime(i):
            yield i


def metrics(numbers):
    ans = {d: {'m': 0, 'n': 0, 's': 0} for d in range(10)}
    last = 0
    with open('primes.txt', 'a') as fp:
        for number in numbers:
            fp.write('%d\n' % number)
            if number // 10**7 > last:
                last = number // 10**7
                print(last)
            c = {d: 0 for d in range(10)}
            temp = number
            while temp:
                c[temp % 10] += 1
                temp //= 10

            for d in range(10):
                if ans[d]['m'] < c[d]:
                    ans[d]['m'] = c[d]
                    ans[d]['n'] = 1
                    ans[d]['s'] = number
                elif ans[d]['m'] == c[d]:
                    ans[d]['n'] += 1
                    ans[d]['s'] += number

    return [
        [d, o['m'], o['n'], o['s']] for d, o in ans.items()
    ]

n = 10
print("Computing primes...")
pr = primes(n)
print("Computing metrics...")
met = metrics(pr)
print("Tabulating...")
print()
table = tabulate(met, ['Digit, d', 'M(%d, d)' % n, 'N(%d, d)' % n, 'S(%d, d)' % n])
print(table)
print()
print("Sum: ", sum([row[3] for row in met]))
