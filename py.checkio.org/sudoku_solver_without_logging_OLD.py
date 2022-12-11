'https://py.checkio.org/en/mission/sudokusolver/'

'''
Input: The initial 9x9 grid composed by integers as a list of lists.

Output: The result of the sudoku as a list of lists.
'''
import numpy as np

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\py.checkio.org\sudoku_solver.log'



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


def convert_dict_into_three_dicts(my_dict):
    '''
    Having a dictionary with keys = tuples (dict_with_possible_digits), convert it into 3 types of dictionaries:
    - 1. dictionary type having as keys all the equal first elements of tuples and as values a list of values for those keys in the old dict
    - 2. dictionary type having as keys all the equal second elements of tuples and as values a list of values for those keys in the old dict
    - 3. dictionary type having as values the lists from small squares
    '''
    
    # analyzing the possible digits in every row
    dict_rows_0 = {0 : [value for key, value in my_dict.items() if key[0] == 0]}
    dict_rows_1 = {1 : [value for key, value in my_dict.items() if key[0] == 1]}
    dict_rows_2 = {2 : [value for key, value in my_dict.items() if key[0] == 2]}
    dict_rows_3 = {3 : [value for key, value in my_dict.items() if key[0] == 3]}
    dict_rows_4 = {4 : [value for key, value in my_dict.items() if key[0] == 4]}
    dict_rows_5 = {5 : [value for key, value in my_dict.items() if key[0] == 5]}
    dict_rows_6 = {6 : [value for key, value in my_dict.items() if key[0] == 6]}
    dict_rows_7 = {7 : [value for key, value in my_dict.items() if key[0] == 7]}
    dict_rows_8 = {8 : [value for key, value in my_dict.items() if key[0] == 8]}
    #dict_rows_8 = {key[0] : [value for key, value in my_dict.items() if key[0] == 8] for key in my_dict.keys() if key[0] == 8}
    list_dicts_rows = [dict_rows_0, dict_rows_1, dict_rows_2, dict_rows_3, dict_rows_4, dict_rows_5, dict_rows_6, dict_rows_7, dict_rows_8]
    
    # analyzing the possible digits in every column
    dict_cols_0 = {0 : [value for key, value in my_dict.items() if key[1] == 0]}
    dict_cols_1 = {1 : [value for key, value in my_dict.items() if key[1] == 1]}
    dict_cols_2 = {2 : [value for key, value in my_dict.items() if key[1] == 2]}
    dict_cols_3 = {3 : [value for key, value in my_dict.items() if key[1] == 3]}
    dict_cols_4 = {4 : [value for key, value in my_dict.items() if key[1] == 4]}
    dict_cols_5 = {5 : [value for key, value in my_dict.items() if key[1] == 5]}
    dict_cols_6 = {6 : [value for key, value in my_dict.items() if key[1] == 6]}
    dict_cols_7 = {7 : [value for key, value in my_dict.items() if key[1] == 7]}
    dict_cols_8 = {8 : [value for key, value in my_dict.items() if key[1] == 8]}
    #dict_cols_8 = {key[1] : [value for key, value in my_dict.items() if key[1] == 8] for key in my_dict.keys() if key[1] == 8}
    list_dicts_cols = [dict_cols_0, dict_cols_1, dict_cols_2, dict_cols_3, dict_cols_4, dict_cols_5, dict_cols_6, dict_cols_7, dict_cols_8]

    # analyzing the possible digits in every small square
    dict_small_square_0 = {0 : [value for key, value in my_dict.items() if key in [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]]}
    dict_small_square_1 = {1 : [value for key, value in my_dict.items() if key in [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]]}
    dict_small_square_2 = {2 : [value for key, value in my_dict.items() if key in [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)]]}
    dict_small_square_3 = {3 : [value for key, value in my_dict.items() if key in [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)]]}
    dict_small_square_4 = {4 : [value for key, value in my_dict.items() if key in [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)]]}
    dict_small_square_5 = {5 : [value for key, value in my_dict.items() if key in [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)]]}
    dict_small_square_6 = {6 : [value for key, value in my_dict.items() if key in [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)]]}
    dict_small_square_7 = {7 : [value for key, value in my_dict.items() if key in [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)]]}
    dict_small_square_8 = {8 : [value for key, value in my_dict.items() if key in [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]]}
    
    list_dicts_small_squares = [dict_small_square_0, dict_small_square_1, dict_small_square_2, dict_small_square_3, dict_small_square_4, 
                                dict_small_square_5, dict_small_square_6, dict_small_square_7, dict_small_square_8]
    
    return list_dicts_rows, list_dicts_cols, list_dicts_small_squares


