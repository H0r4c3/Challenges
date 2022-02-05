'https://py.checkio.org/en/mission/chess-knight/'

'''
Your task is to write a function that can find all of the chessboard cells to which the Knight can move. 
The input data will consist of a start cell and the amount of moves that the Knight will make. 
There is only one figure on the board - your Knight.
If the same cell appears more than once - do not add it again. 
You should return the list of all of the possible cells and sort them as follows: 
in alphabetical order (from 'a' to 'h') and in ascending order (from 'a1' to 'a8' and so on).

Input: A start cell, the number of moves.

Output: A list of all of the possible cells.
'''

result = list()
    
from itertools import product

# Solution using recursion (for n moves)
def chess_knight(start, moves):
    conversion1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    conversion2 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
    global result
    
    print(start)
    
    x, y = [int(conversion1.get(start[0])), int(start[1])]
    
    moves_all = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2, x+2], [y-1, y+1]))
    moves_ok = [(conversion2.get(x), str(y)) for x, y in moves_all if x > 0 and y > 0 and x < 9 and y < 9]
    result1 = [''.join(item) for item in moves_ok]
    
    result.extend(result1)
    result = sorted((list(set(result))))
    print(result)
    
    moves -=1
    if moves == 0:
        result_all = list(result)
        result.clear()
        return result_all
    
    for item in result1:
        print(item)
        result = chess_knight(item, moves)
        
    return result
        

# Solution for only 2 moves       
def chess_knight_(start, moves):
    conversion1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    conversion2 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
    result = list()
    result1 = list()
    
    print(start)
    
    def moves_8(start):
        x, y = [int(conversion1.get(start[0])), int(start[1])]
        moves_all = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2, x+2], [y-1, y+1]))
        moves_ok = [(conversion2.get(x), str(y)) for x, y in moves_all if x > 0 and y > 0 and x < 9 and y < 9]
        result1 = [''.join(item) for item in moves_ok]
        return result1
    
    if moves == 1:
        result1 = moves_8(start)
        result.extend(result1)
        result = sorted((list(set(result))))
        print(result)
        return result
    
    if moves == 2:
        result1 = moves_8(start)
        result.extend(result1)
        result1 = sorted((list(set(result))))
        #print(result)
        
        for item in result1:
            print(item)
            result2 = moves_8(item)
            result.extend(result2)
            result = sorted((list(set(result))))
            print(result)
            
    return result
        
    

if __name__ == '__main__':
    print("Example:")
    #print(chess_knight('a1', 1))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")