from Primer import Primer

max_n = 10**7

primer = Primer(max_n)

numbers = {}
for n in range(1, max_n + 1):
    primes = list(primer.factor_int(n, True))
    if len(primes) == 2:
        key = tuple(sorted(primes))
        if key not in numbers:
            numbers[key] = n
        elif numbers[key] < n:
            numbers[key] = n

# print(numbers)
print(sum(numbers.values()))
