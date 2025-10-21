'https://py.checkio.org/en/mission/colorful-disks/'

'''
Colorful Disks is a game played on a base with vertical stick and some paper disks with a hole in the center. 
The disks all have different radiuses and colors. When all the disks are stacked on top of each other, 
the number of colors that can be seen from above is the score in this game. So, disks that cannot be seen from above are not scored.
Given the radiuses of the disks in order of placing on the stick (from the bottom one to the top one), calculate the score when all the disks are stacked.
'''

def count_discs_(discs: tuple[int, ...], colors) -> int:    
        
    if len(discs)==0: 
        return colors + 1
    else:
        max_disc = max(discs)
        print(max_disc)

        pos_max = discs.index(max_disc)
        print(pos_max)

        rest_discs = discs[pos_max + 1 : ]
        print(rest_discs)
        
        colors += 1
        print(f'colors = {colors}')
        
        return count_discs(rest_discs)
    

def count_discs(discs: tuple[int, ...]) -> int:
    colors = 0
    
    #if len(discs)==1: 
    #    return 1
    
    while len(discs)>0:
        max_disc = max(discs)
        print(max_disc)

        pos_max = discs.index(max_disc)
        print(pos_max)

        discs = discs[pos_max + 1 : ]
        print(discs)
        
        colors += 1
        print(f'colors = {colors}')
        
    return colors

print("Example:")
#print(count_discs((3, 2)))

# These "asserts" are used for self-checking
assert count_discs((3, 6, 7, 4, 5, 1, 2)) == 3
assert count_discs((6, 5, 4, 3, 2, 1)) == 6
assert count_discs((5,)) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")