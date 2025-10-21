'https://py.checkio.org/en/mission/x-and-o/'

'''
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking spaces in a 3×3 grid. 
The player who succeeds in placing three of their respective marks in a horizontal, vertical, or diagonal row (NW-SE and NE-SW) wins the game. 
Maybe you've solve "Xs and Os Referee" already and this mission will be simpler for you.

In this mission, you will play against various bots, your goal is to never lose. You may only achieve wins or draws. 
For each game your function is called several times (in the same environment) for each move until the game is over.

For each step your function receives a grid state as a sequence of strings, where "X" is a X-mark, "O" is an O-mark and "." is an empty cell. 
The second argument is for your mark, either "X" or "O". For each move your function should return the coordinates of the your next mark as a 
sequence of two numbers - row and column. Rows and columns are numbered starting from zero.

Input: Two arguments. A grid state as a tuple of strings (unicode) and your mark as a string "X" or "O".

Output: The coordinates of your move as a list or a tuple of two integers from 0 to 2.
'''

import pandas as pd
import numpy as np

def x_and_o_(grid, your_mark):
    #grid, your_mark = ("XXO", ".X.", "XOO"), "O"
    print(grid), print(your_mark)
    
    grid_list = [list(row) for row in grid]
    df = pd.DataFrame(grid_list, index=['r1', 'r2', 'r3'] , columns=['c1', 'c2', 'c3'])
    print(df, '\n')
    
    return (1, 1)

def x_and_o(grid, mark):
    """
    Determine the best move for the given grid state in Tic-Tac-Toe.
    
    Args:
        grid: A tuple of 3 strings, each representing a row in the Tic-Tac-Toe grid.
              'X' represents X-mark, 'O' represents O-mark, and '.' represents an empty cell.
        mark: A string, either 'X' or 'O', representing your mark.
    
    Returns:
        A tuple of two integers representing the row and column for the next move.
    """
    # Convert grid to a 2D list for easier manipulation
    board = [list(row) for row in grid]
    
    # Determine opponent's mark
    opponent = 'O' if mark == 'X' else 'X'
    
    # Check if we can win in the next move
    winning_move = find_winning_move(board, mark)
    if winning_move:
        return winning_move
    
    # Check if we need to block opponent's winning move
    blocking_move = find_winning_move(board, opponent)
    if blocking_move:
        return blocking_move
    
    # Apply strategy: Try to fork (create two winning ways)
    forking_move = find_forking_move(board, mark)
    if forking_move:
        return forking_move
    
    # Block opponent's forking attempt
    blocking_fork = block_opponent_fork(board, mark, opponent)
    if blocking_fork:
        return blocking_fork
    
    # Take center if available
    if board[1][1] == '.':
        return (1, 1)
    
    # Take opposite corner if opponent has a corner
    opposite_corner = take_opposite_corner(board, opponent)
    if opposite_corner:
        return opposite_corner
    
    # Take any available corner
    corner = take_any_corner(board)
    if corner:
        return corner
    
    # Take any available side
    side = take_any_side(board)
    if side:
        return side
    
    # Should never reach here in a valid Tic-Tac-Toe game
    # Find any empty cell as a fallback
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                return (i, j)
    
    # No valid moves (should not happen in a normal game)
    return (0, 0)

def find_winning_move(board, player):
    """Find a move that would result in a win for the given player."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                # Try this move
                board[i][j] = player
                if is_winner(board, player):
                    # Undo move and return this winning position
                    board[i][j] = '.'
                    return (i, j)
                # Undo move
                board[i][j] = '.'
    return None

def is_winner(board, player):
    """Check if the given player has won on the board."""
    # Check rows
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    
    # Check columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def count_player_in_line(board, line_cells, player):
    """Count how many cells in a line are occupied by the player."""
    count = 0
    for i, j in line_cells:
        if board[i][j] == player:
            count += 1
    return count

def count_empty_in_line(board, line_cells):
    """Count how many cells in a line are empty."""
    count = 0
    for i, j in line_cells:
        if board[i][j] == '.':
            count += 1
    return count

def get_empty_in_line(board, line_cells):
    """Get coordinates of empty cells in a line."""
    empty_cells = []
    for i, j in line_cells:
        if board[i][j] == '.':
            empty_cells.append((i, j))
    return empty_cells

def find_forking_move(board, player):
    """Find a move that creates a fork (two potential winning ways)."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                # Try this move
                board[i][j] = player
                
                # Count potential winning lines
                winning_lines = 0
                
                # Check rows, columns, and diagonals
                lines = [
                    [(i, 0), (i, 1), (i, 2)],  # Row
                    [(0, j), (1, j), (2, j)],  # Column
                ]
                
                # Add diagonals if the cell is on a diagonal
                if (i == j):
                    lines.append([(0, 0), (1, 1), (2, 2)])  # Main diagonal
                if (i + j == 2):
                    lines.append([(0, 2), (1, 1), (2, 0)])  # Other diagonal
                
                for line in lines:
                    # A potential winning line has the player's mark and two empty spaces
                    player_count = sum(1 for x, y in line if board[x][y] == player)
                    empty_count = sum(1 for x, y in line if board[x][y] == '.')
                    
                    if player_count == 1 and empty_count == 2:
                        winning_lines += 1
                
                # Undo move
                board[i][j] = '.'
                
                # If this creates two or more winning ways, it's a fork
                if winning_lines >= 2:
                    return (i, j)
    
    return None

