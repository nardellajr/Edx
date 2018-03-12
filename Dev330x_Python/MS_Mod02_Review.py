def test(x):
    if -50 <= x <= 0:
        print("Entered invalid number: {:d}".format(x))

    # convert x to int
    x = int(x)

    # Test input validity
    if (-50 <= x <= 0) or (100 <= x <= 200):
        print("Entered invalid number: {:d}".format(x))
    else:
        print("Valid number {:d}".format(x))


# Rate   Taxable Income                       Tax Owed
# 10%  $0 to $9,325           10% of Taxable Income
# 15%  $9,325 to $37,950     $932.50 plus 15% of the excess over $9,325
# 25%  $37,950 to $91,900    $5,226.25 plus 25% of the excess over $37,950
# 28%  $91,900 to $191,650   $18,713.75 plus 28% of the excess over $91,900
# 33%  $191,650 to $416,700  $46,643.75 plus 33%% of the excess over $191,650
# 35%  $416,700 to $418,400  $120,910.25 plus 35% of the excess over $416,700
# 39.60%  $418,400+          $121,505.25 plus 39.6% of the excess over $418,400

def tax_owed(income):
    """
    Calculate the taxes owed using the tax bracket table.

    args:
        income: Taxable income in dollars

    returns:
        tax_owed: Taxes owed based on income and tax bracket
    """
    taxbracket1 = 9325
    taxbracket2 = 37950
    taxbracket3 = 91900
    taxbracket4 = 191650
    taxbracket5 = 416700
    taxbracket6 = 418400

    if 0 <= income < taxbracket1:
        tax = .10 * income

    if taxbracket1 <= income < taxbracket2:
        tax = (.10 * taxbracket1) + .15 * (income - taxbracket1)

    if taxbracket2 <= income < taxbracket3:
        tax = (.10 * taxbracket1) + .15 * (taxbracket2 - taxbracket1) + .25 * (income - taxbracket2)

    if taxbracket3 <= income < taxbracket4:
        tax = (.10 * taxbracket1) + .15 * (taxbracket2 - taxbracket1) + .25 * (taxbracket3 - taxbracket2) + .28 * (
                income - taxbracket3)

    if taxbracket4 <= income < taxbracket5:
        tax = (.10 * taxbracket1) + .15 * (taxbracket2 - taxbracket1) + 25 * (taxbracket3 - taxbracket2) + .28 * (
                taxbracket4 - taxbracket3) + .33 * (income - taxbracket4)

    return tax


def taxesowed(income):
    taxbracket1 = 9325
    taxbracket2 = 37950
    taxbracket3 = 91900
    taxbracket4 = 191650
    taxbracket5 = 416700
    taxbracket6 = 418400

    bracket1tax = 0
    bracket2tax = 0
    bracket3tax = 0
    bracket4tax = 0
    bracket5tax = 0
    bracket6tax = 0
    bracket7tax = 0

    taxableamount = 0

    if 0 < income:
        bracket1tax = .10 * taxbracket1
        bal = income - taxbracket1

    if taxbracket1 <= income:
        if income > taxbracket2:
            taxableamount = taxbracket2 - taxbracket1
        else:
            taxableamount = income - taxbracket1

        bracket2tax = .15 * taxableamount

    if taxbracket2 <= income:
        if income > taxbracket3:
            taxableamount = taxbracket3 - taxbracket2
        else:
            taxableamount = income - taxbracket2

        bracket3tax = .25 * taxableamount

    if taxbracket3 <= income:
        if income > taxbracket4:
            taxableamount = taxbracket4 - taxbracket3
        else:
            taxableamount = income - taxbracket3

        bracket4tax = .28 * taxableamount

    if taxbracket4 <= income:
        if income > taxbracket5:
            taxableamount = taxbracket5 - taxbracket4
        else:
            taxableamount = income - taxbracket4

        bracket5tax = .33 * taxableamount

    if taxbracket5 <= income:
        if income > taxbracket6:
            taxableamount = taxbracket6 - taxbracket5
        else:
            taxableamount = income - taxbracket5

        bracket6tax = .35 * taxableamount

    if income >= taxbracket6:
        bracket7tax = .3960 * (income - taxbracket6)

    tax = bracket1tax + bracket2tax + bracket3tax + bracket4tax + bracket5tax + bracket6tax + bracket7tax
    print(tax)
    return tax