def find_unique_digit_in_list(list_dicts_value):
    '''
    Find the unique digits into the lists with possible digits
    '''
    
    # eliminate the digit not in a list and the list with len = 1
    new_list = [item for item in list_dicts_value if type(item) == list and len(item) > 1]

    # flatten the list
    my_list_flat = [item for sublist in new_list for item in sublist]

    # find the unique digits list
    unique_digits_list = [item for item in my_list_flat if my_list_flat.count(item) == 1]
    if unique_digits_list == []:
        return [], None
    else:
        pass

    # find the index of the unique digit
    idx = -1
    for item in list_dicts_value:
        idx += 1
        if (type(item) == list) and (len(item) > 1):
            if unique_digits_list[0] in item:
                return unique_digits_list, idx
            else:
                pass
        else:
            pass
                      

def find_all_unique_digits(list_dicts_rows, list_dicts_cols, list_dicts_small_squares):
    global r_c_ss # decide what was analyzed (ROWs or COLUMNs or SMALL SQUAREs)
    global idx, ind
    r_c_ss = 'rows' # decide what is analyzing (ROWs or COLUMNs or SMALL SQUAREs)
    unique_digit_row_0, idxr0 = find_unique_digit_in_list(list_dicts_rows[0].get(0))
    unique_digit_row_1, idxr1 = find_unique_digit_in_list(list_dicts_rows[1].get(1))
    unique_digit_row_2, idxr2 = find_unique_digit_in_list(list_dicts_rows[2].get(2))
    unique_digit_row_3, idxr3 = find_unique_digit_in_list(list_dicts_rows[3].get(3))
    unique_digit_row_4, idxr4 = find_unique_digit_in_list(list_dicts_rows[4].get(4))
    unique_digit_row_5, idxr5 = find_unique_digit_in_list(list_dicts_rows[5].get(5))
    unique_digit_row_6, idxr6 = find_unique_digit_in_list(list_dicts_rows[6].get(6))
    unique_digit_row_7, idxr7 = find_unique_digit_in_list(list_dicts_rows[7].get(7))
    unique_digit_row_8, idxr8 = find_unique_digit_in_list(list_dicts_rows[8].get(8))
    unique_digit_row_list = [unique_digit_row_0, unique_digit_row_1, unique_digit_row_2, unique_digit_row_3, unique_digit_row_4, 
                             unique_digit_row_5, unique_digit_row_6, unique_digit_row_7, unique_digit_row_8]
    idxr_list = [idxr0, idxr1, idxr2, idxr3, idxr4, idxr5, idxr6, idxr7, idxr8]
    
    # For ROWs, idx = column, ind = row, in grid_arr
    # the position is grid_arr[ind, idx]
    unique_digits_list, idx, ind = check_list_of_lists_for_digit(unique_digit_row_list, idxr_list)
    
    if unique_digits_list:
        return unique_digits_list, idx, ind
    
    r_c_ss = 'columns'
    unique_digit_col_0, idxc0 = find_unique_digit_in_list(list_dicts_cols[0].get(0))
    unique_digit_col_1, idxc1 = find_unique_digit_in_list(list_dicts_cols[1].get(1))
    unique_digit_col_2, idxc2 = find_unique_digit_in_list(list_dicts_cols[2].get(2))
    unique_digit_col_3, idxc3 = find_unique_digit_in_list(list_dicts_cols[3].get(3))
    unique_digit_col_4, idxc4 = find_unique_digit_in_list(list_dicts_cols[4].get(4))
    unique_digit_col_5, idxc5 = find_unique_digit_in_list(list_dicts_cols[5].get(5))
    unique_digit_col_6, idxc6 = find_unique_digit_in_list(list_dicts_cols[6].get(6))
    unique_digit_col_7, idxc7 = find_unique_digit_in_list(list_dicts_cols[7].get(7))
    unique_digit_col_8, idxc8 = find_unique_digit_in_list(list_dicts_cols[8].get(8))
    unique_digit_col_list = [unique_digit_col_0, unique_digit_col_1, unique_digit_col_2, unique_digit_col_3, unique_digit_col_4, 
                             unique_digit_col_5, unique_digit_col_6, unique_digit_col_7, unique_digit_col_8]
    idxc_list = [idxc0, idxc1, idxc2, idxc3, idxc4, idxc5, idxc6, idxc7, idxc8]
    
    # For COLUMNs, idx = row, ind = column, in grid_arr
    # the position is grid_arr[idx, ind]
    unique_digits_list, idx, ind = check_list_of_lists_for_digit(unique_digit_col_list, idxc_list)
    
    if unique_digits_list:
        return unique_digits_list, idx, ind
    
    r_c_ss = 'small squares'
    unique_digit_small_square_0, idxss0 = find_unique_digit_in_list(list_dicts_small_squares[0].get(0))
    unique_digit_small_square_1, idxss1 = find_unique_digit_in_list(list_dicts_small_squares[1].get(1))
    unique_digit_small_square_2, idxss2 = find_unique_digit_in_list(list_dicts_small_squares[2].get(2))
    unique_digit_small_square_3, idxss3 = find_unique_digit_in_list(list_dicts_small_squares[3].get(3))
    unique_digit_small_square_4, idxss4 = find_unique_digit_in_list(list_dicts_small_squares[4].get(4))
    unique_digit_small_square_5, idxss5 = find_unique_digit_in_list(list_dicts_small_squares[5].get(5))
    unique_digit_small_square_6, idxss6 = find_unique_digit_in_list(list_dicts_small_squares[6].get(6))
    unique_digit_small_square_7, idxss7 = find_unique_digit_in_list(list_dicts_small_squares[7].get(7))
    unique_digit_small_square_8, idxss8 = find_unique_digit_in_list(list_dicts_small_squares[8].get(8))
    unique_digit_ss_list = [unique_digit_small_square_0, unique_digit_small_square_1, unique_digit_small_square_2, unique_digit_small_square_3, unique_digit_small_square_4, 
                             unique_digit_small_square_5, unique_digit_small_square_6, unique_digit_small_square_7, unique_digit_small_square_8]
    idxss_list = [idxss0, idxss1, idxss2, idxss3, idxss4, idxss5, idxss6, idxss7, idxss8]
    
    # For SMALL SQUAREs, idx = position in small square, ind = nr. of small square, in grid_arr
    # the position is grid_arr[row , column]
    unique_digits_list, idx, ind = check_list_of_lists_for_digit(unique_digit_ss_list, idxss_list)
    
    if unique_digits_list:
        return unique_digits_list, idx, ind
    else:
        r_c_ss = 'No unique digit found!'
        return [], None, None
    

