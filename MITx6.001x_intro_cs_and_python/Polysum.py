import math
# import polygons

def polysum(numberofsides, lengthofside):
    """
    Sums the area and square of the perimeter of the regular polygon.
    :param numberofsides: number of sides
    :param lengthofside: length of side
    :return: returns the sum, rounded to 4 decimal places
    """

    perimeter = (numberofsides * lengthofside)**2
    polyarea = (0.25*numberofsides*(lengthofside**2)) / (math.tan(math.pi/numberofsides))

    polysum = perimeter + polyarea

    print(polysum)
    print("This returns a string, '{0:.4f}'.format(polysum)")
    print("{0:.4f}".format(polysum))
    print(type("{0:.4f}".format(polysum)))

    print("This returns a float, round(polysum, 4)")
    print(round(polysum, 4))
    print(type(round(polysum, 4)))
    return round(polysum, 4)


if __name__ == '__main__':
    assert polysum(77, 92) == 54174280.595
    # assert polygons.polysum(77, 92) == 54174280.595
    # polysum(5, 4)