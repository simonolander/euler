

def nim_x(heaps, memo=None):
    if memo is None:
        memo = {}
    key = tuple(sorted(heaps))
    if key in memo:
        return memo[key]
    if all(heap == 0 for heap in heaps):
        return 0
    if sum(1 for heap in heaps if heap > 0) == 1:
        return 1
    ans = 0
    for index, heap in enumerate(heaps):
        for stones in range(1, heap + 1):
            if nim_x([heaps[i] - stones if i == index else heaps[i] for i in range(len(heaps))], memo) == 0:
                ans = 1
                break
        if ans == 1:
            break
    memo[key] = ans
    return ans


# memo = {}
# for n in range(1, 1000):
#     a, b, c = n, 2*n, 3*n
#     heaps = (a, b, c)
#     print(n, heaps, a ^ b ^ c, nim_x(heaps, memo))

print(sum(1 for n in range(1, 2**30 + 1) if n ^ (2*n) ^ (3*n) == 0))