def check_unique(unique_digits_list, idx):
    if unique_digits_list != []:
        #unique_digit = unique_digit_list
        return unique_digits_list, idx
    else: 
        return [], None
    

def check_list_of_lists_for_digit(unique_digits_list_of_lists, idx_list):
    for item in unique_digits_list_of_lists:
        if item != []:
            ind = unique_digits_list_of_lists.index(item)
            return item, idx_list[ind], ind
    return [], None, None


def where_unique_found(r_c_ss, idx, ind):
    # Decide where was the unique found (ROWs or COLUMNs or SMALL SQUAREs)
    if r_c_ss == 'rows':
        row, column = ind, idx
        
    elif r_c_ss == 'columns':
        row, column = idx, ind
        
    elif r_c_ss == 'small squares':
        # ind = nr. of small square
        # idx = position in small square
        if ind == 0: # small square nr. 0
            if idx == 0: row, column = 0, 0
            elif idx == 1: row, column = 0, 1
            elif idx == 2: row, column = 0, 2
            elif idx == 3: row, column = 1, 0
            elif idx == 4: row, column = 1, 1
            elif idx == 5: row, column = 1, 2
            elif idx == 6: row, column = 2, 0
            elif idx == 7: row, column = 2, 1
            elif idx == 8: row, column = 2, 2
        if ind == 1: # small square nr. 1
            if idx == 0: row, column = 0, 3
            elif idx == 1: row, column = 0, 4
            elif idx == 2: row, column = 0, 5
            elif idx == 3: row, column = 1, 3
            elif idx == 4: row, column = 1, 4
            elif idx == 5: row, column = 1, 5
            elif idx == 6: row, column = 2, 3
            elif idx == 7: row, column = 2, 4
            elif idx == 8: row, column = 2, 5
        if ind == 2: # small square nr. 2
            if idx == 0: row, column = 0, 6
            elif idx == 1: row, column = 0, 7
            elif idx == 2: row, column = 0, 8
            elif idx == 3: row, column = 1, 6
            elif idx == 4: row, column = 1, 7
            elif idx == 5: row, column = 1, 8
            elif idx == 6: row, column = 2, 6
            elif idx == 7: row, column = 2, 7
            elif idx == 8: row, column = 2, 8
        if ind == 0: # small square nr. 3
            if idx == 0: row, column = 3, 0
            elif idx == 1: row, column = 3, 1
            elif idx == 2: row, column = 3, 2
            elif idx == 3: row, column = 4, 0
            elif idx == 4: row, column = 4, 1
            elif idx == 5: row, column = 4, 2
            elif idx == 6: row, column = 5, 0
            elif idx == 7: row, column = 5, 1
            elif idx == 8: row, column = 5, 2
        if ind == 1: # small square nr. 4
            if idx == 0: row, column = 3, 3
            elif idx == 1: row, column = 3, 4
            elif idx == 2: row, column = 3, 5
            elif idx == 3: row, column = 4, 3
            elif idx == 4: row, column = 4, 4
            elif idx == 5: row, column = 4, 5
            elif idx == 6: row, column = 5, 3
            elif idx == 7: row, column = 5, 4
            elif idx == 8: row, column = 5, 5
        if ind == 2: # small square nr. 5
            if idx == 0: row, column = 3, 6
            elif idx == 1: row, column = 3, 7
            elif idx == 2: row, column = 3, 8
            elif idx == 3: row, column = 4, 6
            elif idx == 4: row, column = 4, 7
            elif idx == 5: row, column = 4, 8
            elif idx == 6: row, column = 5, 6
            elif idx == 7: row, column = 5, 7
            elif idx == 8: row, column = 5, 8
        if ind == 0: # small square nr. 6
            if idx == 0: row, column = 6, 0
            elif idx == 1: row, column = 7, 1
            elif idx == 2: row, column = 8, 2
            elif idx == 3: row, column = 6, 0
            elif idx == 4: row, column = 7, 1
            elif idx == 5: row, column = 8, 2
            elif idx == 6: row, column = 6, 0
            elif idx == 7: row, column = 7, 1
            elif idx == 8: row, column = 8, 2
        if ind == 1: # small square nr. 7
            if idx == 0: row, column = 6, 3
            elif idx == 1: row, column = 7, 4
            elif idx == 2: row, column = 8, 5
            elif idx == 3: row, column = 6, 3
            elif idx == 4: row, column = 7, 4
            elif idx == 5: row, column = 8, 5
            elif idx == 6: row, column = 6, 3
            elif idx == 7: row, column = 7, 4
            elif idx == 8: row, column = 8, 5
        if ind == 2: # small square nr. 8
            if idx == 0: row, column = 6, 6
            elif idx == 1: row, column = 7, 7
            elif idx == 2: row, column = 8, 8
            elif idx == 3: row, column = 6, 6
            elif idx == 4: row, column = 7, 7
            elif idx == 5: row, column = 8, 8
            elif idx == 6: row, column = 6, 6
            elif idx == 7: row, column = 7, 7
            elif idx == 8: row, column = 8, 8
            
    elif r_c_ss == 'No unique digit found!':
        pass
    else:
        pass
    
    return row, column


