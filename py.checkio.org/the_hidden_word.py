'https://py.checkio.org/en/mission/hidden-word/'

'''
You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n). 
Casing does not matter for your search, but whitespaces should be removed before your search. 
You should find the word inside the rhyme in the horizontal (from left to right) or vertical (from up to down) lines. 
For this, you need envision the rhyme as a matrix (2D array). Find the coordinates of the word in the cut rhyme (without whitespaces).

The result must be represented as a list -- [row_start,column_start,row_end,column_end] , where

row_start is the line number for the first letter of the word.
column_start is the column number for the first letter of the word.
row_end is the line number for the last letter of the word.
column_end is the column number for the last letter of the word.

Counting of the rows and columns start from 1.
'''

# import numpy as np
# def checkio(text:str, word:str):
#     text_new = text.lower().replace(' ', '').splitlines()
#     print(text_new)
    
#     row_lists = [list(item) for item in text_new]
#     length_max = max(map(len, row_lists))
    
#     # make the row lists equal in length
#     rows = [item + [None]*(length_max - len(item)) for item in row_lists]
#     rows_arr = np.array(rows)
    
#     return [1, 1, 1, 4]


def checkio(text:str, word:str):
    
    text_rows = text.lower().replace(' ', '').splitlines()
    print(text_rows)
    
    max_len = len(max(text_rows, key=len))
    
    text_rows = [item + ' '*(max_len - len(item)) for item in text_rows]
    print(text_rows)
    
    text_columns = [None] * max_len
    
    for i in range(max_len):
        text_columns[i] = ''.join([item[i] for item in text_rows])
 
    print(text_columns)
    
    for item in text_rows:
        if word in item:
            column_start = item.find(word) + 1
            column_end = column_start + len(word) - 1
            row_start = text_rows.index(item) + 1
            row_end = row_start
            
            print([row_start, column_start, row_end, column_end])
            return [row_start, column_start, row_end, column_end]
            
    for item in text_columns:
        print(item)
        if word in item:
            row_start = item.find(word) + 1
            row_end = row_start + len(word) - 1
            column_start = text_columns.index(item) + 1
            column_end = column_start
            
            print([row_start, column_start, row_end, column_end])
            return [row_start, column_start, row_end, column_end]
            


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
    
print("Coding complete? Click 'Check' to earn cool rewards!")