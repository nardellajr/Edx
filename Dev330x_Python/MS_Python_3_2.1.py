
def booleanoperators():

    # not operator
    print("not True =", not True)
    print("not False =", not False)

    # and operator
    print("False and False =", False and False)
    print("False and True =", False and True)
    print("True and False =", True and False)
    print("True and True =", True and True)  # only that evaluates to True

    colette_ticket = True
    alton_ticket = True
    print("Alton and not Colette =", alton_ticket and not colette_ticket)  #

    colette_ticket = False
    print("Alton and not Colette =", alton_ticket and not colette_ticket)  #


def combiningcomparisons():
    # number outside a range
    x = 11
    print(x < 10 or x > 20)
    x = 50
    print(x < 10 or x > 20)

    # Testing if x is a positive and odd number
    x = -11
    print("x = -11, x > 0 and x % 2 != 0", x > 0 and x % 2 != 0)
    x = 9
    print("x = 9, x > 0 and x % 2 != 0", x > 0 and x % 2 != 0)

    # [ ] Write an expression to test if x is an even number outside the range [-100, 100]
    x = 104  # (True)
    print((x < -100 or x > 100) and x % 2 == 0)

    x = 115  # (False)
    print((x < -100 or x > 100) and x % 2 == 0)

    x = -106 # (True)
    print((x < -100 or x > 100) and x % 2 == 0)

    x = -99  # (False)
    print((x < -100 or x > 100) and x % 2 == 0)

    s = "CapitaL"  # True
    s = "Not Capital" # False

    print(str.isupper(s[:1]) and str.isupper(s[-1:]))

    # [ ] Write a second expression to test if x is an even number outside the range [-100, 100]
    x = 104  # (True), x not in the range and Even
    print(not(-100 < x < 100) and x % 2 == 0)

    x = 115  # (False), x not in the range but Odd
    print(not(-100 < x < 100) and x % 2 == 0)
    print(not(x > -100 and x < 100) and x % 2 == 0)



if __name__ == '__main__':
    booleanoperators()
    combiningcomparisons()