def fill_with_unique_digit(unique_digits_list, grid_arr):
    if unique_digits_list != []:
        row, column = where_unique_found(r_c_ss, idx, ind)
        # Fill the found digit in grid_arr and start over with replace_zero_with_digit(grid_arr)
        grid_arr[row, column] = unique_digits_list[0]
        return grid_arr
    else:
        return grid_arr
    
    
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


def all_steps(grid):
        grid_arr = np.array(grid)
        
        split_the_grid_in_small_squares(grid_arr)

        grid_arr, dict_with_possible_digits = replace_zero_with_digit(grid_arr)
        
        # check if the grid is full (Sudoku is solved)
        if np.all(grid_arr):
            return grid_arr, dict_with_possible_digits
        else:
            pass
        
        # Starting to check the unique digit condition
        list_dicts_rows, list_dicts_cols, list_dicts_small_squares = convert_dict_into_three_dicts(dict_with_possible_digits)
        
        unique_digits_list, idx, ind = find_all_unique_digits(list_dicts_rows, list_dicts_cols, list_dicts_small_squares)
        
        grid_arr = fill_with_unique_digit(unique_digits_list, grid_arr)
        
        return grid_arr, dict_with_possible_digits        
    
def analyze_the_dict_with_possible_digits(dict_with_possible_digits):
    # eliminate the single values and select only the values with 2 elements
    dict_reduced = {key : value for key, value in dict_with_possible_digits.items() if (type(value) == list) and (len(value) == 2)}
    
    return dict_reduced

