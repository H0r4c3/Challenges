'https://py.checkio.org/en/mission/sudokusolver/'

'''
Input: The initial 9x9 grid composed by integers as a list of lists.

Output: The result of the sudoku as a list of lists.
'''
import numpy as np

def split_the_grid_in_small_squares(grid_arr):
    '''
    Split the grid in small squares and make a list with them
    '''
    ss_list = list()
    
    for m in range(0,9,3):
        for n in range(0,9,3):
            ss = grid_arr[m:m+3, n:n+3]
            ss_list.append(ss)
            
    return ss_list
    
    
def find_the_neighbours_for_each_small_square(grid_arr, square_nr):
    '''
    Make a dictionary with vertical neighbours and horizontal neighbours for each small square
    '''
    
    '''
    0 1 2
    3 4 5
    6 7 8
    '''
    
    
    ss_list = split_the_grid_in_small_squares(grid_arr)
    
    hn_dict = {0:(ss_list[1], ss_list[2]), 1:(ss_list[0], ss_list[2]), 2:(ss_list[0], ss_list[1]), 
            3:(ss_list[4], ss_list[5]), 4:(ss_list[3], ss_list[5]), 5:(ss_list[3], ss_list[4]), 
            6:(ss_list[7], ss_list[8]), 7:(ss_list[6], ss_list[8]), 8:(ss_list[6], ss_list[7])}
    
    vn_dict = {0:(ss_list[3], ss_list[6]), 1:(ss_list[4], ss_list[7]), 2:(ss_list[5], ss_list[8]), 
            3:(ss_list[0], ss_list[6]), 4:(ss_list[1], ss_list[7]), 5:(ss_list[2], ss_list[8]), 
            6:(ss_list[0], ss_list[3]), 7:(ss_list[1], ss_list[4]), 8:(ss_list[2], ss_list[5])}
    
    hn = hn_dict[square_nr]
    vn = vn_dict[square_nr]
    
    return hn, vn
    
    
def find_the_small_square(grid_arr, row, column):
    '''
    Decide in which small square is positioned the element [row, column]
    and return the small square.
    '''
    if row in [0,1,2]:
        m = 0
        x = 0
    elif row in [3,4,5]:
        m = 3
        x = 1
    elif row in [6,7,8]:
        m = 6
        x = 2
    else:
        pass
        
    if column in [0,1,2]:
        n = 0
        y = 0
    elif column in [3,4,5]:
        n = 3
        y = 1
    elif column in [6,7,8]:
        n = 6
        y = 2
    else:
        pass
    
    square_nr = x*3 + y
    
    small_square = grid_arr[m:m+3, n:n+3]
    
    return small_square, square_nr


def find_number_of_zeros_h(small_square, r):
    '''
    Calculate the number of zeros in the row of small square where the analyzed position is
    '''
    # Find the row in the small square where the analyzed digit is positioning
    if r == 0:
        r_ss = 0
    elif r == 1:
        r_ss = 1
    elif r == 2:
        r_ss = 2
    elif r == 3:
        r_ss = 0
    elif r == 4:
        r_ss = 1
    elif r == 5:
        r_ss = 2
    elif r == 6:
        r_ss = 0
    elif r == 7:
        r_ss = 1
    elif r == 8:
        r_ss = 2
    else:
        pass
    
    # Extract the row from the small square  
    global row_ss  
    row_ss = small_square[r_ss, :]
    
    
    # Verify the number of 0 in the column of the small square
    if list(row_ss).count(0) == 1:
        return 1
    if list(row_ss).count(0) == 2:
        return 2
    else:
        return 3
    
    
