
def generate_star3(size):
    for row in range(size):
        for col in range(size):
            if row == col:
                print("*", end="")
            elif col + row == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    print("--------")


def evenodd():
    """ Complete the following program to count the number of even positive numbers,
        odd negative numbers, and zeros in `lst`
    """

    lst = [9, 0, -2, -4, -5, 2, -15, 6, -65, -7]

    even_positives = 0
    odd_negatives = 0
    zeros = 0

    # Count even_positives, odd_negatives, and zeros
    for i, x in enumerate(lst):
        if i % 2 == 0:
            print(f"even i: {i}")
            if x > 0:
                even_positives = even_positives + 1
        else:
            print(f"odd i: {i}")
            if x < 0:
                odd_negatives = odd_negatives + 1
            if x == 0:
                zeros = zeros + 1

    print("Number of even positives:", even_positives)
    print("Number of odd negatives:", odd_negatives)
    print("Number of zeros:", zeros)


    # Write a program to count the number of punctuation marks (. , ? ! ' " : ;) in `s`
    pmarks = [".", ",", "?", "!", "'", '"', ":", ";"]

    # Sherlock Holmes (by Sir Arthur Conan Doyle, 1859-1930)
    s = "??Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth."

    punctuationcount = 0

    for i in s:
        if i in pmarks:
            punctuationcount = punctuationcount + 1

    print(punctuationcount)

    continued = True
    while continued:
        i = input("Please enter an odd positive number(put spaces between the numbers) ")
        nums = i.split(" ")
        # print(nums)

        # odd length of numbers
        if len(nums) % 2 != 0:
            for x in nums:
                # Test for positive number
                if int(x) >= 0:
                    continued = False
                    break

if __name__ == '__main__':
    generate_star3(5)
    evenodd()