def replace_with_values_from_dict(grid_arr, dict_with_possible_digits):
    dict_reduced = analyze_the_dict_with_possible_digits(dict_with_possible_digits)
    
    # make copies
    grid_arr2 = np.copy(grid_arr)
    dict_reduced2 = dict.copy(dict_reduced)

    for key, value in dict_reduced2.items():
        for i in [1, 0]:
            r, c = key
            digit = value[i]
            grid_arr2[r, c] = digit
            
            grid_arr2, dict_with_possible_digits = all_steps(grid_arr2)
            
            # check if the grid is full (Sudoku is solved)
            if np.all(grid_arr2):
                return grid_arr2
            else:
                grid_arr2 = np.copy(grid_arr)
                
    return grid_arr2
            
    
    
     

# Return the solution of the sudoku.
def checkio(grid):
    global replacements # how many digits were replaced
    global st # how many times the script is starting from the beginning
    global replacements_arr # a grid that contains only the replacements
    
    replacements = 0
    st = 0
    replacements_arr = np.array([[0 for i in range(9)] for j in range(9)])

    grid_arr, dict_with_possible_digits = all_steps(grid)
    
    # check if the grid is full (Sudoku is solved)
    if np.all(grid_arr):
        return grid_arr.tolist()
    else:
        pass
        
    dict_with_possible_digits = analyze_the_dict_with_possible_digits(dict_with_possible_digits)
    
    grid_arr = replace_with_values_from_dict(grid_arr, dict_with_possible_digits)
        
    return grid_arr.tolist()
    





if __name__ == '__main__':
    
    # My TESTS:
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
                         
                    
    print('Test PASSED!')       
                    
                    
                    
    print('My Verification Tests DONE!!!')
                    
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
                    
    # assert checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4],
    #                 [0, 0, 1, 0, 3, 0, 5, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 8, 5, 9, 7, 2, 6, 4, 0],
    #                 [0, 0, 0, 6, 0, 1, 0, 0, 0],
    #                 [0, 2, 6, 3, 8, 5, 9, 1, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 3, 0, 5, 0, 2, 0, 0],
    #                 [8, 0, 0, 4, 9, 7, 0, 0, 6]]) == [[5, 6, 8, 7, 1, 9, 3, 2, 4],
    #                                                   [9, 7, 1, 2, 3, 4, 5, 6, 8],
    #                                                   [2, 3, 4, 5, 6, 8, 7, 9, 1],
    #                                                   [1, 8, 5, 9, 7, 2, 6, 4, 3],
    #                                                   [3, 9, 7, 6, 4, 1, 8, 5, 2],
    #                                                   [4, 2, 6, 3, 8, 5, 9, 1, 7],
    #                                                   [6, 1, 9, 8, 2, 3, 4, 7, 5],
    #                                                   [7, 4, 3, 1, 5, 6, 2, 8, 9],
    #                                                   [8, 5, 2, 4, 9, 7, 1, 3, 6]], "second"
    
    print('Local tests done!!!')