def find_number_of_zeros_v(small_square, c):
    '''
    Calculate the number of zeros in the column of small square where the analyzed position is
    '''
    # Find the column in the small square where the analyzed digit is positioning
    if c == 0:
        c_ss = 0
    elif c == 1:
        c_ss = 1
    elif c == 2:
        c_ss = 2
    elif c == 3:
        c_ss = 0
    elif c == 4:
        c_ss = 1
    elif c == 5:
        c_ss = 2
    elif c == 6:
        c_ss = 0
    elif c == 7:
        c_ss = 1
    elif c == 8:
        c_ss = 2
    else:
        pass
    
    # Extract the column from the small square
    global col_ss
    col_ss = small_square[:, c_ss]
    
    # Verify the number of 0 in the column of the small square
    if list(col_ss).count(0) == 1:
        return 1
    if list(col_ss).count(0) == 2:
        return 2
    else:
        return 3
    
    
def possible_digits(actual_digits, other_digits):
    '''
    Create a list with possible digits having 2 lists: 1. list with actual digits, 2. list with digits to be eliminated
    '''
    poss_digits_list = [item for item in actual_digits if item not in other_digits]
    
    return poss_digits_list


def possible_digits_final(grid_arr, r, c):
    '''
    Eliminate the digits from row, column and small square
    '''
    
    # Select the whole row nr. r
    row_r = grid_arr[r, :]
    
    actual_digits = range(1, 10)
     
    # Eliminate the digits from row_r
    possible_after_row = possible_digits(actual_digits, row_r)
    
    # Stop the checks if remains only 1 digit after the row check
    if len(possible_after_row) == 1:
        return possible_after_row
    
    # Select the whole column nr. c
    col_c = grid_arr[:, c]
    
    # Eliminate the digits from col_c
    possible_after_column = possible_digits(possible_after_row, col_c)
    
    # Stop the checks if remains only 1 digit after the column check
    if len(possible_after_column) == 1:
        return possible_after_column
    
    # Select the small square nr. x + y
    square_rr3_cc3, square_nr = find_the_small_square(grid_arr, r, c)
    
    # Eliminate the digits from square_rr3_cc3
    possible_after_small_square = possible_digits(possible_after_column, square_rr3_cc3)
    
    # Stop the checks if remains only 1 digit after small square check
    if len(possible_after_small_square) == 1:
        return possible_after_small_square
    
    # Find the number of zeros on the row or column of the analyzed empty spot (0)
    h_zero = find_number_of_zeros_h(square_rr3_cc3, r)
    v_zero = find_number_of_zeros_v(square_rr3_cc3, c)
        
    # Verify the possible digits in neighbours small squares:
    # Select the horizontal neighbours and vertical neighbours of the small square
    hn, vn = find_the_neighbours_for_each_small_square(grid_arr, square_nr)
    hn1 = hn[0]
    hn2 = hn[1]
    vn1 = vn[0]
    vn2 = vn[1]
    
    # Check if the possible digits are in horizontal neighbours AND in vertical neighbours
    if h_zero == 3 or v_zero == 3: # No digits in the row or column of ss (3 zeros)
        for digit in possible_after_small_square:
            
            if (digit in hn1) and (digit in hn2) and (digit in vn1) and (digit in vn2):
                return [digit]
            
    # Check if the possible digits are in horizontal neighbours
    if h_zero == 1: # 2 digits in the row of ss (1 zero)
        digit_list = list()
        for digit in possible_after_small_square:
            if (digit in hn1) and (digit in hn2):
                digit_list.append(digit)
            else:
                pass
    
        # If it's only one digit in digit_list, that's the one!        
        if len(digit_list) == 1:
            return digit_list
        else:
            pass
    
    
    # Check if the possible digits are in vertical neighbours
    if v_zero == 1: # 2 digits in the column of ss (1 zero)
        digit_list = list()       
        for digit in possible_after_small_square:
            if (digit in vn1) and (digit in vn2):
                digit_list.append(digit)
            else:
                pass
    
        # If it's only one digit in digit_list, that's the one!    
        if len(digit_list) == 1:
            return digit_list
        else:
            pass
    
    
    
    # Check if the possible digits are in 2 horizontal neighbours and in 1 vertical neighbor   
    
       
    if h_zero == 2: # 1 digit in the row of ss and 2 zeros -> must be in h1 and h2 and in one of (vn1 or vn2) 
                 # Rule for vn1 or vn2: the digit must be in hn in column col_ss, the digit must be in ss in column cdss, the element in ss must be in column cess, all 3 different)
        digit_list = list()
        
        for digit in possible_after_small_square:
            
            #row_ss is the whole row of digit in small square
            cess = np.where(row_ss != 0)[0]  # position of non-zero element in small square in same row with digit
            cdhn1 = np.where(vn1==digit)[1]  # number of column of digit in vn1
            cdhn2 = np.where(vn2==digit)[1]  # number of column of digit in vn2
            
            if (digit in hn1) and (digit in hn2):
                if digit in vn1:
                    if cdhn1 != cess:
                        
                        digit_list.append(digit)
                elif digit in vn2:
                    if cdhn2 != cess:
                        
                        digit_list.append(digit)
            else:
                pass
                
            # If it's only one digit in digit_list, that's the one!    
            if len(digit_list) == 1:
                return digit_list
            else:
                pass
            
    
    # Check if the possible digits are in 2 vertical neighbours and in 1 horizontal neighbor
           
    if v_zero == 2: # 1 digit in the column of ss and 2 zeros -> must be in vn1 and vn2 and in one of (hn1 or hn2) 
                    # Rule for hn1 or hn2: the digit must be in hn in row row_ss, the digit must be in ss in row rdss, the element in ss must be in row ress, all 3 different)
        digit_list = list()
        
        for digit in possible_after_small_square:
            #row_ss is the whole row of digit in small square
            ress = np.where(col_ss != 0)[0]  # position of non-zero element in small square in same column with digit
            rdhn1 = np.where(hn1==digit)[0]  # number of row of digit in hn1
            rdhn2 = np.where(hn2==digit)[0]  # number of row of digit in hn2
            
            if (digit in vn1) and (digit in vn2):
                if digit in hn1:
                    if rdhn1 != ress:
                        
                        digit_list.append(digit)
                elif digit in hn2:
                    if rdhn2 != ress:
                        
                        digit_list.append(digit)
            else:
                pass     
    
        # If it's only one digit in digit_list, that's the one!    
        if len(digit_list) == 1:
            return digit_list
        else:
            pass
    
    return possible_after_small_square


