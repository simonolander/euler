divisors = [1 for i in range(10**7 + 1)]
divisors[0] = 0
for d in range(2, len(divisors)):
    dd = d
    while dd < len(divisors):
        divisors[dd] += 1
        dd += d

count = 0
for a, b in zip(divisors, divisors[1::]):
    if a == b:
        count += 1
print(count)
