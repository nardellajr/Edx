
def isIn(char, astr):
    """
    :param char: a single character
    :param astr: an alphabetized string
    :return: True if char is in astr: False otherwize
    """
    # Base case
    if len(astr) == 0:
        return False

    if len(astr) == 1:
        return astr == char

    midstring = int(len(astr)/2)
    if astr[midstring] == char:
        return True

    if char < astr[midstring]:
        # We could check for astr len == 1 instead of checking midstring != 0
        # return midstring != 0 and isIn(char, astr[:midstring])
        return isIn(char, astr[:midstring])
    else:
        # We could check for astr len == 1 instead of checking midstring != 0
        # return midstring != 0 and isIn(char, astr[midstring:])
        return isIn(char, astr[midstring:])


if __name__ == '__main__':

    assert isIn("S", "PQRSTUVWX"), "Should return True"
    assert isIn("t", "pqrstuvw"), "Should return True"

    # Search string doesn't exist
    print("isIn('i', 'hennry')")
    if isIn("i", "hennry"):
        print("True")
    else:
        print("False")

    # Test Empty string
    print("isIn('i', '')")
    if isIn("i", ""):
        print("True")
    else:
        print("False")

    # Test string length of 1
    print("isIn('i', 'i')")
    if isIn("i", "i"):
        print("True")
    else:
        print("False")