def create_dictionary_possible_digits(grid_arr):
    '''
    Create a dictionary having as key = position in grid or digit != 0, value = list with all possible digits, after elimination of taken digits.
    This method is only for Testing Purpose.
    '''
    # Replace all the 0 with a list with all possible digits in that position
    poss_dict = dict()
    for r in range(0, 9):
        for c in range(0, 9):
            if grid_arr[r, c] == 0:
                new_item = possible_digits_final(grid_arr, r, c)
                poss_dict[r, c] = new_item
            else:
                new_item = grid_arr[r, c]
                poss_dict[r, c] = new_item
                
    return poss_dict


def replace_zero_with_digit(grid_arr):
    '''
    Parse the grid, and, where is a 0, calculate all possible digits; 
    if it's only ONE possibility, replace the 0 with it, and start again
    '''
    global replacements # how many digits were replaced
    global st # how many times the script is starting from the beginning
    global replacements_arr # a grid that contains only the replacements
    
    # initialize a dictionary where will be put the lists with possible digits
    dict_with_possible_digits = dict()
    st += 1
    
    for r in range(0, 9):
        for c in range(0, 9):
            if grid_arr[r, c] == 0:
                new_item = possible_digits_final(grid_arr, r, c)
                dict_with_possible_digits[(r, c)] = new_item
                if len(new_item) == 1:
                    
                    replacements_arr[r, c] = new_item[0]
                    grid_arr[r, c] = new_item[0]
                    replacements += 1
                    dict_with_possible_digits[(r, c)] = new_item[0]
                    replace_zero_with_digit(grid_arr)
                else:
                    pass
            else:
                dict_with_possible_digits[(r, c)] = grid_arr[r, c]      
    
    return grid_arr, dict_with_possible_digits    
    

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

    
def find_zeros(grid_arr):
    '''
    Find next 0 in Sudoku grid and return row and column
    '''
    for row in range(9):
        for col in range(9):
            if grid_arr[row][col] == 0 :
                return row, col
    return None   
    

