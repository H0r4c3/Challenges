'https://py.checkio.org/en/mission/place-queens/'

'''
You should place eight chess Queens on an 8x8 chessboard so that no two Queens threaten each other. 
For this challenge, we have already placed one or more Queens on the board, so you will need to finish the placement.

1 
2
3
4
5
6
7
8
 a b c d e f g h
'''

from itertools import product, combinations

COLS, ROWS = 'abcdefgh', '12345678'
DIAGS = []
WHOLE_BOARD = list(map(''.join, product(COLS, ROWS)))
D1 =[['a1'], ['a2', 'b1'], ['a3', 'b2', 'c1'], ['a4', 'b3', 'c2', 'd1'], ['a5', 'b4', 'c3', 'd2', 'e1'], ['a6', 'b5', 'c4', 'd3', 'e2', 'f1'], 
     ['a7', 'b6', 'c5', 'd4', 'e3', 'f2', 'g1'], ['a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'], ['h2', 'g3', 'f4', 'e5', 'd6', 'c7', 'b8'], 
     ['h3', 'g4', 'f5', 'e6', 'd7', 'c8'], ['h4', 'g5', 'f6', 'e7', 'd8'], ['h5', 'g6', 'f7', 'e8'], ['h6', 'g7', 'f8'], ['h7', 'g8'], ['h8']]

D2 = [['a8'], ['a7', 'b8'], ['a6', 'b7', 'c8'], ['a5', 'b6', 'c7', 'd8'], ['a4', 'b5', 'c6', 'd7', 'e8'], ['a3', 'b4', 'c5', 'd6', 'e7', 'f8'], 
      ['a2', 'b3', 'c4', 'd5', 'e6', 'f7', 'g8'], ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'], ['h7', 'g6', 'f5', 'e4', 'd3', 'c2', 'b1'], 
      ['h6', 'g5', 'f4', 'e3', 'd2', 'c1'], ['h5', 'g4', 'f3', 'e2', 'd1'], ['h4', 'g3', 'f2', 'e1'], ['h3', 'g2', 'f1'], ['h2', 'g1'], ['h1']]


def col_row_diagonals_to_eliminate(coord):
    col = coord[0]
    row = coord[1]
    
    diag1 = [item for item in D1 if coord in item]
    diag2 = [item for item in D2 if coord in item]
    
    elements_from_diags = {item for sublist in diag1 for item in sublist} | {item for sublist in diag2 for item in sublist}
    
    return col, row, elements_from_diags


def eliminate_columns_and_rows(cols, rows):
    cols_all, rows_all = list(COLS), list(ROWS)
    
    cols_ok = [item for item in cols_all if item not in cols]
    rows_ok = [item for item in rows_all if item not in rows]
    
    return cols_ok, rows_ok


def eliminate_diagonals(placed):
    cols, rows, all_elements_from_diags = list(), list(), set()
    
    for coord in placed:
        col, row, elements_from_diags = col_row_diagonals_to_eliminate(coord)
        #print(col, row, elements_from_diags)
        cols.append(col)
        rows.append(row)
        all_elements_from_diags = all_elements_from_diags.union(elements_from_diags)
    
    cols_ok, rows_ok = eliminate_columns_and_rows(cols, rows)
    #print(f'Remaining cols and rows: cols_list = {cols_ok}, rows_list = {rows_ok}')
    
    # after eliminating the columns and the rows
    remaining_board = list(map(''.join, product(cols_ok, rows_ok)))
    #print(f'Remaining board after eliminating cols and rows = {remaining_board}')
    
    # eliminating the elements in diagonals
    #print(f'All elements from diags for eliminating = {sorted(all_elements_from_diags)}')
    remaining_board = [item for item in remaining_board if item not in all_elements_from_diags]
    #print(f'Remaining board after eliminating diagonals = {remaining_board}')
    
    return remaining_board
    

def calculate_all_combinations(placed, remaining_board):
    print(f'placed = {placed}')
    placed_queens = len(placed)
    print(f'placed_queens = {placed_queens}')
    q = 8 - placed_queens # how many more queens must be placed
    print(f'q = {q}')
    
    # calculate combinations of remaining queens from remaining_board
    # if len(remaining_board) > q:
    #     remaining_board_combinations = list(combinations(remaining_board, 4))
    #     return remaining_board_combinations
    # elif len(remaining_board) == q:
    #     remaining_board_combinations = placed | remaining_board
    #     return remaining_board_combinations
    # else:
    #     print('No remaining_board_combinations')
    #     return []
    
    remaining_board_combinations = list(combinations(remaining_board, q))
    return remaining_board_combinations

def verify_all_8_queens(new_placed):
    elements_for_all_queens = list()

    for coord in new_placed:
        col, row, elements_from_diags = col_row_diagonals_to_eliminate(coord)
        print(f'row = {row}, col = {col}')
        print(f'elements_from_diags = {elements_from_diags}')
        elements_from_row = {item for item in WHOLE_BOARD if item[1] == row}
        print(f'elements_from_row = {elements_from_row}')
        elements_from_col = {item for item in WHOLE_BOARD if item[0] == col}
        print(f'elements_from_col = {elements_from_col}')
        all_elements = elements_from_row | elements_from_col | elements_from_diags
        all_elements.discard(coord)
        elements_for_all_queens.append(tuple(sorted(all_elements)))
        
    for coord in new_placed:
        for queen in elements_for_all_queens:
            if coord in queen:
                verification = False
                return elements_for_all_queens, verification
    
    verification = True                 
    return elements_for_all_queens, verification
    
        
    
def place_queens(placed):
    print(f'placed = {placed}')
    
    #new_placed = {"b2", "c4", "d6", "e8", "a5", "f3", "g1", "h7"}
    new_placed = {"b2", 'c4'}
    elements_for_all_queens, verification = verify_all_8_queens(new_placed)
    print(elements_for_all_queens)
    print(verification)
    
    
    return {}


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import combinations
    COLS = "abcdefgh"
    ROWS = "12345678"

    THREATS = {c + r: set(
        [c + ROWS[k] for k in range(8)] +
        [COLS[k] + r for k in range(8)] +
        [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8] +
        [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
               for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}

    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example" # "a5", "f3", "g1", "h7"
    assert checker(place_queens, {"b2", "c4", "d6", "e8", "a7", "g5"}, False), "2nd Example"
