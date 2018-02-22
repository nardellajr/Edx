import sys
import os


def directorystuff():
    print(sys.platform)

    print(f"Working directory start: ", os.getcwd())
    # print(f"Working directory start: ", os.getcwdu())
    # print(f"Working directory start: ", os.getegid())

    os.chdir('test_chdir')

    print(f"Working directory change: {os.getcwd()}")

    # Working directory start:  E:\Work\Python\Edx
    # Working directory change: E:\Work\Python\Edx\test_chdir

    os.chdir("..\..")  # os.chdir("..\..")

    print(f"Working directory change: {os.getcwd()}")

    os.chdir("Edx")

    print(f"Working directory change: {os.getcwd()}")

    print(f"Current directory content: {os.listdir()}")

    os.mkdir("new_child")

    dir = os.listdir()
    print(f"Current directory content: {os.listdir()}")

    if "new_child" in dir:
        print("new_child directory created")

    os.rmdir("new_child")
    dir = os.listdir()

    if "new_child" not in dir:
        print("new_child directory was removed")


    print(f"Working directory change: {os.getcwd()}")

    os.mkdir("new_child")
    print(f"Current directory content: {os.listdir()}")
    os.rename("new_child", "old_child")
    print("Renamed new_child to old_child")
    print(f"Current directory content: {os.listdir()}")
    os.rmdir("old_child")
    print(f"Current directory content: {os.listdir()}")


def directorytask1():

    dirname = input("Please enter a directory name: ")

    os.mkdir(dirname)
    print(f"Directory contents: {os.listdir()}")
    os.rmdir(dirname)
    print(f"Directory contents: {os.listdir()}")


def directorytask1b():

    # os.path.isfile(...)
    # os.path.isdir(...)

    # top = os.getcwd()
    print(f"Current working directory: {os.getcwd()}")
    currdir = os.listdir()
    removedir = False
    if "test_dir" in currdir:
        os.chdir("test_dir")
        for root, dir, files in os.walk(os.getcwd()):
            if dir:
                print(f"There are {len(dir)} directories under 'Test_dir'. ")
                print(f"Can't remove 'Test_dir'. ")
                removedir = False
            if files:
                print(f"There are {len(files)} files under the 'Test_dir'. ")
                print(f"Can't remove 'Test_dir'. ")
                removedir = False
            print(f"Root: {root}, Dir: {dir}, Files: {files}")
        else:
            # Empty directory
            removedir = False
        if removedir:
            os.rmdir("test_dir")
        else:
            return

    os.mkdir("test_dir")
    os.chdir("test_dir")
    print(f"Working directory change: {os.getcwd()}")

    os.mkdir("my_dir")
    os.chdir("my_dir")
    print(f"Working directory change: {os.getcwd()}")
    os.chdir("..")
    print(f"Working directory change: {os.getcwd()}")
    os.rename("my_dir", "your_dir")
    print(f"Directory contents: {os.listdir()}")
    os.rmdir("your_dir")
    print(f"Directory contents: {os.listdir()}")



def pathinfo():

    print(f"Current working dir: {os.getcwd()}")

    abs_path = os.path.abspath("parent_dir/child1_dir/leaf1.txt")
    print(f"Absolute path to leaf1.txt is {abs_path}")

    if os.path.exists(abs_path):
        print("Path exists")

        if os.path.isfile(abs_path):
            print("It's a file")
        elif os.path.isdir(abs_path):
            print("It's a directory")
    else:
        print("Path doesn't exist")



if __name__ == '__main__':
    # directorytask1()

    directorytask1b()

    #pathinfo()





