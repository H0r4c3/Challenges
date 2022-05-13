'https://py.checkio.org/en/mission/the-stone-wall/'

'''
As input you'll get a multiline string consists of '0' and '#' - a view of a stone wall from above. 
The '#' will show the stone part of the wall and the '0' will show the empty part. The relative location of you and the wall is as follows: 
you look at the array from the bottom of it.
Your task is to find the index of the place where the wall is the narrowest (as shown at the picture below). 
The width of the wall is the height of the columns of the array (multiline string). 
If there are several such places, return the index of leftmost. Index starts from 0.
'''

import re

def stone_wall_(wall):
    if '0' not in wall: return 0
    
    wall = wall.splitlines()[1:]
    print(wall)
    
    # columns where '0' is found
    cols = list() 
    
    for item in wall:
        f = re.finditer('0', item)
        for match in f:
            m = match.span()
            cols.append(m[0])
    
    cols.sort()
    
    # create a dictionary having keys = columns and values = repetitions
    repetitions = {i:cols.count(i) for i in cols}
    print(repetitions)
    
    # sort the dictionary after the value
    repetitions = {key:value for key, value in sorted(repetitions.items(), key=lambda item: item[1], reverse=True)}
    print(repetitions)
       
    repetitions_list = list(repetitions.keys())
    
    print(repetitions_list[0])
    return repetitions_list[0]


# Best Solution:
# https://py.checkio.org/mission/the-stone-wall/publications/fed.kz/python-3/zip-min-index/?ordering=most_voted&filtering=all

def stone_wall(wall):
    print(f'START wall = {wall}')
    
    wall = list(zip(*wall.split()))
    print(wall)
    
    print(min(wall, key=lambda x: x.count('#')))
    
    return wall.index(min(wall, key=lambda x: x.count('#')))




if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")