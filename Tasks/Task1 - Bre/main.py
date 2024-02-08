import matplotlib.pyplot as plt
from BresenhamAlgorithm import bresenham_line


def draw_line(points):
    ## Draw using matplotlib
    pass


if __name__ == '__main__':

    points = bresenham_line(1, 1, 8, 4)
    draw_line(points)

    points = bresenham_line(1, 1, 4, 8)
    draw_line(points)

    '''
    points = bresenham_line(2, 1, 7, 7)
    draw_line(points)

    points = bresenham_line(1, 2, 7, 7)
    draw_line(points)
    '''
