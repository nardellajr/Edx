
def searchlist():
    lst = [22, 89, 69, 78, 58, 22, 56, 13, 74, 8, 32, 58, 8, 63, 46, 79, 9, 38, 25, 96]

    searchvalue = input("Please enter an integer value between 0 and 100 ")

    if searchvalue.isdigit():
        num = int(searchvalue)
    else:
        print(f"{searchvalue} is not an integer")
        return

    if num in lst:
        print(f"{num} is contained in the list")
    else:
        print(f"{num} is not contained in the list")


def findapplicant():
    """ The `records` list contains information about a company's employees
        each of the elements in `records` is a list containing the name and ID of an employee.
        Write a program to test if `applicant` is contained in `records` and display an appropriate message
    """

    # Records of names and IDs
    records = [['Colette', 22347], ['Skye', 35803], ['Alton', 45825], ['Jin', 24213]]
    applicant = ['Joana', 20294]
    applicant1 = ['Colette', 22347]

    if applicant in records:
        print(f"{applicant} is contained in the records")
    else:
        print(f"{applicant} is not contained in the records")

    if applicant1 in records:
        print(f"{applicant1} is contained in the records")
    else:
        print(f"{applicant1} is not contained in the records")


if __name__ == '__main__':
    searchlist()
    findapplicant()
