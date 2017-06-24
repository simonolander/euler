from numpy import ndindex
from Primer import product


def row_naive(n):
    ans = 0
    for r1 in ndindex(*([3] * 1)):
        if n == 1:
            ans += 1
            continue

        for r2 in ndindex(*([3] * 3)):
            if any(a == b for a, b in zip(r1[0::2], r2[1::2])) or any(a == b for a, b in zip(r2, r2[1::])):
                continue
            if n == 2:
                ans += 1
                continue

            for r3 in ndindex(*([3] * 5)):
                if any(a == b for a, b in zip(r2[0::2], r3[1::2])) or any(a == b for a, b in zip(r3, r3[1::])):
                    continue
                if n == 3:
                    ans += 1
                    continue

                for r4 in ndindex(*([3] * 7)):
                    if any(a == b for a, b in zip(r3[0::2], r4[1::2])) or any(a == b for a, b in zip(r4, r4[1::])):
                        continue
                    if n == 4:
                        ans += 1
                        continue

                    for r5 in ndindex(*([3] * 9)):
                        if any(a == b for a, b in zip(r4[0::2], r5[1::2])) or any(a == b for a, b in zip(r5, r5[1::])):
                            continue
                        if n == 5:
                            ans += 1
                            continue
    return ans


def ps(a, b=-1, c=-1):
    return (p for p in range(3) if p != a and p != b and p != c)

def pss(gen):
    return ps(*gen)


def row_naive_faster(n):
    ans = 0
    for r1 in range(3):
        if n == 1:
            ans += 1
            continue

        for r22 in ps(r1):
            for r21 in ps(r22):
                for r23 in ps(r22):
                    if n == 2:
                        ans += 1
                        continue
                    for r32 in ps(r21):
                        for r34 in ps(r23):
                            for r31 in ps(r32):
                                for r33 in ps(r32, r34):
                                    for r35 in ps(r34):
                                        if n == 3:
                                            ans += 1
                                            continue
                                        for r42 in ps(r31):
                                            for r44 in ps(r33):
                                                for r46 in ps(r35):
                                                    for r41 in ps(r42):
                                                        for r43 in ps(r42, r44):
                                                            for r45 in ps(r44, r46):
                                                                for r47 in ps(r46):
                                                                    if n == 4:
                                                                        ans += 1
                                                                        continue

    return ans


def row_naive_rec(n, cn=1, prev=None):
    if n == 1:
        return 3
    if cn == 1:
        return sum(row_naive_rec(n, cn+1, [r1]) for r1 in range(3))
    else:
        ans = 0
        for upper in zip(*[ps(p) for p in prev]):
            middle_pss = [pss(tpl) for tpl in  zip(upper, upper[::1])]
            for lower in zip(ps(upper[0]), *middle_pss, ps(upper[-1])):
                if cn == n:
                    ans += 1
                    continue
                else:
                    ans += row_naive_rec(n, cn + 1, lower)
        return ans


def reduce_colors(colors):
    reduced = list(colors)
    if reduced[0] != 0:
        color0 = reduced[0]
        for i, color in enumerate(reduced):
            if color == color0:
                reduced[i] = 0
            elif color == 0:
                reduced[i] = color0
    for i in range(1, len(reduced)):
        color = reduced[i]
        if color == 0:
            continue
        elif color == 1:
            break
        else:
            for j in range(i, len(reduced)):
                if reduced[j] == 2:
                    reduced[j] = 1
                elif reduced[j] == 1:
                    reduced[j] = 2
            break
    return reduced


def row(n, prev=None):
    if n == 1:
        return 3 if prev is None else 2
    if prev is None:
        ans = 0
        for colors in ndindex(*([3] * (n - 1))):
            ans += 4 * product(2 if a == b else 1 for a, b in zip(colors, colors[1::])) * row(n-1, colors)
        return ans
    else:
        low_colors = [low_color for low_color in ndindex(*([3] * n)) if not any(a == b for a, b in zip(prev, low_color))]
        ans = 0
        for high_color in ndindex(*([3] * (n - 1))):
            for i, hc in enumerate(high_color):
                if hc == low_colors[i] or hc == low_colors[i+1]:
                    continue
                ans += row(n-1, high_color)
        return ans


print(row_naive_rec(1))
print(row_naive_rec(2))
print(row_naive_rec(3))
print(row_naive_rec(4))
print(row_naive_rec(5))



# print(reduce_colors([0, 1, 0, 0]))
# print(reduce_colors([0, 2, 0, 0]))
# print(reduce_colors([1, 0, 1, 1]))
# print(reduce_colors([1, 2, 1, 1]))
# print(reduce_colors([2, 0, 2, 2]))
# print(reduce_colors([2, 1, 2, 2]))
# print(reduce_colors([0, 1, 2]))
# print(reduce_colors([0, 2, 1]))
# print(reduce_colors([1, 0, 2]))
# print(reduce_colors([1, 2, 0]))
# print(reduce_colors([2, 0, 1]))
# print(reduce_colors([2, 1, 0]))
# print(reduce_colors([0, 0, 1, 0, 1]))
# print(reduce_colors([0, 0, 2, 0, 2]))
# print(reduce_colors([1, 1, 0, 1, 0]))
# print(reduce_colors([1, 1, 2, 1, 2]))
# print(reduce_colors([2, 2, 0, 2, 0]))
# print(reduce_colors([2, 2, 1, 2, 1]))
# print(reduce_colors([0, 0, 0, 0, 0, 0]))
# print(reduce_colors([1, 1, 1, 1, 1, 1]))
# print(reduce_colors([2, 2, 2, 2, 2, 2]))
