'https://py.checkio.org/en/mission/hypercube/'

'''git filter-repo --invert-paths --force --path old_moved_Hella_HMF_validation/Results - Copy.xlsx
Your function receives an array of letters as an argument. 
Your task is to return True if it’s possible to read the word 'Hypercube' in this array, and False if otherwise. 
The 'Hypercube' is in the array only if the word "hypercube" can be read/compiled from an unbroken letter line. 
In addition, the line can bend at a 90-degree angle, but can’t go diagonally. It’s completely case insensitive.
'''

# My Solution:

import numpy as np

letters = ['h', 'y', 'p', 'e', 'r', 'c', 'u', 'b', 'e']

def check_letters(grid_a):
    '''Check if all the letters from hypercube are in grid'''
    global letters
    
    for letter in letters:
        if (np.where(grid_a == letter)[0]).size == 0:
            return False
    return True
        
        
def coordinates(grid_a, letter):
    '''Find the coordinates of a letter in grid_a'''
    let = np.where(grid_a == letter)
    x, y = let[0], let[1]
    coords_letter = [(x, y) for x, y in zip(let[0], let[1])]
    
    return coords_letter


def find_neighbors(matrix, element_coordinates):
    '''Find the <neighbors_coordinates> of neighbors for an element having <element_coordinates> in a <matrix>'''
    neighbors_coordinates = list()
    dimensions = matrix.shape
    
    x, y = element_coordinates[0], element_coordinates[1]
    print((x, y))
     
    c1 = (x+1, y) if x+1 <= dimensions[0] - 1 else None
    c2 = (x, y+1) if y+1 <= dimensions[1] - 1 else None
    c3 = (x-1, y) if x-1 >= 0 else None
    c4 = (x, y-1) if y-1 >= 0 else None
    #print(c1, c2, c3, c4)
    
    neighbors_coordinates = [item for item in [c1, c2, c3, c4] if item != None]
    
    print(f'{element_coordinates} has as neighbors_coordinates {neighbors_coordinates}')    
    return neighbors_coordinates


def check_if_next_letter_is_neighbor(matrix, coords1, coords2):
    '''check if at least one of neighbors of coords1 is in coords2 '''
    for item in coords1:
        neighbors_coordinates = find_neighbors(matrix, item)
        if not set(neighbors_coordinates).isdisjoint(set(coords2)):
            return True
    return False
    

def hypercube(grid):
    global letters
    
    # transform all letters from grid in lowercase
    lower_grid = [list(map(lambda x: x.lower(), item)) for item in grid]
    
    # transform the grid to an array
    grid_a = np.array(lower_grid)
    
    # check if all the letters from the word 'hypercube' are in grid
    if not check_letters(grid_a):
        return False
    
    # make a list with all the coordinates in grid for every letter in 'hypercube'
    coords = [coordinates(grid_a, letter) for letter in letters]
    print(f'coords = {coords}')
    
    # check if the next letter is neighbor
    for i in range(len(coords)-1):
        if check_if_next_letter_is_neighbor(grid_a, coords[i], coords[i+1]) == False:
            print(f'{coords[i]} has NO neighbor in {coords[i+1]}')
            return False
        else:
            print(f'{coords[i]} has neighbor in {coords[i+1]}')
    return True
    


if __name__ == '__main__':
    print("Example:")
    # print(hypercube([
    #           ['g', 'f', 'H', 'Y', 'v'],
    #           ['z', 'e', 'a', 'P', 'u'],
    #           ['s', 'B', 'T', 'e', 'y'],
    #           ['k', 'u', 'c', 'R', 't'],
    #           ['l', 'O', 'k', 'p', 'r']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert hypercube([
    #           ['g', 'f', 'H', 'Y', 'v'],
    #           ['z', 'e', 'a', 'P', 'u'],
    #           ['s', 'B', 'T', 'e', 'y'],
    #           ['k', 'u', 'c', 'R', 't'],
    #           ['l', 'O', 'k', 'p', 'r']]) == True
    # assert hypercube([
    #           ['H', 'a', 't', 's', 'E'],
    #           ['a', 'Y', 'p', 'u', 'B'],
    #           ['a', 'a', 'P', 'y', 'U'],
    #           ['x', 'x', 'x', 'E', 'C'],
    #           ['z', 'z', 'z', 'z', 'R']]) == False
    
    assert hypercube([["h","h","h","y"],
                      ["a","a","d","p"],
                      ["b","e","x","e"],
                      ["u","c","c","r"]]) == False
    
    print("Coding complete? Click 'Check' to earn cool rewards!")