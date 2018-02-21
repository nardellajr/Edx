
def main(vowels):

    v = "a,e,i,o,u"
    vowelcount = 0

    # Count the number of vowels in a string
    for item in vowels:
        if item in v:
            vowelcount += 1

    print(vowelcount)
    return vowelcount


def FindBob(namestring):

    count = 0
    bobcount = 0

    for item in namestring:
        if item == "b":
            #get the next 2 position and see if it make bob
            if namestring[count: count + 3] == "bob":
                bobcount += 1
        count += 1

    print(bobcount)
    return bobcount


if __name__ == "__main__":
    # s = "aeiout"
    # assert main(s) == 5, "Should have been 5 vowels"

    s = "azcbobobegghakl"
    assert FindBob(s) == 2, "should have found 2 bobs"
