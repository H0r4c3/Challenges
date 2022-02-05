'https://py.checkio.org/en/mission/square-board/'

'''
You are designing a board game in which tokens move around the square board with. (like in Monopoly (Wikipedia) )
You need to write the function that returns the coordinates after the token has moved. The coordinates of a token are being represented by a tuple consisting of a row and column. The coordinates of a top-left one - (0, 0).

You are given three arguments:
the first one is the length of the game board’s side (an integer);
the second is the token’s current position (an integer);
Cells around the board are numbered clockwise starting with 0 on the bottom right corner.

the third is the number of steps to advance (an integer);
A positive number represents a clockwise direction. A negative number represents a counterclockwise direction.
Input: 3 arguments: the length of the game board’s side (an integer), token’s current position (an integer), and the number of steps to advance (an integer).

Output: The coordinates after the token has moved (a tuple consisting of a row and column).
'''

from typing import Tuple
Coordinate = Tuple[int, int]

def square_board(side: int, token: int, steps: int) -> Coordinate:
    s = side - 1
    
    end_pos = (token + steps) % (4 * s)
    print(f'end_pos = {end_pos}')
    
    
    # c[0] = (s, s-0)
    # c[1] = (s, s-1)
    # c[2] = (s, s-2)
    # #..............
    # c[s] = (s, s-s)
    
    #d1 = {s-i : (s, s-(s-i)) for i in range(s, -1, -1)}
    d1 = {i : (s, (s-i)) for i in range(s+1)}
    #print(d1)
    
    # c[s+1] = (s-1, 0)
    # c[s+2] = (s-2, 0)
    # #..............
    # c[s+s] = (s-s, 0)
    
    d2 = {s+i : (s-i, 0) for i in range(s+1)}
    #print(d2)
    
    # c[2*s+1] = (0, s-2)
    # c[2*s+2] = (0, s-1)
    # #..............
    # c[3*s] = (0, s-0)
    
    d3 = {2*s+i : (0, i) for i in range(0, s+1)}
    #print(d3)
    
    
    # c[3*s+1] = (s-2, s)
    # c[3*s+2] = (s-1, s)
    # #..............
    # c[3*s+s] = (s-0, s)
    
    d4 = {3*s+i : (i, s) for i in range(s)}
    #print(d4)
    
    #d = d1 | d2 | d3 | d4
    d = {**d1, **d2, **d3, **d4}
    print(f'd = {d}')
    
    print(d.get(end_pos))
    return d.get(end_pos)


# Shorter version of my solution
def square_board_(side: int, token: int, steps: int) -> Coordinate:
    s = side - 1
    
    end_pos = (token + steps) % (4 * s)
    print(f'end_pos = {end_pos}')
    
    d1 = {i : (s, (s-i)) for i in range(s+1)}
    d2 = {s+i : (s-i, 0) for i in range(s+1)}
    d3 = {2*s+i : (0, i) for i in range(0, s+1)}
    d4 = {3*s+i : (i, s) for i in range(s)}
    
    #d = d1 | d2 | d3 | d4
    d = {**d1, **d2, **d3, **d4}
    print(f'd = {d}')
    
    print(d.get(end_pos))
    return d.get(end_pos)




# https://py.checkio.org/mission/square-board/publications/tom-tom/python-3/first/share/bb881ffe7c0c3280e08c41d73d925106/
from typing import Tuple
Coordinate = Tuple[int, int]


def square_board_(side: int, token: int, steps: int) -> Coordinate:
    s = side - 1
    p = (token + steps) % (4 * s)
    return ((s, s - p), (2 * s - p, 0), (0, p - 2 * s), (p - 3 * s, s))[p // s]



if __name__ == '__main__':
    print("Example:")
    #print(square_board(4, 1, 4))
    #assert square_board(4, 1, 4) == (1, 0)
    #assert square_board(6, 2, -3) == (4, 5)
    #assert square_board(7, 20, 21) == (0, 5)
    assert square_board(3, 5, -4) == (2, 1)

    print("Coding complete? Click 'Check' to earn cool rewards!")