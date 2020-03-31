board = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]


def solve(board):
    # the base case would only be possible if we've hit the end of our board
    finder = find_blank_entry(board)

    # base case
    if not finder:
        return True
    else:
        row, col = finder

    # recursion
    for i in range(1, 10):
        # check if values for sudoku (1-9) are valid solutions
        if valid(board, i, (row, col)):
             # add to board if valid
            board[row][col] = i

            if solve(board):  # recursion - call solve function on new board
                return True

            # if we loop through all numbers and none are valid, we reset
            # position value to 0 and try again
            board[row][col] = 0

    return False


def valid(board, num, pos):
    # Check row
    # if the row at i == num. also, we have to make sure the position we just altered (pos[1])
    # we ignore it
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check grid
    # pos = (i, j)  --> row, col
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True  # if a number is valid across row, column and grid checks, return True


def print_board(board):
    # this will be to print out a readable board,
    # seperating every third row with a line
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            # this will separate after every third element in i
            # for readability
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # if j is at the last element in i, to go to the next line
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_blank_entry(board):
    # for every element in every row (i)
    for i in range(len(board)):
        for j in range(len(board[0])):
            # if the j element in the row i is blank (0), return the position
            if board[i][j] == 0:
                return (i, j)  # row, column

    return None

print_board(board)
solve(board)
print('__________________')
print_board(board)