def replace_with_values_from_dict(grid_arr, dict_with_possible_digits):
    '''
    Replace every 0 with value from dict_with_possible_digits
    '''
    
    blank = find_zeros(grid_arr)
    
    if not blank:
        return True, grid_arr
    else:
        row, col = blank

    for value in dict_with_possible_digits[(row, col)]:
        if isValid(grid_arr, value, blank):
            print(value)
            grid_arr[row][col] = value

            if replace_with_values_from_dict(grid_arr, dict_with_possible_digits):
                return True, grid_arr

            grid_arr[row][col] = 0
            
    return False


def all_steps(grid):
    grid_arr = np.array(grid)
    
    split_the_grid_in_small_squares(grid_arr)

    grid_arr, dict_with_possible_digits = replace_zero_with_digit(grid_arr)
    
    return grid_arr, dict_with_possible_digits             
    

# Return the solution of the sudoku.
def checkio_(grid):
    global replacements # how many digits were replaced
    global st # how many times the script is starting from the beginning
    global replacements_arr # a grid that contains only the replacements
    
    replacements = 0
    st = 0
    replacements_arr = np.array([[0 for i in range(9)] for j in range(9)])

    grid_arr, dict_with_possible_digits = all_steps(grid)
    print(f'grid_arr = {grid_arr}')
    print(f'dict_with_possible_digits = {dict_with_possible_digits}')
    
    verification, grid_arr = replace_with_values_from_dict(grid_arr, dict_with_possible_digits)
    print(grid_arr)
    
    if verification:
        return grid_arr.tolist()
    else:
        print('NO Solution!!!')
        
        
        
# Best Solution: 
# https://py.checkio.org/mission/sudokusolver/publications/przemyslaw.daniel/python-3/17-liner-cleanest-recursive/?ordering=most_voted&filtering=all

