import string

def gcd_iter(a, b):
    """
    Greatest Common Divisor of 2 positive integers is the largest integer that divides each of them
    without a remainder.
    :param a: int
    :param b: int
    :return: a positive integer, the greatest common divisor of a & b
    """

    #d = a
    #if a > b:
    #    d = b

    d = min(a, b)

    for i in range(d, 0, -1):
        if (b % i == 0 and a % i == 0) or i == 1:
            print(f"Greatest Common Divisor: {i}")
            return i

    # Another way to write
    # while a % d != 0 or b % d != 0:
    #    d -= 1


def gcd_recur(a, b):
    """ Recursive function """
    # Base case is when b = 0
    if b == 0:
        print(f"Greatest Common Divisor: {a}")
        return a
    else:
        return gcd_recur(b, a % b)


"""
    Euclid's Algorithm
    
    What happens in this recursive function?
    1st called with 9,12
        gcd_recur(12, 9) 9 % 12 = 9
    2nd call with 12, 9
        gcd_recur(9, 3)  12 % 9 = 3
    3rd call with 9, 3
        gcd_recur(3, 0)    9 % 3 = 0      
    4th call with 3, 0
        return 3

    And 3 works it way back up the calls to be returned
"""


def fib(x):
    """
    Fibonacci numbers, modeled the following challenge:
    Newborn pair of rabbits(1 female, 1 male) are put in a pen
    Rabbits mate at age of 1 month
    Rabbits have a one month gestation period
    Assume rabbits never die, that female always produces 1 new pair (1 male, 1 female) every month
    from its second month on.
    How many female rabbits are there at the end of 1 year, 5 years, etc ??

    - At the end of the first month, they mate, but there is still only 1 pair.
    - At the end of the second month the female produces a new pair, so now there are 2 pairs of rabbits in the field.
    - At the end of the third month, the original female produces a second pair, making 3 pairs in all in the field.
    - At the end of the fourth month, the original female has produced yet another new pair,
        and the female born two months ago also produces her first pair, making 5 pairs.

    At the end of the nth month, the number of pairs of rabbits is equal to the number of new pairs
     (that is, the number of pairs in month n − 2) plus the number of pairs
      alive last month (that is, n − 1). This is the nth Fibonacci number.

    females(n) = females(n-1) + females(n-2)

    In this case there are 2 Base cases
    females(0) = 1
    females(1) = 1

    Recursive Case
    females(n) = females(n-1) + females(n-2)

    assumes x an int >=0
    :returns Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        # f = fib(x - 1) + fib(x - 2)
        # print(f)
        return fib(x - 1) + fib(x - 2)


def ispalindrome(s):
    """
    A Palindrome a sequence of characters which reads the same backward as forward, like taco cat

    Base case: a string of length 0 or 1
    Recursive case: if first character matches last character, then is a palindrome if middle section is a palindrome

    Example 'Able was I, ere I saw Elba' converted to 'ablewasiereisawleba'

    'ablewasiereisawleba' -- First letter = last letter 'a' == 'a', then
    'blewasiereisawleb'   -- First letter = last letter 'b' == 'b', and so on

    :param x:
    :return:
    """

    def tochars(s):

        s = s.lower()
        ans = ""
        for c in s:
            if c in string.ascii_lowercase:
                ans = ans + c
        return ans

    def ispal(s):
        if len(s) <= 1:
            print("True")
            return True
        else:
            return s[0] == s[-1] and ispal(s[1:-1])  # Slices out everything except first and last letter of string

    return ispal(tochars(s))


if __name__ == '__main__':
    print("Iterative")
    assert gcd_iter(9, 12) == 3, "Should return 3"
    assert gcd_iter(6, 12) == 6, "Should return 6"
    assert gcd_iter(17, 12) == 1, "Should return 1"
    print("Recursive")
    assert gcd_recur(9, 12) == 3, "Should return 3"
    assert gcd_recur(6, 12) == 6, "Should return 6"
    assert gcd_recur(17, 12) == 1, "Should return 1"

    print("Fibonacci")
    assert fib(0) == 1, "Should have returned 3"
    assert fib(3) == 3, "Should have returned 3"
    assert fib(7) == 21, "Should have returned 21"

    print("Palindrome")
    print("Is 'eve' a palindrome?")
    assert ispalindrome("eve"), "Should return True"
    print("Is 'Able was I, ere I saw Elba' a palindrome?")
    assert ispalindrome("Able was I, ere I saw Elba"), "Should return True"
    print("Is 'Mike' a palindrome?")
    if not ispalindrome("Mike"):
        print("False")
    else:
        print("Should return False")
