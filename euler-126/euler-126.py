from itertools import count


def layer(x, y, z, n):
    return 2*(x*y + y*z + x*z) + 4*(x + y + z + n - 2) * (n - 1)

print(layer(3, 2, 1, 1))  # 22
print(layer(3, 2, 1, 2))  # 46
print(layer(3, 2, 1, 3))  # 78
print(layer(3, 2, 1, 4))  # 118
print(layer(5, 1, 1, 1))  # 22

limit = 30000
memo = {}

for x in count(1):
    if layer(x, x, x, 1) > limit:
        break
    for y in count(x):
        if layer(x, y, y, 1) > limit:
            break
        for z in count(y):
            if layer(x, y, z, 1) > limit:
                break
            for n in count(1):
                l = layer(x, y, z, n)
                if l > limit:
                    break
                if l not in memo:
                    memo[l] = [(x, y, z, n)]
                else:
                    memo[l].append((x, y, z, n))

search = 1000
smallest = None
lst = None
for layer_size, count in memo.items():
    if len(count) == search:
        if smallest is None or layer_size < smallest:
            smallest = layer_size
            lst = count

print(smallest, lst)
