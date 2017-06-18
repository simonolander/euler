

max_n = 10**17
fibs = [
    (1, 1),
    (2, 1),
]

while fibs[-1][0] < max_n:
    fibs.append(
        (fibs[-1][0] + fibs[-2][0], fibs[-1][1] + fibs[-2][1])
    )

print(fibs)

counts = [
    1,
    1
]

for i in range(2, len(fibs)):
    fib = fibs[i]
    counts.append(fib[1] + sum(counts[j] for j in range(i - 1)))

print(counts)


def count(n):
    smallest_over_index = 0
    smallest_over = fibs[smallest_over_index][0]
    while smallest_over < n:
        smallest_over_index += 1
        smallest_over = fibs[smallest_over_index][0]
    if smallest_over == n + 1:
        return sum(counts[i] for i in range(smallest_over_index))
    if smallest_over == n:
        return 1 + count(n - 1)
    smallest_under = fibs[smallest_over_index - 1][0]
    return sum(counts[i] for i in range(smallest_over_index - 1)) + count(n - smallest_under) + n - smallest_under

print(count(10**17) - 1)