def is_correct(value, x, y, grid):
    horizontal = set(grid[x])
    vertical = {grid[i][y] for i in range(9)}
    r3x3 = [(i, j) for i in range(3) for j in range(3)]
    square = {grid[x//3*3+i][y//3*3+j] for i, j in r3x3}
    grid[x][y] = value
    return value not in (horizontal | vertical | square)

def checkio(grid):
    r9x9 = [(i, j) for i in range(9) for j in range(9)]
    empty = [(i, j) for i, j in r9x9 if not grid[i][j]]
    if not empty: return grid
    x, y = empty.pop()
    for k in range(1, 10):
        if is_correct(k, x, y, grid) and checkio(grid):
            return grid
    grid[x][y] = 0
    


if __name__ == '__main__':
    
    #My TESTS:
    # assert checkio([[0, 2, 3, 4, 5, 6, 7, 8, 9],
    #                 [9, 0, 7, 6, 4, 3, 2, 1, 5],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[1, 2, 3, 4, 5, 6, 7, 8, 9],
    #                                                   [9, 8, 7, 6, 4, 3, 2, 1, 5],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0]], "Test1: Row condition"
    
    # assert checkio([[0, 9, 0, 0, 0, 0, 0, 0, 0],
    #                 [2, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [3, 7, 0, 0, 0, 0, 0, 0, 0],
    #                 [4, 6, 0, 0, 0, 0, 0, 0, 0],
    #                 [5, 4, 0, 0, 0, 0, 0, 0, 0],
    #                 [6, 3, 0, 0, 0, 0, 0, 0, 0],
    #                 [7, 2, 0, 0, 0, 0, 0, 0, 0],
    #                 [8, 1, 0, 0, 0, 0, 0, 0, 0],
    #                 [9, 5, 0, 0, 0, 0, 0, 0, 0]]) == [[1, 9, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [2, 8, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [3, 7, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [4, 6, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [5, 4, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [6, 3, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [7, 2, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [8, 1, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [9, 5, 0, 0, 0, 0, 0, 0, 0]], "Test2: Column condition"
                    
    # assert checkio([[1, 2, 3, 0, 0, 0, 0, 0, 0],
    #                 [4, 5, 6, 0, 0, 0, 0, 0, 0],
    #                 [7, 8, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 1, 2, 3, 0, 0, 0],
    #                 [0, 0, 0, 4, 0, 6, 0, 0, 0],
    #                 [0, 0, 0, 7, 8, 9, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 2, 3],
    #                 [0, 0, 0, 0, 0, 0, 4, 5, 6],
    #                 [0, 0, 0, 0, 0, 0, 7, 8, 9]]) == [[1, 2, 3, 0, 0, 0, 0, 0, 0],
    #                                                   [4, 5, 6, 0, 0, 0, 0, 0, 0],
    #                                                   [7, 8, 9, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 1, 2, 3, 0, 0, 0],
    #                                                   [0, 0, 0, 4, 5, 6, 0, 0, 0],
    #                                                   [0, 0, 0, 7, 8, 9, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 1, 2, 3],
    #                                                   [0, 0, 0, 0, 0, 0, 4, 5, 6],
    #                                                   [0, 0, 0, 0, 0, 0, 7, 8, 9]], "Test3: Small square condition"
                    
    
    # assert checkio([[0, 2, 3, 9, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 1, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 1],
    #                 [0, 0, 0, 0, 0, 3, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 6, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 9, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[1, 2, 3, 9, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 1, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 1],
    #                                                   [0, 0, 0, 0, 0, 3, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 6, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 9, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 9, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0]], "Test4: Small square + Neighbor small squares condition"   
                    
    
    # assert checkio([[0, 2, 3, 9, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 8, 0, 1, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 1],
    #                 [0, 0, 0, 0, 0, 3, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 6, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 9, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 8, 0, 0, 0, 0]]) == [[1, 2, 3, 9, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 8, 0, 1, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 1],
    #                                                   [0, 0, 0, 0, 0, 3, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 6, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 9, 0, 0, 0, 0],
    #                                                   [0, 0, 0, 0, 8, 0, 0, 0, 0]], "Test5: Small square + Neighbor small squares condition with 2 possible digits"
    
    
    # assert checkio([[3, 7, 1, 6, 8, 4, 9, 5, 2],
    #                 [0, 4, 9, 7, 0, 0, 0, 0, 0],
    #                 [5, 0, 0, 0, 0, 0, 4, 7, 0],
    #                 [0, 8, 7, 0, 0, 0, 5, 3, 4],
    #                 [0, 0, 0, 3, 0, 7, 2, 0, 0],
    #                 [2, 0, 3, 8, 0, 0, 1, 9, 7],
    #                 [0, 0, 0, 0, 7, 0, 0, 4, 9],
    #                 [0, 0, 0, 0, 0, 3, 7, 2, 0],
    #                 [7, 0, 0, 4, 9, 8, 6, 1, 0]]) == [[3, 7, 1, 6, 8, 4, 9, 5, 2],
    #                                                   [0, 4, 9, 7, 0, 0, 0, 0, 0],
    #                                                   [5, 0, 0, 0, 0, 0, 4, 7, 0],
    #                                                   [0, 8, 7, 0, 0, 0, 5, 3, 4],
    #                                                   [0, 0, 0, 3, 0, 7, 2, 0, 0],
    #                                                   [2, 0, 3, 8, 4, 0, 1, 9, 7],
    #                                                   [0, 0, 0, 0, 7, 0, 0, 4, 9],
    #                                                   [0, 0, 0, 0, 0, 3, 7, 2, 0],
    #                                                   [7, 0, 0, 4, 9, 8, 6, 1, 0]], "Test6: Unique digits ROWS"
    
    # assert checkio([[3, 0, 5, 0, 0, 2, 0, 0, 7],
    #                 [7, 4, 0, 8, 0, 0, 0, 0, 0],
    #                 [1, 9, 0, 7, 0, 3, 0, 0, 0],
    #                 [6, 7, 0, 0, 3, 8, 0, 0, 4],
    #                 [8, 0, 0, 0, 0, 0, 7, 0, 9],
    #                 [4, 0, 0, 0, 7, 0, 0, 3, 8],
    #                 [9, 0, 4, 5, 2, 1, 0, 7, 6],
    #                 [5, 0, 7, 3, 0, 9, 4, 2, 1],
    #                 [2, 0, 0, 4, 0, 7, 9, 0, 0]]) == [[3, 0, 5, 0, 0, 2, 0, 0, 7],
    #                                                   [7, 4, 0, 8, 0, 0, 0, 0, 0],
    #                                                   [1, 9, 0, 7, 0, 3, 0, 0, 0],
    #                                                   [6, 7, 0, 0, 3, 8, 0, 0, 4],
    #                                                   [8, 0, 0, 0, 0, 4, 7, 0, 9],
    #                                                   [4, 0, 0, 0, 7, 0, 0, 3, 8],
    #                                                   [9, 0, 4, 5, 2, 1, 0, 7, 6],
    #                                                   [5, 0, 7, 3, 0, 9, 4, 2, 1],
    #                                                   [2, 0, 0, 4, 0, 7, 9, 0, 0]], "Test6: Unique digits COLUMNS"
                         
                    
    # print('Test PASSED!')       
                    
                    
                    
    # print('My Verification Tests DONE!!!')
                    
    #These "asserts" using only for self-checking and not necessary for auto-testing
         
    assert checkio([[0, 7, 1, 6, 8, 4, 0, 0, 0],
                    [0, 4, 9, 7, 0, 0, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 0, 0, 0, 0, 5, 0, 4],
                    [0, 0, 0, 3, 0, 7, 0, 0, 0],
                    [2, 0, 3, 0, 0, 0, 0, 9, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [0, 0, 0, 0, 0, 3, 7, 2, 0],
                    [0, 0, 0, 4, 9, 8, 6, 1, 0]]) == [[3, 7, 1, 6, 8, 4, 9, 5, 2],
                                                      [8, 4, 9, 7, 2, 5, 3, 6, 1],
                                                      [5, 6, 2, 9, 3, 1, 4, 7, 8],
                                                      [6, 8, 7, 2, 1, 9, 5, 3, 4],
                                                      [9, 1, 4, 3, 5, 7, 2, 8, 6],
                                                      [2, 5, 3, 8, 4, 6, 1, 9, 7],
                                                      [1, 3, 6, 5, 7, 2, 8, 4, 9],
                                                      [4, 9, 8, 1, 6, 3, 7, 2, 5],
                                                      [7, 2, 5, 4, 9, 8, 6, 1, 3]], "first"
                    
    print(f'first Sudoku solved!!!')
                    
    assert checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4],
                    [0, 0, 1, 0, 3, 0, 5, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 5, 9, 7, 2, 6, 4, 0],
                    [0, 0, 0, 6, 0, 1, 0, 0, 0],
                    [0, 2, 6, 3, 8, 5, 9, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3, 0, 5, 0, 2, 0, 0],
                    [8, 0, 0, 4, 9, 7, 0, 0, 6]]) == [[5, 6, 8, 7, 1, 9, 3, 2, 4],
                                                      [9, 7, 1, 2, 3, 4, 5, 6, 8],
                                                      [2, 3, 4, 5, 6, 8, 7, 9, 1],
                                                      [1, 8, 5, 9, 7, 2, 6, 4, 3],
                                                      [3, 9, 7, 6, 4, 1, 8, 5, 2],
                                                      [4, 2, 6, 3, 8, 5, 9, 1, 7],
                                                      [6, 1, 9, 8, 2, 3, 4, 7, 5],
                                                      [7, 4, 3, 1, 5, 6, 2, 8, 9],
                                                      [8, 5, 2, 4, 9, 7, 1, 3, 6]], "second"
    
    print('Local tests done!!!')