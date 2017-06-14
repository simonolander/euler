def rec(b, w, b1, w1, memo):
    if (b, w, b1, w1) in memo:
        return memo[(b, w, b1, w1)]
    if b == 0 and w == 0:
        return 1

    ans = 0
    min_b2 = 1 if b > 0 else 0
    max_b2 = min(b, b1)
    for b2 in range(min_b2, max_b2 + 1):
        min_w2 = 1 if b2 == 0 else 0
        max_w2 = min(w, w1 if b2 == b1 else w)
        for w2 in range(min_w2, max_w2 + 1):
            ans += rec(b - b2, w - w2, b2, w2, memo)

    memo[b, w, b1, w1] = ans
    return ans


def n(b, w):
    memo = {}
    return sum(rec(b - b1, w - w1, b1, w1, memo) for b1 in range(1, b + 1) for w1 in range(0, w + 1) if b1 != 0 or w1 != 0)


print(n(60, 40))
