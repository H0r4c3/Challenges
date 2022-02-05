'https://py.checkio.org/en/mission/scytale-encryption/'

'''
For example, suppose the message is "let's meet at eleven in the evening" and diameter of the rod allows to write 4 letters in a circle. 
The scytale with a message written on it would look like this:

Input: ciphertext: str, crib: str

Output: plaintext: str or None
'''

from typing import Optional

import numpy as np
import textwrap
def scytale_decipher(ciphertext: str, crib: str) -> Optional[str]:
    result = list()
    for k in range(2, len(ciphertext)):
        # split the string in parts of length k
        text_list = textwrap.wrap(ciphertext, k)
        
        r = len(text_list[0]) - len(text_list[-1])
        # fill the last string with spaces to have the same length as the other
        text_list[-1] = text_list[-1] + r*' '
        
        # transform the strings in lists of chars
        list_of_chars = [list(item) for item in text_list]
        
        # transform the list in array having the rows swapped with the columns
        arr = np.array(list_of_chars, dtype=object).transpose()
        
        # collapse the array into one dimension
        result_list = arr.flatten()
        
        # transform into a string having the spaces eliminated
        result_string = ''.join(result_list).replace(' ', '')
        
        if crib in result_string:
            result.append(result_string)
        
    if len(result) > 1 or len(result) == 0:
        return None
    else:
        return result[0]
    
    
    
# Same solution, but with prints        
def scytale_decipher_(ciphertext: str, crib: str) -> Optional[str]:
    result = list()
    for k in range(2, len(ciphertext)):
        text_list = textwrap.wrap(ciphertext, k)
        print(text_list)
        r = len(text_list[0]) - len(text_list[-1])
        text_list[-1] = text_list[-1] + r*' '
        list_of_chars = [list(item) for item in text_list]
        print(list_of_chars)
        arr = np.array(list_of_chars, dtype=object).transpose()
        print(arr)
        
        result_list = arr.flatten()
        result_string = ''.join(result_list).replace(' ', '')
        print(result_string)
        print(crib)
        
        if crib in result_string:
            result.append(result_string)
            
    print(result)
        
    if len(result) > 1 or len(result) == 0:
        return None
    else:
        return result[0]



if __name__ == "__main__":
    print("Example:")
    #print(scytale_decipher("aaaatctwtkdn", "dawn"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert scytale_decipher("aaaatctwtkdn", "dawn") == "attackatdawn"
    assert scytale_decipher("hdoeerlallrdow", "world") == "hellodearworld"
    assert (scytale_decipher("totetshpmeecisendysescwticsriasraytlaegphet", "sicret") == None), "Crib is not in plaintext"
    assert (scytale_decipher("aaaatctwtkdn", "at") == None), "More than one possible decryptions"

    print("Coding complete? Click 'Check' to earn cool rewards!")