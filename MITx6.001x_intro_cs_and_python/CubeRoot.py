
def main():

    cube = 29
    epsilon = 0.01
    guess = 0.0
    increment = 0.00001
    num_guesses = 0

    while abs(guess**3 - cube) >= epsilon and guess <= cube:
        guess += increment
        num_guesses += 1

    print("num_guesses =", num_guesses)
    if abs(guess**3 - cube) >= epsilon:
        print("Failed on cube root of", cube)
    else:
        print(guess, "is close to the cube root of", cube)


def main2():
    x = 23
    epsilon = 0.01
    step = 0.1
    guess = 0.0

    while abs(guess ** 2 - x) >= epsilon:
        if guess <= x:
            guess += step
        else:
            break

    if abs(guess ** 2 - x) >= epsilon:
        print('failed')
    else:
        print('succeeded: ' + str(guess))


def main3():
    x = 25
    epsilon = 0.01
    step = 0.1
    guess = 0.0

    # This will go into an infinite loop !!
    while guess <= x:
        if abs(guess ** 2 - x) >= epsilon:
            guess += step

    if abs(guess ** 2 - x) >= epsilon:
        print('failed')
    else:
        print('succeeded: ' + str(guess))


def BisectionSearch():
    x = 25
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = x
    ans = (high + low)/2.0

    while abs(ans**2 - x) >= epsilon:
        print("low = " + str(low) + " high = " + str(high) + ' ans = ' + str(ans))
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans

        ans = (high + low)/2.0

    print("numGuesses = " + str(numGuesses))
    print(str(ans) + " is close to square root of " + str(x))

def numberGuesser():

    validinputs = "h,l,c"
    print("Please think of a number between 0 and 100!")
    high = 100
    low = 0
    ans = int((high + low) / 2)
    user = ""

    while user != "c":
        print("Is your secret number " + str(ans) + "?")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to "
              "indicate I guessed correctly. ", end='')
        user = input()

        if user not in validinputs:
            print("Sorry, I did not understand your input.")
        else:
            if user == "c":
                break

            if user == "h":
                high = ans
            else:
                low = ans

            ans = int((high + low)/2)

    print("Game over. Your secret number was :", ans)


if __name__ == "__main__":
    # main()
    # main2()
    #    main3()
    # BisectionSearch()
    numberGuesser()

