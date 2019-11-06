def is_even(i):
    """Input: i, a positive int
       Returns True if i is even, otherwise False
    """
    print('hi')
    return i % 2 == 0


print(is_even(5))


def g(x):
    def h():
        x = 'abc'

    x = x + 1
    print('in g(x): x = ', x)
    h()
    return x


x = 3
z = g(x)

print('*****recursive functions*****')


def recursive_power(base, exp):
    # this handles case where exp is <= 0 and base case check
    if exp <= 0:
        return 1

    return base * recursive_power(base, exp - 1)


print(recursive_power(2, 5))


def iter_power(base, exp):
    value = 1
    for _ in range(exp):
        value *= base

    return value


print(iter_power(2, 5))

print('recursive Tower of Hanoi')


def print_move(frm, to):
    print('move from ' + str(frm) + ' to ' + str(to))


def towers(n, fr, too, spare, count):
    count += 1
    if n == 1:
        print_move(fr, too)
    else:
        towers(n - 1, fr, spare, too, count)
        print("1st recursive step")
        towers(1, fr, too, spare, count)
        towers(n - 1, spare, too, fr, count)

    print(count)


print(towers(4, 'P1', 'P2', 'P3', 0))


def gcdIter(a, b):
    """
    a, b: postive integers
    :return: a positive integer, the greatest common divisor of a & b
    """
    # we use the smaller value of the 2 inputs, so we reduced the number of times we have to loop
    # start_value = b
    # if a < b:
    #     start_value = a
    start_value = min(a, b)  # rewrite the above if statement

    for i in range(start_value, 0, -1):
        # print(i)
        if b % i == 0 and a % i == 0:
            print(i)
            break


gcdIter(120, 102)
gcdIter(2, 12)
gcdIter(17, 12)


def gcdRecur(a, b):
    print(f'a = {a}, b = {b}')
    if b == 0:
        return a

    return gcdRecur(b, a % b)


print(gcdRecur(120, 102))


# Code for determining the number of Rabbits, Fibonacci
# 2 base cases
# Recursive case
# Females(n) = Females(n-1) + Females(n-2)
def fib(x):
    if x == 0 or x == 1:
        return 1

    return fib(x - 1) + fib(x - 2)


fib(1)
fib(2)
fib(3)
print(fib(12))


# Fibonacci iteration
x = int(input("Enter no. of terms you want in Fibonacci Series: "))
if x < 0:
    print("Please enter a non-zero positive integer value")
if x > 0:
    first_term = 0
    second_term = 1
    print(first_term)
    print(second_term)
    for a in range(1, x-1):
        third_term = first_term + second_term
        print(third_term)
        first_term, second_term = second_term, third_term


def isPalindrome(s):
    """
    This recursive function take a string and compares the first and last item to see if they match and
    if they do, take the string minus the fist and last characters and calls the function again, working down
    to the len of the string is <= 1.
    :param s:
    :return:
    """

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


print('---------------------')
print('Is able was I ere I saw Elba, a palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))


def isIn(char, aStr):
    """
    :param char: a single character
    :param aStr: an alphabetized string
    :return: True if char is in aStr, False otherwise
    """
    # first test middle character
    l = len(aStr) / 2
    print(l)

    if



print(isIn('a', 'abdefgjklmqrstuvwxyz'))
print(isIn('a', ''))







