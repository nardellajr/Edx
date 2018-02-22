
# Different ways to use import
#import math
import math as ml
#from math import pow

def test():
    #print(pow(2, 3))

    x = -5
    print(ml.fabs(x))

    print(ml.gcd(17, 12))

    values = input("Enter 2 positive integers: ").split()  # splits on space by default

    print(ml.gcd(int(values[0]), int(values[1])))

    # Pythagorean theorem
    # h**2 = a**2 + b**2
    # h = sqrt(a**2 + b**2)

    a = 3
    b = 4
    h = ml.sqrt(a**2 + b**2)
    print(h)

    print(f"Even number: 102 %2, no remainder {102 % 2}")  # Test for the remainder
    print(f"Odd number: 77 % 2, has remainder {77 % 2}")  # Test for the remainder

    #  / - division operator
    #  // - Integer division operator

    def is_even(n):
        if (n % 2) == 0:
            print(ml.sqrt(n))

    i = [25, 34, 193, 2, 81, 26, 44]

    for item in range(len(i)):
        is_even(item)


def mathstuff():

    # round up
    x = ml.ceil(31.8)
    print(x)  # will print 32

    x = ml.trunc(31.8)
    print(x)  # will print 31

    # round down
    x = ml.floor(31.8)
    print(x)  # will print 31

    # Price of a chocolate box
    p = 4.35

    # Quantity needed
    q = 200

    # Order total price (Should be 4.35 * 200 = $870.00)
    total = p * q
    print(f"Total: {total}")
    print("Total price: ", "{0:.2f}".format(ml.ceil(total)))


if __name__ == '__main__':
    # test()
    mathstuff()

