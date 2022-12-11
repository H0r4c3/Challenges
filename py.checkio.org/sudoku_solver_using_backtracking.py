'https://medium.com/@ev.zafeiratos/sudoku-solver-with-python-a-methodical-approach-for-algorithm-optimization-part-1-b2c99887167f'



# Initialize a 2-D list with initial values described by the problem. Returns board
def setBoard():
    board = list()
    sudokuBoard = '''200080300
060070084
030500209
000105408
000000000
402706000
301007040
720040060
004010003'''
    rows = sudokuBoard.split('\n')
    for row in rows:
        column = list()
        for character in row:
            digit = int(character)
            column.append(digit)
        board.append(column)
    return board

# The resulting board is:
'''
[[2, 0, 0, 0, 8, 0, 3, 0, 0], 
 [0, 6, 0, 0, 7, 0, 0, 8, 4], 
 [0, 3, 0, 5, 0, 0, 2, 0, 9], 
 [0, 0, 0, 1, 0, 5, 4, 0, 8], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [4, 0, 2, 7, 0, 6, 0, 0, 0], 
 [3, 0, 1, 0, 0, 7, 0, 4, 0], 
 [7, 2, 0, 0, 4, 0, 0, 6, 0], 
 [0, 0, 4, 0, 1, 0, 0, 0, 3]]
'''


def findEmpty(board):
    '''
    Find next empty space in Sudoku board and return dimensions
    '''
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0 :
                return row, col
    return None


def isValid(board, num, pos):
    '''
    Check whether a specific number can be used for specific dimensions
    '''
    row, col = pos
    # Check if all row elements include this number
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check if all column elements include this number
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already included in the block
    rowBlockStart = 3* (row // 3)
    colBlockStart = 3* (col // 3)

    rowBlockEnd = rowBlockStart + 3
    colBlockEnd = colBlockStart + 3
    for i in range(rowBlockStart, rowBlockEnd):
        for j in range(colBlockStart, colBlockEnd):
            if board[i][j] == num:
                return False

    return True



def allowedValues(board, row, col):
    '''
    The allowedValues() function extracts for each cell a list of legitimate numbers.
    '''
    numbersList = list()

    for number in range(1,10):

        found = False
        # Check if all row elements include this number
        for j in range(9):
            if board[row][j] == number:
                found = True
                break
        # Check if all column elements include this number
        if found == True:
            continue
        else:
            for i in range(9):
                if board[i][col] == number:
                    found = True
                    break

        # Check if the number is already included in the block
        if found == True:
            continue
        else:
            rowBlockStart = 3* (row // 3)
            colBlockStart = 3* (col // 3)

            rowBlockEnd = rowBlockStart + 3
            colBlockEnd = colBlockStart + 3
            for i in range(rowBlockStart, rowBlockEnd):
                for j in range(colBlockStart, colBlockEnd):
                    if board[i][j] == number:
                        found = True
                        break
        if found == False:
            numbersList.append(number)
    return numbersList


def cacheValidValues(board):
    '''
    Store in a dictionary the legitimate values for each individual cell
    '''
    cache = dict()
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                cache[(i,j)] = allowedValues(board, i, j)
    return cache


'''
Implement backtracking algorithm
Search for the next empty cell. If none is found, then we have already solved the puzzle, if not move to step 2.
Make a guess on the correct number by iterating numbers 1-9 and simply examine whether it is a valid solution, given the already established numbers in the board.
If a valid number is found, call the solve() function recursively and make a guess for the next empty cell.
If none of numbers 1-9 is valid, previous call of the function will reset the value of the cell to 0 and continue iterating to find the next valid number.
'''

# Solve Sudoku using backtracking
def solveWithCache(board, cache):
    '''
    This function is expecting the dictionary cache in its parameters list and this time iterates only through 
    the list of legitimate values for each cell instead of all numbers 1-9.
    '''
    blank = findEmpty(board)
    if not blank:
        return True
    else:
        row, col = blank

    for value in cache[(row,col)]:
        if isValid(board, value, blank):
            board[row][col] = value

            if solveWithCache(board, cache):
                return True

            board[row][col] = 0
    return False

board = [[2, 0, 0, 0, 8, 0, 3, 0, 0], 
 [0, 6, 0, 0, 7, 0, 0, 8, 4], 
 [0, 3, 0, 5, 0, 0, 2, 0, 9], 
 [0, 0, 0, 1, 0, 5, 4, 0, 8], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [4, 0, 2, 7, 0, 6, 0, 0, 0], 
 [3, 0, 1, 0, 0, 7, 0, 4, 0], 
 [7, 2, 0, 0, 4, 0, 0, 6, 0], 
 [0, 0, 4, 0, 1, 0, 0, 0, 3]]

cache = cacheValidValues(board)
print(cache)

solution = solveWithCache(board, cache)
print(solution)