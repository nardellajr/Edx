
"""
Recursive function, how it works. Each call to the function creates new scope, environment variables

1st:    4 * fact(3)
2nd:    3 * fact(2)
3rd:    2 * fact(1)
4th:    we return 1, to the calling, which is the 3rd

3rd:    2 * 1, return to calling
2nd:    3 * 2, return to calling
1st:    4 * 6

prints out 24

"""


def fact(n):
    """ Recursive method"""
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def fact_iter(n):
    """ Iteration method """
    prod = 1
    for i in range(1, n + 1):
        prod *= 1
    return prod


def power_iter_while(base, exp):
    """ Iteration method """
    count = 0
    var = 1
    while count < exp:
        count += 1
        var *= base

    print(var)
    return var


def recursive_power_function(base, exp):
    """ Recursive method"""
    if exp <= 0:
        return 1.0

    return base * recursive_power_function(base, exp - 1)


def power_iter_for(base, exp):
    """ Iteration method """
    var = 1
    for i in range(exp):
        var *= base

    print(var)
    return var


if __name__ == '__main__':
    # print(fact(4))
    # assert power_iter_while(2.5, 4) == 39.0625, "Should return 39.0625"
    # assert power_iter_for(2.5, 4) == 39.0625, "Should return 39.0625"

    # assert recursive_power_function(2.5, 4) == 39.0625, "Should return 39.0625"
    assert recursive_power_function(8.79, 0) == 1.0000, "Should return 1.0000"
