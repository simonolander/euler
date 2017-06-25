import matplotlib.pyplot as plt


def plot_grid(width, height):
    regular_color = 'black'
    cross_color = 'blue'
    for i in range(height + 1):
        plt.plot([0, width], [i, i], color=regular_color)
    for i in range(width + 1):
        plt.plot([i, i], [0, height], color=regular_color)

    side = width + height - 2
    cx, cy = width / 2, height / 2
    sx, sy = cx - side / 2, cy
    for i in range(side + 1):
        plt.plot([sx + i / 2, cx + i / 2], [sy + i / 2, cy - side / 2 + i / 2], color=cross_color)
        plt.plot([sx + i / 2, cx + i / 2], [cy - i / 2, cy + side / 2 - i / 2], color=cross_color)

    for x in range(side):
        for y in range(side):
            pos_x = sx + 1 / 2 + x/2 + y / 2
            pos_y = sy + y/2 - x / 2
            scatter_color = 'green' if in_bounds(x, y, width, height) else 'red'
            plt.scatter(pos_x, pos_y, color=scatter_color)

    plt.axis('scaled')
    plt.show()


def regular_rectangles(width, height):
    ans = 0
    for x in range(width):
        for y in range(height):
            for w in range(1, width - x + 1):
                for h in range(1, height - y + 1):
                    ans += 1
    return ans


def in_bounds(x, y, width, height):
    side = width + height - 2
    if x + y < height - 2:
        return False
    if y - x > (side - 1) - (width - 2):
        return False
    if x + y > (side - 1) * 2 - (height - 2):
        return False
    if x - y > (side - 1) - (width - 2):
        return False
    return True


def cross_rectangles(width, height):
    side = width + height - 2
    ans = 0
    for x in range(side):
        for y in range(side):
            if not in_bounds(x, y, width, height):
                continue
            for w in range(0, side):
                for h in range(0, side):
                    if not in_bounds(x, y + h, width, height):
                        continue
                    if not in_bounds(x + w, y + h, width, height):
                        continue
                    if not in_bounds(x + w, y, width, height):
                        continue
                    ans += 1
    return ans


def rectangles(width, height):
    return regular_rectangles(width, height) + cross_rectangles(width, height)


size = (47, 43)
ans = 0
for y in range(1, size[1] + 1):
    for x in range(1, size[0] + 1):
        n = rectangles(x, y)
        print((x, y), n)
        ans += n
print(ans)
