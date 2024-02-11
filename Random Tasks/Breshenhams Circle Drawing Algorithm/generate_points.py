
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


if __name__ == '__main__':
    print(octant_one(0, 0, 20))



