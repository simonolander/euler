import itertools


def square_laminae(n):
    max_side = n // 4 + 1

    count = 0
    for side in range(3, max_side + 1):
        squares_used = side * 4 + 4
        count += 1
        for layer in itertools.count(1):
            layer_side = side - layer * 2
            if layer_side < 1:
                break
            squares_used += layer_side * 4 + 4
            if squares_used > n:
                break
            count += 1

    return count


print(square_laminae(1000000))
