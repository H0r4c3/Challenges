'https://py.checkio.org/en/mission/the-square-chest/'

'''
On the chest keypad is a grid of numbered dots. 
The grid is comprised of a square shaped array of dots and contains lines that connect some pairs of adjacent dots. 
The answer to the code is the number of squares that are formed by these lines.
'''

from typing import List

def contains(list1, list2):
    check =  all(item in list1 for item in list2)
    return check

def checkio(lines_list: List[List[int]]) -> int:
    """Return the quantity of squares"""
    result = 0
    all_squares = [None] * 15
    lines_list = [sorted(item) for item in lines_list]
    print(lines_list)
    
    # small squares
    all_squares[0] = ([1,2], [2,6], [5,6], [1,5]) # start
    all_squares[1] = ([2,3], [3,7], [6,7], [2,6]) # +1
    all_squares[2] = ([3,4], [4,8], [7,8], [3,7]) # +2
    
    all_squares[3] = ([5,6], [6,10], [9,10], [5,9]) # +4
    all_squares[4] = ([6,7], [7,11], [10,11], [6,10]) # +5
    all_squares[5] = ([7,8], [8,12], [11,12], [7,11]) # +6
    
    all_squares[6] = ([9,10], [10,14], [13,14], [9,13]) # +8
    all_squares[7] = ([10,11], [11,15], [14,15], [10,14]) # +9
    all_squares[8] = ([11,12], [12,16], [15,16], [11,15]) # +10
    
    # medium squares
    all_squares[9] = ([1,2], [2,3], [3,7], [7,11], [10,11], [9,10], [5,9], [1,5]) # medium square start
    all_squares[10] = ([2,3], [3,4], [4,8], [8,12], [11,12], [10,11], [6,10], [2,6]) # +1
    all_squares[11] = ([5,6], [6,7], [7,11], [11,15], [14,15], [13,14], [9,13], [5,9]) # +4
    all_squares[12] = ([6,7], [7,8], [8,12], [12,16], [15,16], [14,15], [10,14], [6,10]) # +5
    
    # biggest square
    all_squares[13] = ([1,2], [2,3], [3,4], [4,8], [8,12], [12,16], [15,16], [14,15], [13,14], [9,13], [5,9], [1,5]) # exterior square
    
    for i in range(14):
        if contains(lines_list, all_squares[i]):
            print(f'all_squares[{i}] = {all_squares[i]}')
            result += 1
    
    print(f'result = {result}')
    return result



# Best Solution: 
# https://py.checkio.org/mission/the-square-chest/publications/evrur97/python-3/on-the-square/share/260bd0479fc895f6c72028bb060edb43/
# Define maps for every type of square

from typing import List

SMALL_SQUARE = [[0,1],[1,5],[4,5],[0,4]]
MEDIUM_SQUARE = [[0,1], [1,2], [2,6], [6,10], [9,10], [8,9], [4,8], [0,4]]
LARGE_SQUARE = [[0,1], [1,2], [2,3], [3,7], [7,11], [11,15], [14,15], [13,14], [12,13], [8,12], [4,8], [0,4]]

# Identify where each type of square can originate
A = [1]
B = [1, 2, 5, 6]
C = [1, 2, 3, 5, 6, 7, 9, 10, 11]

def make_squares(origins, shape):
    """
    Given an origin and a map, create the set of lines that represent the given shape
    """
    test_square_collection = []
    for  x in origins:
        test_square = []
        for s in shape:
            test_square.append([x + s[0], x + s[1]])
        test_square_collection.append(test_square)
    return test_square_collection

    
def checkio_(lines_list: List[List[int]]) -> int:
    
    # Clean up any lines that are not specified as low number, high number
    sorted_lines_list = []
    for line in lines_list:
        sorted_lines_list.append(sorted(line))
    
    count = 0
    
    # Build a collection of all possible squares
    test_square_collection = make_squares(A,LARGE_SQUARE)
    test_square_collection += make_squares(B,MEDIUM_SQUARE)
    test_square_collection += make_squares(C,SMALL_SQUARE)
    
    for test_square in test_square_collection:
        found = True
        for edge in test_square:
            if edge not in sorted_lines_list:
                found = False
                break
        if found:
            count += 1

    return count





if __name__ == '__main__':
    print("Example:")
    # print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
    #                [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
    #                [10, 14], [12, 16], [14, 15], [15, 16]]))

    # assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
    #                  [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
    #                  [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    # assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
    #                  [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
    #                  [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    # assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    # assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    # assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
    #                  [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    
    assert checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],[14,13],[13,9],[15,14]]) == 3
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
