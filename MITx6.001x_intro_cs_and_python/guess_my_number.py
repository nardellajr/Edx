
print('Please think of a number between 0 and 100!')

low = 0
high = 100
feedback = None

while feedback == 'h' or feedback == 'l' or feedback is None:
    # guess = int((high + low) / 2.0)
    guess = (high + low) // 2.0
    print(f"Is you secret number {guess}?")
    feedback = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low."
                     " Enter 'c' to indicate I guessed correctly.")

    if feedback not in ['h', 'l', 'c']:
        print('Sorry, I did not understand your input')
        feedback = None
    else:
        if feedback == 'h':
            high = guess
        if feedback == 'l':
            low = guess
        if feedback == 'c':
            break

print('Game over. Your secret number was:', guess)

