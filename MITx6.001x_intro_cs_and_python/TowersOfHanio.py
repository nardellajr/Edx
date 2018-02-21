
"""
Hard to solve iteratively but not so bad using recursive calls

Think recursively!
    Solve a smaller problem
    Solve a basic problem
    Solve a smaller problem
"""


"""
3 tall spikes,
one spike has a stack of 64 different size discs
Need to move all disc to another spike, but
can only move one disc at a time, and a larger disc can never cover up a small disc
"""


def printmove(fromstack, tostack):
    print("move from " + str(fromstack) + " to " + str(tostack))


def towers(stacksize, fromstach, tostack, spare):

    if stacksize == 1:
        printmove(fromstach, tostack)
    else:
        towers(stacksize - 1, fromstach, spare, tostack)
        towers(1, fromstach, tostack, spare)
        towers(stacksize - 1, spare, tostack, fromstach)


if __name__ == '__main__':
    print(towers(4, "P1", "P2", "P3"))
