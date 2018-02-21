

def evalquadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    """

    result = a*(x**2) + b*x + c

    print(result)
    return result


def a(x):
    return x + 1


def b(x):
    return x + 1.0


def c(x, y):
    return x + y


def f(x, y):
    x + y -2


def d(x, y):
    """
    :param x: Can be of any type
    :param y: Can be of any type
    :return: ??
    """
    return x > y


def e(x, y, z):
    """
    :param x: Can be of any type
    :param y: Can be of any type
    :param z: Can be of any type
    :return:
    """
    return x >= y and x <= z
    # Could also be written as     return y <= x <= z


if __name__ == '__main__':
    # evalquadratic(-1.64, 3.12, -5.12, 7.98)
    # print(f)  # returns the function f

    # d("apple", 11.1)  # TypeError: '>' not supported between instances of 'str' and 'float'

    value = e(a(3), b(4), c(3, 4))

    print(type(value))
    print(value)

