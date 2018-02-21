
def integerToBinary(num):

    isneg = False

    if num < 0:
        isneg = True
        num = abs(num)

    result = ""
    if num == 0:
        result = "0"

    while num > 0:
        # This will show if bit should be on or off
        result = str(num % 2) + result
        num = num//2
        print("num", num)

    if isneg:
        result = "-" + result

    print("result", result)


def floatToBinary():

    x = float(input("Enter a decimal number between 0 and 1: "))
    p = 0

    while ((2**p)*x) % 1 != 0:
        print("Remainder = " + str((2**p)*x - int((2**p)*x)))
        p += 1

    print(f"2 raised to the power of {p}")
    num = int(x*(2**p))

    result = ""
    if num == 0:
        result = "0"

    while num > 0:
        result = str(num % 2) + result
        num = num//2

    print(f"len of result: { len(result) }")
    print(f"range { list(range(p-len(result))) }")

    for i in range(p - len(result)):
        result = "0" + result

    result = result[0:-p] + "." + result[-p:]
    print("The binary representation of the decimal " + str(x) + " is " + result)


if __name__ == '__main__':

    # integerToBinary(110000245)
    #integerToBinary(19)
    floatToBinary()  # Enter  .375   or .333