def block_opponent_fork(board, mark, opponent):
    """Block opponent's forking move."""
    opponent_forks = []
    
    # Find all potential opponent forking moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                # Try opponent's move here
                board[i][j] = opponent
                
                # Count potential winning lines
                winning_lines = 0
                
                # Check rows, columns, and diagonals
                lines = [
                    [(i, 0), (i, 1), (i, 2)],  # Row
                    [(0, j), (1, j), (2, j)],  # Column
                ]
                
                # Add diagonals if the cell is on a diagonal
                if (i == j):
                    lines.append([(0, 0), (1, 1), (2, 2)])  # Main diagonal
                if (i + j == 2):
                    lines.append([(0, 2), (1, 1), (2, 0)])  # Other diagonal
                
                for line in lines:
                    # A potential winning line has the opponent's mark and two empty spaces
                    opponent_count = sum(1 for x, y in line if board[x][y] == opponent)
                    empty_count = sum(1 for x, y in line if board[x][y] == '.')
                    
                    if opponent_count == 1 and empty_count == 2:
                        winning_lines += 1
                
                # Undo move
                board[i][j] = '.'
                
                # If this creates two or more winning ways, it's a fork
                if winning_lines >= 2:
                    opponent_forks.append((i, j))
    
    if len(opponent_forks) == 0:
        return None
    
    if len(opponent_forks) == 1:
        return opponent_forks[0]
    
    # If there are multiple forking opportunities, create a forcing move
    # by making a move that will force the opponent to defend
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                # Try our move
                board[i][j] = mark
                
                # Check if this creates a threat
                has_threat = False
                for row in range(3):
                    if all(board[row][col] == mark for col in range(3) if board[row][col] != '.'):
                        if count_empty_in_line(board, [(row, col) for col in range(3)]) == 1:
                            has_threat = True
                
                for col in range(3):
                    if all(board[row][col] == mark for row in range(3) if board[row][col] != '.'):
                        if count_empty_in_line(board, [(row, col) for row in range(3)]) == 1:
                            has_threat = True
                
                # Check diagonals
                diag1 = [(0, 0), (1, 1), (2, 2)]
                diag2 = [(0, 2), (1, 1), (2, 0)]
                
                if all(board[i][i] == mark for i in range(3) if board[i][i] != '.'):
                    if count_empty_in_line(board, diag1) == 1:
                        has_threat = True
                
                if all(board[i][2-i] == mark for i in range(3) if board[i][2-i] != '.'):
                    if count_empty_in_line(board, diag2) == 1:
                        has_threat = True
                
                # Undo move
                board[i][j] = '.'
                
                if has_threat and (i, j) not in opponent_forks:
                    return (i, j)
    
    # If no forcing move, block one of the forks
    return opponent_forks[0]

def take_opposite_corner(board, opponent):
    """Take the opposite corner if the opponent has taken a corner."""
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    opposite_corners = {
        (0, 0): (2, 2),
        (0, 2): (2, 0),
        (2, 0): (0, 2),
        (2, 2): (0, 0)
    }
    
    for corner in corners:
        i, j = corner
        if board[i][j] == opponent:
            opp_i, opp_j = opposite_corners[corner]
            if board[opp_i][opp_j] == '.':
                return (opp_i, opp_j)
    
    return None

def take_any_corner(board):
    """Take any available corner."""
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for i, j in corners:
        if board[i][j] == '.':
            return (i, j)
    return None

def take_any_side(board):
    """Take any available side (middle of an edge)."""
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for i, j in sides:
        if board[i][j] == '.':
            return (i, j)
    return None

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    from random import choice

    def random_bot(grid, mark):
        empties = [(x, y) for x in range(3) for y in range(3) if grid[x][y] == "."]
        return choice(empties) if empties else (None, None)

    def referee(field):
        lines = (
            ["".join(row) for row in field]
            + ["".join(row) for row in zip(*field)]
            + [
                "".join(row)
                for row in zip(*[(r[i], r[2 - i]) for i, r in enumerate(field)])
            ]
        )
        if "X" * 3 in lines:
            return "X"
        elif "O" * 3 in lines:
            return "O"
        elif not "." in "".join(lines):
            return "D"
        else:
            return "."

    def check_game(user_func, user_mark, bot_mark, bot_algorithm=random_bot):
        grid = [["."] * 3 for _ in range(3)]
        if bot_mark == "X":
            x, y = bot_algorithm(grid, bot_mark)
            grid[x][y] = "X"
        while True:
            user_result = user_func(tuple("".join(row) for row in grid), user_mark)
            if (
                not isinstance(user_result, (tuple, list))
                or len(user_result) != 2
                or not all(isinstance(u, int) and 0 <= u < 3 for u in user_result)
            ):
                print("The result must be a list/tuple of two integers from 0 to 2.")
                return False

            if grid[user_result[0]][user_result[1]] != ".":
                print("You tried to mark the filled cell.")
                return False
            grid[user_result[0]][user_result[1]] = user_mark
            game_result = referee(grid)

            if game_result == "D" or game_result == user_mark:
                return True
            bot_move = bot_algorithm(grid, bot_mark)
            grid[bot_move[0]][bot_move[1]] = bot_mark
            game_result = referee(grid)
            if game_result == bot_mark:
                print("Lost :-(")
                return False
            elif game_result == "D":
                return True

    assert check_game(x_and_o, "X", "O"), "Random X"
    assert check_game(x_and_o, "O", "X"), "Random O"