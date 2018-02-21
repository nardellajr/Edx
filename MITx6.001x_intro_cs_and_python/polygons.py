import math


def polysum(n, s):
    """
    Sums the area and square of the perimeter of the regular polygon.
    :param n: number of sides
    :param s: length of side
    :return: returns the sum, rounded to 4 decimal places
    """

    perimeter = (n * s)**2
    polyarea = (0.25*n*(s**2)) / (math.tan(math.pi / n))
    polysum = perimeter + polyarea

    return round(polysum, 4)