def ispalindrome(word):
    palindrome = True

    word = word.replace(" ", "").lower()

    center = len(word) // 2
    for i in range(center):
        print(word[i])
        print(word[len(word) - i - 1])
        if word[i] != word[len(word) - i - 1]:
            palindrome = False
            break

    return palindrome


def rangetest():
    while True:
        n = int(input("Please enter a number outside the ranges [-50, 0] and [100, 200]"))

        if (-50 <= n <= 0) or (100 <= n <= 200):
            print("InValid Number {:d}".format(n))
        else:
            break


def workwithtable():
    table = [[5, 2, 6], [4, 6, 0], [9, 1, 8], [7, 3, 8]]

    # transpose columns to rows
    for t in range(len(table[0])):
        for i in table:
            print(i[t], end=" ")
        print()

    # display the sum of each column in table
    sum = 0
    for t in range(len(table[0])):
        for i in table:
            sum += i[t]
        print(sum)
        sum = 0


def generatediamond(size):
    """
    print(f"A {row - col}")
    print(f"B {col - row}")
    print(f"C {size // 2}")
    """

    if size % 2 == 0:
        size -= 1

    for row in range(size):
        for col in range(size):
            if col == size // 2 and (row == 0 or row == (size - 1)):
                print("*", end="")
                break
            # prints left side of the diamond
            elif (row + col) == (size // 2) or row - col == size // 2:
                print("*", end="")
            # print the right side of the diamond
            elif (col - row) == (size // 2) or row + col == ((size // 2) + (size - 1)):
                print("*", end="")
            else:
                print(" ", end="")
        print()


from datetime import datetime


def groceryreceipt():
    d = datetime.today()
    print(d.strftime("%a %B %m, %Y @ %I:%M %p"))
    print("-" * 30, end="\n\n")

    items = [["APPLES 1LB", 1.99, 2], ["OLIVE OIL", 10.99, 1], ["TOMATOS 1LB", 1.29, 2.6], ["MILK 1/2G", 3.45, 1],
             ["FLOUR 5LB", 2.99, 1], ["BELL PEPPERS 1LB", 1.35, 2.8], ["WHITE TUNA", 1.69, 1],
             ["CHEESE 1/2LB", 4.99, 2]]

    count = 0
    itemtotal = 0
    grandtotal = 0
    for i in items:
        count += 1
        itemtotal = (i[1] * i[2])
        print(" {:d} - {:18s} ${:5.2f}".format(count, i[0], itemtotal))
        print("{:8.1f} @ ${:5.2f}".format(i[2], i[1]))
        grandtotal += itemtotal

    print("-" * 30)
    print("{:>23s} ${:5.2f}".format("Total", grandtotal))


def dashes():
    """Print a fancy line of dashes"""
    print("o" + 35 * '-' + "o")


def display(message):
    """
    Print `message` in the center of a 35 characters string

    args:
        message: string to display

    returns:
        None
    """
    print("|{:^35s}|".format(message))


def draw(board):
    """
    Draw the `board` table.

    The board reflects the current state of the game, a number indicates an available location.

    args:
        board: 3x3 table (list of lists) containing the current state of the game

    returns:
        None

    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9
        -----------
         4 | 5 | 6
        -----------
         1 | 2 | 3

         After a few marks: board = [['7', '8', 'X'], ['O', 'O', '6'], ['1', 'X', '3']]
         The printout should look like:
         7 | 8 | X
        -----------
         O | O | 6
        -----------
         1 | X | 3
    """
    for r in board:
        count = 0
        for c in r:
            print(" {:s} ".format(c), end="")
            count += 1
            if count != len(r):
                print("|", end="")
        print()
        print("-" * 11)


def available(location, board):
    """
    Check the availability of a `location` on the current `board`

    An available location on the board contains a number between 1 and 9 stored as a string.
    If the location contains 'X' or 'O', the location is not available and the function should return False;
    otherwise, the function should return True indicating the location is available

    args:
        location: a number between 1 and 9 stored as a string
        board: 3x3 table (list of lists) containing the current state of the game

    returns:
        True if the location is available. False if the location is not available

    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9
        -----------
         4 | 5 | 6
        -----------
         1 | 2 | 3

         available("1", board) --> returns True
         available("9", board) --> returns True

         After a few marks: board = [['7', '8', 'X'], ['O', 'O', '6'], ['1', 'X', '3']]
         The printout should look like:
         7 | 8 | X
        -----------
         O | O | 6
        -----------
         1 | X | 3

         available("1", board) --> returns True, because there is a number
         available("5", board) --> returns False, because there is 'O'
         available("9", board) --> returns False, because there is 'X'
    """
    locavailable = False
    for r in board:
        if location in r:
            locavailable = True
            break

    return locavailable


def mark(player, location, board):
    """
    Mark `location` on the `board` with the `player` symbol.

    Should replace the `location` number on the board with `X` or `O`

    args:
        player: player's symbol, either 'X' or 'O'
        location: a number between 1 and 9 stored as a string
        board: 3x3 table (list of lists) containing the current state of the game

    returns:
        None

    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9
        -----------
         4 | 5 | 6
        -----------
         1 | 2 | 3

         After mark('O', '4', board)
         The printout should look like:
         7 | 8 | 9
        -----------
         O | 5 | 6
        -----------
         1 | 2 | 3

         After mark('X', '3', board)
         The printout should look like:
         7 | 8 | 9
        -----------
         O | 5 | 6
        -----------
         1 | 2 | X

         After mark('O', '9', board)
         The printout should look like:
         7 | 8 | O
        -----------
         O | 5 | 6
        -----------
         1 | 2 | X
    """
    exitloops = False
    for r in range(len(board)):
        for n in range(len(board[r])):
            if location == board[r][n]:
                board[r][n] = player
                exitloops = True
                break

        if exitloops:
            break


def check_win(board):
    """
    Check if there is a winner.

    A win happens if the either of the players was able to place 3 symbols ('X' or 'O') in:
    a horizontal, vertical, diagonal, or anti-diagonal placement.

    args:
        board: 3x3 table (list of lists) containing the current state of the game

    returns:
        True if there is a winner. False if there is no winner yet

    examples:
        Horizontal win:
        ================
         7 | O | 9
        -----------
         X | X | X
        -----------
         1 | O | 3
        check_win(board) --> returns True, because 'X' won

         O | O | O
        -----------
         X | X | 6
        -----------
         X | O | 3
        check_win(board) --> returns True, because 'O' won

        Vertical win:
        ================
         7 | 8 | X
        -----------
         X | O | X
        -----------
         O | O | X
        check_win(board) --> returns True, because 'X' won

         X | O | O
        -----------
         4 | O | 6
        -----------
         X | O | X
        check_win(board) --> returns True, because 'O' won

        Diagonal win:
        ================

         X | 8 | O
        -----------
         4 | X | X
        -----------
         O | O | X
        check_win(board) --> returns True, because 'X' won

         O | X | O
        -----------
         X | O | X
        -----------
         1 | 2 | O
        check_win(board) --> returns True, because 'O' won


        Anti-Diagonal win:
        ================
         O | 8 | X
        -----------
         4 | X | X
        -----------
         X | O | O
        check_win(board) --> returns True, because 'X' won

         7 | 8 | O
        -----------
         X | O | X
        -----------
         O | O | X
        check_win(board) --> returns True, because 'O' won

        No winners yet:
        ================
         O | 8 | 9
        -----------
         4 | X | X
        -----------
         X | O | O
        check_win(board) --> returns False
    """
    horwin = False
    vertwin = False
    diawin = False
    antidiawin = False
    diaOwin = False
    diaXwin = False

    # *** Look at cleaning up this code to reduce duplication of loops and checks ***
    for boardrow in board:
        # Check Horizontal win
        if boardrow.count('O') == 3 or boardrow.count('X') == 3:
            horwin = True
            break

    # Check vertical win
    for i in range(len(board[0])):
        sumO = 0
        sumX = 0
        for boardrow in board:
            if boardrow[i] == 'O':
                sumO += 1
            if boardrow[i] == 'X':
                sumX += 1

            if sumX == 3 or sumO == 3:
                vertwin = True
                break

        # Forward diagonal
        if board[i][i] == 'O':
            diaOwin += 1
        if board[i][i] == 'X':
            diaXwin += 1

        if diaOwin == 3 or diaXwin == 3:
            diawin = True
            break

    player = ['O', 'X']
    # Anti - diagonal
    for p in player:
        if board[0][2] == p and board[1][1] == p and board[2][0] == p:
            antidiawin = True
            break

    return horwin or vertwin or diawin or antidiawin


def check_tie(board):
    """
    Check the game for a tie, no available locations and no winners.

    args:
        board: 3x3 table (list of lists) containing the current state of the game

    returns:
        True if there is a tie. False the board is not full yet or there is a winner

    examples:
         O | O | X
        -----------
         X | X | O
        -----------
         O | O | X
        check_tie(board) --> returns True

         O | O | 9
        -----------
         X | X | 6
        -----------
         X | O | 3
        check_tie(board) --> returns False, because there are still available location
    """

    # Check board not full
    tie = True
    for r in board:
        for i in r:
            if i != "O" and i != "X":
                tie = False
                break

    return tie


from random import randint


def tictactoe():
    board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]

    player = ['X', 'O']
    turn = randint(0, 1)

    win = False
    tie = False
    while not win and not tie:
        # switch players
        turn = (turn + 1) % 2
        current_player = player[turn]  # contains 'X' or 'O'

        # display header
        dashes()
        display("TIC TAC TOE")
        dashes()

        # display game board
        print()
        draw(board)
        print()

        # display footer
        dashes()

        # player select a location to mark
        while True:
            location = input("|{:s} Turn, select a number (1, 9): ".format(current_player))
            if available(location, board):
                break  # Only the user input loop, main loop does NOT break
            else:
                print("Selection not available!")
        dashes()

        # mark selected location with player symbol ('X' or 'O')
        mark(current_player, location, board)

        # check for win
        win = check_win(board)

        # check for tie
        tie = check_tie(board)

    # Display game over message after a win or a tie
    # clear_output()

    # display header
    dashes()
    display("TIC TAC TOE")
    dashes()

    # display game board (Necessary to draw the latest selection)
    print()
    draw(board)
    print()

    # display footer
    dashes()
    display("Game Over!")
    if (tie):
        display("Tie!")
    elif (win):
        display("Winner:")
        display(current_player)
    dashes()


if __name__ == '__main__':
    tictactoe()

"""
    groceryreceipt()
    
    generatediamond(3)

    workwithtable()

    rangetest()
    
    assert ispalindrome("madam") == True
    assert ispalindrome("A nut for a jar of tuna") == True
    assert ispalindrome("sir") == False
    
    assert(taxesowed(40000) == 5738.75, "Not valid")
    assert taxesowed(100000) == 20981.75, "Incorrect value returned"
    assert taxesowed(200000) == 49399.25
    assert taxesowed(417000) == 121015.25
    assert taxesowed(500000) == 153818.85

    test(-30)
    test(-55)
    test(199)
    test(201)
"""
