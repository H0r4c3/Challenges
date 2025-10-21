'''
Steps:

Represent the board as a system of equations using modulo-2 arithmetic (since lights toggle between 0 and 1).
Use Gaussian elimination to solve for the correct set of button presses.
Return the optimal sequence of presses that turns all lights off.
Here's the implementation:

Lights Out Solver

Answer in chat instead
How It Works
Matrix Setup: Each button press affects itself and its adjacent neighbors, forming a 25x25 binary system.
Equation Formation: The system is solved using modulo-2 Gaussian elimination.
Solution Extraction: The function returns a list of button presses that lead to all lights being off.
'''

import numpy as np

def index(x, y):
    return x * 5 + y

def gaussian_elimination_mod2(A, b):
    A = np.array(A, dtype=int) % 2
    b = np.array(b, dtype=int) % 2
    rows, cols = A.shape
    
    for col in range(cols):
        pivot_row = None
        for row in range(col, rows):
            if A[row, col] == 1:
                pivot_row = row
                break
        
        if pivot_row is None:
            continue
        
        A[[col, pivot_row]] = A[[pivot_row, col]]
        b[[col, pivot_row]] = b[[pivot_row, col]]
        
        for row in range(rows):
            if row != col and A[row, col] == 1:
                A[row] ^= A[col]
                b[row] ^= b[col]
    
    return b.tolist()

def wall_keeper(on_panels):
    A = np.zeros((25, 25), dtype=int)
    b = np.zeros(25, dtype=int)
    
    for x in range(5):
        for y in range(5):
            idx = index(x, y)
            A[idx, idx] = 1
            if x > 0:
                A[idx, index(x - 1, y)] = 1
            if x < 4:
                A[idx, index(x + 1, y)] = 1
            if y > 0:
                A[idx, index(x, y - 1)] = 1
            if y < 4:
                A[idx, index(x, y + 1)] = 1
    
    if on_panels and isinstance(on_panels[0], int):
        on_panels = [( (n - 1) // 5, (n - 1) % 5 ) for n in on_panels]
    
    for x, y in on_panels:
        b[index(x, y)] = 1
    
    solution = gaussian_elimination_mod2(A, b)
    result = [i + 1 for i in range(25) if solution[i] == 1]  # Convert (row, col) to 1-based index
    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import chain


    def checker(solution, on_panels):
        answer = solution(on_panels)
        wk_p = list((0, 1)[n in on_panels] for n in range(1, 26))
        p = list(wk_p[n: n+5] for n in range(0, 25, 5))
        for a in answer:
            r, c = (a-1) // 5, (a-1) % 5
            p[r][c] = 1 - p[r][c]
            if r+1 < 5:
                p[r+1][c] = 1 - p[r+1][c]
            if r-1 > -1:
                p[r-1][c] = 1 - p[r-1][c]
            if c+1 < len(p[0]):
                p[r][c+1] = 1 - p[r][c+1]
            if c-1 > -1:
                p[r][c-1] = 1 - p[r][c-1]
        return sum(chain(*p)) == 0

    assert checker(wall_keeper, [5, 7, 13, 14, 18]), 'basic'
    assert checker(wall_keeper, list(range(1, 26))), 'all_lights'
