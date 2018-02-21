from datetime import time, datetime
import math as mth
import random
import os

def directory_count():
    """
    I) Get the current minute using appropriate functionality from `datetime`
    II) Take the square root of ..the current minute + 15
    III) Round the square root to an integer
    VI) return the rounded number as the number of directories to be created
    """
    dt = datetime.today()
    print(f"minute: {dt.minute}")

    dirnum = mth.floor(mth.sqrt(dt.minute + 15))
    print(f"Number of directories: {dirnum}")

    return dirnum


def name_generator():
    """
    Generate a single directory name using the pattern (MM_DD_YY_randnum).
    """
    num = random.randint(10000, 50000)
    print(num)

    dt = datetime.today()
    dirname = dt.strftime("%m_%d_%y_") + str(num)
    print(dirname)

    return dirname


def directory_creator(name):
    """
    Create a single directory called 'name' in the current working directory
    :param name: directory to be created
    :return: None
    """
    # print(os.getcwd())
    os.mkdir(name)


def create():
    """
    Generate the necessary directories
    :return:
    """
    numberofdirectories = directory_count()
    newdir = 0
    while newdir < numberofdirectories:
        newdir += 1
        name = name_generator()
        directory_creator(name)




if __name__ == '__main__':


    if'parent_dir' not in os.getcwd():
        if os.path.exists("./parent_dir"):
            print("Changing working dir to parent_dir")
            os.chdir("parent_dir")
        else:
            os.mkdir(os.getcwd() + "./parent_dir")
            print("Changing working dir to parent_dir")
            os.chdir("parent_dir")
    else:
        # so the code can run multiple times
        # while directory not ending with 'parent_dir' move up the path ..\
        while "parent_dir" not in os.getcwd()[-11]:
            # move up in dir to find 'parent_dir'
            os.chdir("..")
            print("moved up", os.getcwd())

    print(f"The current working directory is: {os.getcwd()}")

    randomdir = "randoms_directory"

    if not os.path.exists(os.getcwd() + "/" + randomdir):
        os.mkdir(randomdir)

    print("Changing working dir to", randomdir)
    os.chdir(randomdir)

    print(f"The current working directory is: {os.getcwd()}")

    create()

    print("Current directory content:", os.listdir())


