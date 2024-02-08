import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from BresenhamAlgorithm import bresenham_line


def draw_pixels(points):
    fig, ax = plt.subplots()
    pixel_size = 1

    ax.set_xlim(0, max(points, key=lambda x: x[0])[0] + 1)
    ax.set_ylim(0, max(points, key=lambda x: x[1])[1] + 1)
    ax.set_xticks(range(max(points, key=lambda x: x[0])[0] + 2))
    ax.set_yticks(range(max(points, key=lambda x: x[1])[1] + 2))
    ax.grid(True, which='both')

    point1, point2, first_pass = None, None, True

    for point in points:
        if first_pass:
            point1 = point
            first_pass = False
        else:
            point2 = point
        square = Rectangle((point[0] - 1, point[1] - 1), pixel_size, pixel_size, facecolor="blue")
        ax.add_patch(square)

    ax.set_title(f"Line from {point1} to {point2}")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == '__main__':

    points = bresenham_line(1, 1, 8, 4)
    draw_pixels(points)

    points = bresenham_line(1, 1, 4, 8)
    draw_pixels(points)

    points = bresenham_line(2, 1, 7, 7)
    draw_pixels(points)

    points = bresenham_line(1, 2, 7, 7)
    draw_pixels(points)

