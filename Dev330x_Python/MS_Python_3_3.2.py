import os
import random
import shutil


def setupenv():

    # Remove the `files_exercises` directory (if it exists)
    if 'files_exercises' in os.listdir():
        print('Removing "files_exercises" directory')
        shutil.rmtree('files_exercises')

    # Create a new directory called `files_exercises`
    print('Making "files_exercises" directory')
    os.mkdir('files_exercises')

    # Change the working directory to `files_exercises`
    print('Changing working directory to "files_exercises"')
    os.chdir('files_exercises')

    # Display the current working directory to verify you are in the correct location
    print("Current working directory:", os.getcwd())

    # Create 100 text files, the first line of each file is a random number in the range [1000, 9999]
    print("Creating 100 text files")
    random.seed(25000)  # to get the same random numbers every time the setup runs
    for i in range(100):
        file_name = str(i) + ".txt"
        f = open(file_name, 'w')
        f.write(str(random.randint(1000, 9999)))
        f.close()

    # Create 5 directories
    print("Creating 5 directories")
    for i in range(1, 6):
        os.mkdir("dir_" + str(i))

    print("Environment setup completed!")


def changetoworkingdirectory():
    # Navigate to `parent_dir` directory (if not already in it)
    current_path = os.getcwd()
    nb_path = None
    if "parent_dir" in current_path:
        nb_path = current_path.split("parent_dir")[0]
    elif "parent_dir" in os.listdir():
        nb_path = current_path

    if nb_path is not None:
        print("Changing directory to parent_dir")
        os.chdir(os.path.join(nb_path, 'parent_dir'))
    else:
        print("Making directory 'parent_dir'")
        os.mkdir(os.path.join(current_path, 'parent_dir'))

    if 'files_exercises' in os.listdir():
        os.chdir(os.path.join(os.getcwd(), 'files_exercises'))

    print("Current directory:", os.getcwd())


def removefile(recreatetestenv):

    try:
        changetoworkingdirectory()

        if 'files_exercises' not in os.getcwd() and 'files_exercises' not in os.listdir():
            if recreatetestenv:
                print("Running setupenv()")
                setupenv()

        num = input("Please enter a file number: ")
        num = int(num)
        filename = str(num) + ".txt"
        os.remove(filename)

    except ValueError as exception_object:
        print(num, "is not a number. {0:}".format(exception_object))
    except FileNotFoundError as exception_object:
        print("Cannot find file: ", exception_object)
    except PermissionError as exception_object:
        print("Cannot delete a directory: ", exception_object)
    except Exception as exception_object:
        print("Unexpected Exception: ", exception_object)
    else:
        print(filename, "was removed")


if __name__ == '__main__':

    recreatetestenv = False
    removefile(recreatetestenv)

