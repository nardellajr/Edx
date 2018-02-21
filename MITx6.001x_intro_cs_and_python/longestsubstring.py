
# prints the longest substring, in which the letters occur in alphabetical order
def main(alphstring):

    longestsubstring = ""
    currentsubstring = ""

    for item in alphstring:
        if currentsubstring == "" or ord(item) >= ord(currentsubstring[-1]):
            currentsubstring += item
        else:

            if len(currentsubstring) > len(longestsubstring):
                longestsubstring = currentsubstring
            currentsubstring = ""
            currentsubstring += item


    if len(currentsubstring) > len(longestsubstring):
        longestsubstring = currentsubstring

    print("Longest substring in alphabetical order is: ", longestsubstring)
    return longestsubstring


if __name__ == "__main__":

    s = 'azcbobobegghakl'
    assert main(s) == "beggh", "Should have been 'beggh'"

    s = 'abcbcd'
    assert main(s) == "abc", "Should have been 'abc'"
