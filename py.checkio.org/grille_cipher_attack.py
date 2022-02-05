'https://py.checkio.org/en/mission/grille-cipher-attack/share/a43dc10f231ee4e89a84be53c6d99bd4/'

'''
This is the fourth mission inspired by classical cryptography. In this mission we will attempt to break the Rotating Grille cipher. 
For more info on grille cipher check out missions Cipher Map and Rotating Grille Cipher - it's highly recommended that you've solved them before trying this one.

First, let's quickly go over the algorithm: the key to encryption is a square stencil with holes cut in it (in this mission we will use grille of size 8x8); 
the sender places the grille on a sheet and writes the first 16 letters of the message; then, turning the grille 90 degrees clockwise, 
the second 16 are written, and so on until the grid is filled. To decrypt a message, receiver arranges the cryptogram in an 8x8 square, 
places the grille on top of it and reads the letters in the holes, rotating the grille when necessary.

You are given two strings of text: a message and a corresponding cryptogram; both strings are 64 characters long. You need to find and return the grille used 
to encrypt the message. Like previous missions, the grille is a list of strings where "X" means hole, "." means no hole.

Important note: each input in this task is guaranteed to have a single solution.

Input: plaintext: string, cryptogram: string

Output: key: list of str size 8x8
'''

from typing import List

import numpy as np
import numpy.ma as ma

# Solution incomplete (not working)
def find_grille(plaintext: str, cryptogram: str) -> List[str]:
    crypto = list(cryptogram)
    crypto_arr = np.array(crypto).reshape(8, 8)
    print(crypto_arr)
    
    # plain = list(plaintext)
    # plain_arr1 = np.array(plain[:16]).reshape(4, 4)
    # plain_arr2 = np.array(plain[16:32]).reshape(4, 4)
    # plain_arr3 = np.array(plain[32:48]).reshape(4, 4)
    # plain_arr4 = np.array(plain[48:64]).reshape(4, 4)
    # print(plain_arr1)
    
    
    def find_mask(crypto_arr, plain):
        condition = (crypto_arr == plain[0]) | (crypto_arr == plain[1]) | (crypto_arr == plain[2]) | (crypto_arr == plain[3]) \
            | (crypto_arr == plain[4]) | (crypto_arr == plain[5]) | (crypto_arr == plain[6]) | (crypto_arr == plain[7]) \
            | (crypto_arr == plain[8]) | (crypto_arr == plain[9]) | (crypto_arr == plain[10]) | (crypto_arr == plain[11]) \
            | (crypto_arr == plain[12]) | (crypto_arr == plain[13]) | (crypto_arr == plain[14]) | (crypto_arr == plain[15])
    
        result = np.where(condition, 'X', '.')
        #print(result)
        return result
    
    plain = list(plaintext)
    plain1 = plain[:16]
    plain2 = plain[16:32]
    plain3 = plain[32:48]
    plain4 = plain[48:64]
    mask1 = find_mask(crypto_arr, plain1)
    #print(plain1)
    #print(mask1)
    mask2 = find_mask(crypto_arr, plain2)
    #print(plain2)
    mask2_rot = np.rot90(mask2, -1, (1,0))
    mask3 = find_mask(crypto_arr, plain3)
    #print(plain3)
    mask3_rot = np.rot90(mask3, -2, (1,0))
    mask4 = find_mask(crypto_arr, plain4)
    #print(plain4)
    mask4_rot = np.rot90(mask4, -3, (1,0))
    
    # print(mask1[0], mask2_rot[0], mask3_rot[0], mask4_rot[0])
    # print(mask1[1], mask2_rot[1], mask3_rot[1], mask4_rot[1])
    # print(mask1[2], mask2_rot[2], mask3_rot[2], mask4_rot[2])
    # print(mask1[3], mask2_rot[3], mask3_rot[3], mask4_rot[3])
    # print(mask1[4], mask2_rot[4], mask3_rot[4], mask4_rot[4])
    # print(mask1[5], mask2_rot[5], mask3_rot[5], mask4_rot[5])
    # print(mask1[6], mask2_rot[6], mask3_rot[6], mask4_rot[6])
    # print(mask1[7], mask2_rot[7], mask3_rot[7], mask4_rot[7])
    
    x, y = np.where(mask1 == 'X')
    set1 = set(zip(x, y))
    #print(sorted(list(set1)))
    x, y = np.where(mask2_rot == 'X')
    set2 = set(zip(x, y))
    #print(sorted(list(set2)))
    x, y = np.where(mask3_rot == 'X')
    set3 = set(zip(x, y))
    #print(sorted(list(set3)))
    x, y = np.where(mask4_rot == 'X')
    set4 = set(zip(x, y))
    #print(sorted(list(set4)))
    
    intersect = set1.intersection(set2, set3, set4)
    mask_pos = sorted(list(intersect))
    print(mask_pos)
    
    grille = np.full((8,8), '.')
    for item in mask_pos:
        grille[item[0], item[1]] = 'X'
    #print(grille[2])
    #print(grille[5])
    
    grille_list = grille.tolist()
    result = list(map(lambda x: ''.join(x), grille_list))
    print(result)
    
       
    return result


if __name__ == "__main__":
    print("Example:")
    # print(
    #     find_grille(
    #         "quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
    #         "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves",
    #     )
    # )

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert find_grille(
    #     "quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
    #     "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves",
    # ) == [
    #     "XXXX....",
    #     "XXXX....",
    #     "XXXX....",
    #     "XXXX....",
    #     "........",
    #     "........",
    #     "........",
    #     "........",
    # ]

    assert find_grille(
        "weareallfromxanthcubesaidquicklyjustvisitingphazewewontbeforlong",
        "wejhewucuaeswtbrveeoisantsalilbifdteifrqunooigrmplxcakhonnlagtyz",
    ) == [
        "X...X...",
        ".X.....X",
        "..X...X.",
        "...X.X..",
        "X.....X.",
        "...X...X",
        "..X.X...",
        ".X...X..",
    ]

    assert find_grille(
        "theideaofcognitivebiasinpsychologyworksinananalogouswayacognitiv",
        "tgovgeubyhsiawseiinorkdepaswoasifcyncyaanaognconaginihlttoiivloo",
    ) == [
        "X.......",
        ".X.....X",
        "X.....XX",
        ".X..X...",
        "XX......",
        "..XXX...",
        "..X....X",
        "...X....",
    ]

    print("Coding complete? Click 'Check' to earn cool rewards!")