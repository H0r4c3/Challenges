'https://py.checkio.org/en/mission/x-o-referee/'

'''
You will be the referee for this games results. 

You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. 

Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.
'''

import pandas as pd
from typing import List


def checkio(game_result: List[str]) -> str:
    game_result_lists = map(list, game_result)
    df = pd.DataFrame(game_result_lists, index=['r1', 'r2', 'r3'] , columns=['c1', 'c2', 'c3'])
    print(df)
    
    # column
    #print(set(df['b']))
    
    # row
    #print(set(df.loc[2]))
    
    # element
    #print(df.at[1, 'a'])
    
    #print(df.nunique(axis='index')) 
    #print(df.nunique(axis='columns')) 
    
    col = dict(df.nunique(axis='index'))
    row = dict(df.nunique(axis='columns'))
    
    print(col)
    print(row)
    
    # check the columns:
    for key, value in col.items():
        if value == 1:
            return df.at['r1', key]

    # check the rows:  
    for key, value in row.items():
        if value == 1:
            return df.at['r1', key]
        else:
            return 'D'
        
    # check the diagonals:
    
                     
    
    



if __name__ == "__main__":
    print("Example:")
    print(checkio(["X.O", "XX.", "XOO"]))
    #print(checkio(["OOX", "XXO", "OXX"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"