import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def dda_line(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))

    x_increment = dx / float(steps)
    y_increment = dy / float(steps)

    x = x0
    y = y0
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points


def draw_pixels(points, point1, point2):
    fig, ax = plt.subplots()
    pixel_size = 1 

    ax.set_xlim(0, max(points, key=lambda x: x[0])[0] + 1)
    ax.set_ylim(0, max(points, key=lambda x: x[1])[1] + 1)
    ax.set_xticks(range(max(points, key=lambda x: x[0])[0] + 2))
    ax.set_yticks(range(max(points, key=lambda x: x[1])[1] + 2))
    ax.grid(True, which='both')

    for point in points:
        square = Rectangle((point[0] - 1, point[1] - 1), 
                           pixel_size, pixel_size, 
                           facecolor="blue")
        ax.add_patch(square)

    ax.set_title(f"DDA Line from {point1} to {point2}")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == '__main__':
    point1 = (1, 1)
    point2 = (8, 4)
    points = dda_line(*point1, *point2)
    draw_pixels(points, point1, point2)
