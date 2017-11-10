

def triangle_sum(tri, r, c, h, memo):
    if (r, c, h) in memo:
        return memo[(r, c, h)]
    ans = tri[r][c]
    if h > 0:
        ans += triangle_sum(tri, r + 1, c, h - 1, memo)
        ans += triangle_sum(tri, r + 1, c + 1, h - 1, memo)
    if h > 1:
        ans -= triangle_sum(tri, r + 2, c + 1, h - 2, memo)

    memo[(r, c, h)] = ans
    return ans


def min_triangle_sum(tri):
    memo = {}
    minimum = tri[0][0]
    for r in range(len(tri)):
        for c in range(r + 1):
            print(r, c)
            for h in range(len(tri) - r):
                print(r, c, h)
                s = triangle_sum(tri, r, c, h, memo)
                if s < minimum:
                    minimum = s
                    print(r, c, h, ':', minimum)
    return minimum


def min_triangle_sum_2(tri):
    memo = {}
    for r in range(len(tri)):
        s = 0
        memo[(r, 0)] = 0
        for c in range(0, r + 1):
            s += tri[r][c]
            memo[(r, c+1)] = s

    minimum = tri[0][0]
    for r in range(len(tri)):
        for c in range(r + 1):
            minimum_2 = 0
            for h in range(len(tri) - r):
                minimum_2 += memo[(r + h, c + h + 1)] - memo[(r + h, c)]
                if minimum_2 < minimum:
                    minimum = minimum_2
                    print(r, c, h, ':', minimum)
    return minimum


def make_triangle(n=1000):
    triangle = [[0] * k for k in range(1, n + 1)]
    r = 0
    c = 0
    t = 0
    for k in range(n * (n + 1) // 2):
        t = (615949 * t + 797807) % 2**20
        triangle[r][c] = t - 2**19
        c += 1
        if c == len(triangle[r]):
            r += 1
            c = 0
    return triangle


triangle = [
    [ 15],
    [-14, - 7],
    [ 20, -13, - 5],
    [- 3,   8,  23, -26],
    [  1, - 4, - 5, -18,   5],
    [-16,  31,   2,   9,  28,   3],
]

triangle = make_triangle()
print(min_triangle_sum_2(triangle))
