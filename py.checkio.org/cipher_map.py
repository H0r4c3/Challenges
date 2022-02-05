'https://py.checkio.org/en/mission/cipher-map2/'

'''
A cipher grille is a 4×4 square of paper with four windows cut out. 
Placing the grille on a paper sheet of the same size, the encoder writes down the first four symbols of his password inside the windows (see fig. below). 
After that, the encoder turns the grille 90 degrees clockwise. The symbols written earlier become hidden under the grille and clean paper appears inside the windows. 
The encoder then writes down the next four symbols of the password in the windows and turns the grille 90 degrees again. 
Then, they write down the following four symbols and turn the grille once more. Lastly, they write down the final four symbols of the password.

Input: A cipher grille and a ciphered password as a tuples of strings.

Output: The password as a string.
'''

import numpy as np
from typing import List

def masking(grille_, password_):
    # creating the mask of grille_arr where condition grille_arr == 'X' is True
    mask = np.ma.masked_where(grille_ != 'X', grille_)
    #print(mask)

    # getting the mask of the array
    result_mask = np.ma.getmask(mask)

    # masking the array1 with the result of mask of array2
    masked = np.ma.masked_array(password_, mask=result_mask)

    # return all of non-masked data as a 1-D array
    masked_array = np.ma.compressed(masked)
    #print(masked_array)

    return masked_array

# Solution with prints
def recall_password_(grille: List[str], password: List[str]) -> str:
    # your code here
    grille_lists = list(map(list, grille))
    grille_arr = np.array(grille_lists)
    grille_arr1 = np.rot90(grille_arr, 1, (1,0))
    grille_arr2 = np.rot90(grille_arr, 2, (1,0))
    grille_arr3 = np.rot90(grille_arr, 3, (1,0))
    print(grille_arr)
   # print(grille_arr1)
   # print(grille_arr2)
   # print(grille_arr3)
    
    pw_lists = list(map(list, password))
    pw = np.array(pw_lists)
    print(pw)
   
    masked_array = masking(grille_arr, pw)
    masked_array1 = masking(grille_arr1, pw)
    masked_array2 = masking(grille_arr2, pw)
    masked_array3 = masking(grille_arr3, pw)
    print(masked_array)
    print(masked_array1)
    print(masked_array2)
    print(masked_array3)
    
    result = np.concatenate((masked_array, masked_array1, masked_array2, masked_array3))
    print(f'result = {result}')
    
    return ''.join(result)
 
 
def recall_password(grille: List[str], password: List[str]) -> str:
    grille_lists = list(map(list, grille))
    
    grille_arr = np.array(grille_lists)
    grille_arr1 = np.rot90(grille_arr, 1, (1,0))
    grille_arr2 = np.rot90(grille_arr, 2, (1,0))
    grille_arr3 = np.rot90(grille_arr, 3, (1,0))
    
    pw_lists = list(map(list, password))
    pw = np.array(pw_lists)
   
    masked_array = masking(grille_arr, pw)
    masked_array1 = masking(grille_arr1, pw)
    masked_array2 = masking(grille_arr2, pw)
    masked_array3 = masking(grille_arr3, pw)
    
    result = np.concatenate((masked_array, masked_array1, masked_array2, masked_array3))
    #print(f'result = {result}')
    
    return ''.join(result)
 
 


if __name__ == '__main__':
    print("Example:")
    print(recall_password(['X...', '..X.', 'X..X', '....'], ['itdf', 'gdce', 'aton', 'qrdi']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert recall_password(['X...', '..X.', 'X..X', '....'], ['itdf', 'gdce', 'aton', 'qrdi']) == 'icantforgetiddqd'
    assert recall_password(['....', 'X..X', '.X..', '...X'], ['xhwc', 'rsqx', 'xqzz', 'fyzr']) == 'rxqrwsfzxqxzhczy'
    print("Coding complete? Click 'Check' to earn cool rewards!")