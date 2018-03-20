import os


def errortypes():

    try:
        # SyntaxError
        # print(exec("if w in q:"))
        # SyntaxError unexpected EOF while parsing (<string>, line 1)

        # ValueError
        # print(float("mike"))
        # Created ValueError could not convert string to float: 'mike'

        # TypeError
        stuff = ""
        stuff.count(1)
        # Created TypeError must be str, not int

    except SyntaxError as exception_object:
        print("SyntaxError", exception_object)
    except TypeError as exception_object:
        print("Created TypeError", exception_object)
    except ValueError as exception_object:
        print("Created ValueError", exception_object)


def handlingexceptions():
    lst = [8, 85.4, [55, 4], 'word', (59,), {2: 43.5}]

    try:
        x = input("Enter a number: ")
        x = float(x)

        for i in range(7):
            print("{} / {:.2f} = {:.2f}".format(lst[i], x, lst[i] / x))

    except TypeError as exception_object:
        print("Error with:", x, exception_object)
    except ValueError as exception_object:
        print(x, "is not a float", exception_object)
    except ZeroDivisionError as exception_object:
        print("Cannot divide by zero", exception_object)

    print("Done!")


def fileexceptionhandling():

    print(os.getcwd())

    # ask user for a file name
    fname = input("Enter file name: ")
    f = None
    try:
        # the file should be located in `parent_dir`
        fname = os.path.join(os.getcwd(), "parent_dir", fname)

        # opening text_file.txt for reading
        f = open(fname, 'r')
        print(f.readline())
        f.close()

    except Exception as exception_object:
        print("Unexpected exception", exception_object)
    finally:
        if f != None and not f.close():
            f.close()


def findnum(x):

    valid_nums = (1, 2, 8, 16, 32, 64)

    while x not in valid_nums:

        try:
            x = int(input("Please enter a number: "))
            print(x)
        except ValueError as exception_object:
            print("Oops! That was no valid number. Try again...")

    print("You guessed the number!")


if __name__ == '__main__':
    findnum(4)

    # handlingexceptions()
    # errortypes()