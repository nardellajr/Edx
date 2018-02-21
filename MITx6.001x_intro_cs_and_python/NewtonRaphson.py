

# This is a lot more efficient, only 4,5 guesses to get a result
def newtonraphson(num):

    epsilon = 0.01
    y = num
    guess = y/2.0
    numguesses = 0

    while abs(guess*guess - y) >= epsilon:
        numguesses += 1
        guess = guess - (((guess**2) - y) / (2*guess))  # Newton-Raphson solution:  g - (g**2 - k)/2g

    print("numGuesses = " + str(numguesses))
    print("Square root of " + str(y) + " is about " + str(guess))


if __name__ == '__main__':
    newtonraphson(24)
    newtonraphson(54)
    