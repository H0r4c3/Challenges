'https://py.checkio.org/en/mission/identify-block/'

'''
This mission uses a 4x4 grid. Each square is numbered from 1 to 16 in row-major order.
You are given 4 numbers (a set of integers). These numbers represent the positions of each square on the grid and a whole block if all the squares are adjacent.

You have to identify the kind of block. (Refer to the following image or comment of initial code for the kind of block).
The answer is an upper-case alphabet letter ('I', 'J', 'L', 'O', 'S', 'T' or 'Z'). If it’s not a block, then return None.

The block is placed anywhere on the grid and can be rotated (0, 90, 180 or 270 degrees).
'''

def identify_block(numbers):
    """
    grid(4x4):
    +--+--+--+--+
    |1 |2 |3 |4 |
    +--+--+--+--+
    |5 |6 |7 |8 |
    +--+--+--+--+
    |9 |10|11|12|
    +--+--+--+--+
    |13|14|15|16|
    +--+--+--+--+


    blocks(7 kinds):

    'I'  'J'  'L'  'O'  'S'  'T'  'Z'

     *    *   *    **    **  ***  **
     *    *   *    **   **    *    **
     *   **   **
     *

    """
    return None


# Best Solution:
# https://py.checkio.org/mission/identify-block/publications/martin_b/python-3/straightforward/share/ebb4791689d2d309be519ffaad42d1db/

def identify_block(numbers):
    # define the lettes
    letters = {
        (0, 4, 8, 12): 'I',
        (1, 5, 8, 9): 'J',
        (0, 4, 8, 9): 'L',
        (0, 1, 4, 5): 'O',
        (1, 2, 4, 5): 'S',
        (0, 1, 2, 5): 'T',
        (0, 1, 5, 6): 'Z'
    }

    # normalize - move the letter to the top left corner
    def normalize(b):
        m = (min(b) // 4) * 4 + min(x % 4 for x in b)
        return tuple(x - m for x in sorted(b))

    # normalize the input
    numbers = normalize([x - 1 for x in numbers])
    for block, letter in letters.items():
        # get grid from the letter numbers
        grid = [1 if i in block else 0 for i in range(16)]
        grid = tuple(tuple(grid[i:i + 4]) for i in range(0, 16, 4))
        # compare the input to the 4 rotations of the letter
        for i in range(4):
            # compare the grid to the normalized numbers
            g = sum(grid, ())
            if numbers == normalize([i for i in range(16) if g[i]]):
                return letter
            # rotate grid
            grid = tuple([r for r in zip(*grid)][::-1])



# Another Solution:
# https://chowdera.com/2022/01/202201102108211126.html

import numpy as np
def identify_block_(numbers):
    """
    grid(4x4):
    +--+--+--+--+
    |1 |2 |3 |4 |
    +--+--+--+--+
    |5 |6 |7 |8 |
    +--+--+--+--+
    |9 |10|11|12|
    +--+--+--+--+
    |13|14|15|16|
    +--+--+--+--+


    blocks(7 kinds):

    'I'  'J'  'L'  'O'  'S'  'T'  'Z'

     *    *   *    **    **  ***  **
     *    *   *    **   **    *    **
     *   **   **
     *
    """
    numbers = list(numbers)
    numbers.sort()

    data = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

    blocks ={
        'I':[(1,1,1),(4,4,4)],
        'J':[(4,3,1),(4,1,1),(1,3,4),(1,1,4)],
        'L':[(4,4,1),(2,1,1),(1,4,4),(1,1,2)],
        'O':[(1,3,1)],
        'S':[(1,2,1),(4,1,4)],
        'T':[(3,1,1),(1,1,3),(4,1,3),(3,1,4)],'Z':[(1,4,1),(3,1,3)]}

    HLS = [tuple(np.argwhere(data == i)[0])for i in numbers]
    HLS = sorted(HLS,key=lambda x:(x[0], x[1]))
    
    HLS_C = sum([1 for i in range(len(HLS)-1) if HLS[i+1][1]-HLS[i][1]>1 or HLS[i+1][0]-HLS[i][0]>1])

    numbers_C = tuple([numbers[i+1]-numbers[i] for i in range(len(numbers)-1)])
    print(HLS_C,numbers_C)
    result = None
    if HLS_C > 0:
        result = None
    if HLS_C == 0:
        for k,v in blocks.items():
            if numbers_C in v:
                result = k

    print(result)
    return result


# Another Best Solution:
# https://py.checkio.org/mission/identify-block/publications/vit.aborigen/python-3/dictionary-with-rotated-figures/?ordering=most_voted&filtering=all

FIGURES = {
    "I": ({1,2,3,4}, {1,5,9,13}),
    "J": ({2,6,9,10}, {1,5,6,7}, {1,2,5,9}, {1,2,3,7}),
    "L": ({1,5,9,10}, {1,2,3,5}, {1,2,6,10}, {3,5,6,7}),
    "O": ({1,2,5,6},),
    "S": ({2,3,5,6}, {1,5,6,10}),
    "T": ({1,2,3,6}, {2,5,6,10}, {2,5,6,7}, {1,5,6,9}),
    "Z": ({1,2,6,7}, {2,5,6,9}),
}

def move_figure_to_top_left(numbers):
    while not any(number in numbers for number in {1, 2, 3, 4}):
        numbers = {(num - 4) for num in numbers}
    while not any(number in numbers for number in {1, 5, 9, 13}):
        numbers = {(num - 1) for num in numbers}
    return numbers

def identify_block(numbers):
    numbers = move_figure_to_top_left(numbers)
    for figure, form in FIGURES.items():
        if numbers in form:
            return figure
    return


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) == None, 'None'
    print('"Run" is good. How is "Check"?')