
def octant_one(centre_x: int = 0, centre_y: int = 0, R:int = 10) -> list[(int, int)]:

    x, y  = 0, R
    d = 3 - 2 * R
    points = []

    while x <= y:
        points.append((x, y))
        if d < 0:
            x = x + 1
            d = d + 4 * x + 6
        elif d >= 0:
            x = x + 1
            y =  y -  1
            d = d + 4 * (x - y) + 10

    return points


def quadrant_one(centre_x: int = 0, centre_y: int = 0, R:int = 10) -> list[(int, int)]:

    points_half = octant_one(centre_x, centre_y, R)
    points_otherhalf = [(y, x) for (x, y) in points_half]
    total_points = points_half + points_otherhalf
    return total_points


def draw_circle_breshenham(centre_x: int = 0, centre_y: int = 0, R:int = 10) -> list[(int, int)]:

    main_quad = quadrant_one(centre_x, centre_y, R)
    quad_2 = [(-x, y) for (x, y) in main_quad]
    quad_3 = [(x, -y) for (x, y) in main_quad]
    quad_4 = [(-x, -y) for (x, y) in main_quad]

    total_circle_points = main_quad + quad_2 + quad_3 + quad_4

    return sorted(total_circle_points)


if __name__ == '__main__':
    print(draw_circle_breshenham(0, 0, 8))



