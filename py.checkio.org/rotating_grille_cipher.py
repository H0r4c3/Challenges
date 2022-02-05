'https://py.checkio.org/en/mission/rotating-grille-cipher/'

'''
Rotating grille cipher is a transposition cipher that uses a special square sheet of cardboard (the grille ) with holes cut in it. 
To encrypt a message, sender must place the grille on an empty sheet of paper and write letters of the plaintext into the holes left to right, top to bottom. 
After filling all the holes, the grille is rotated 90 degrees clockwise (the holes move to empty spaces) and the process continues. 
After the grille was rotated 2 more times, there should be no empty spaces on the paper; 
if the message is not finished, the algorithm is repeated on the next sheet.

Input: plaintext: str, grille: list of str (positions of holes are marked by "Х" )

Output: ciphertext: str or None

In this task you are given a message and a key (4x4 square grille); length of the message is divisible by 16. 
You need to encrypt a message with the rotating grille cipher. There is a problem, though: some of the keys are defective. 
A "correct" key is made in such a way that, when laid over a grid and rotated around, every cell is shown exactly once. 
So with defective keys, either some cells are shown more than once, or after applying the key in all four directions there are still unfilled spaces on the sheet.
'''

from typing import List, Optional

import numpy as np

def replacings(grille_arr, plaintext):
    '''replaces X with chars from plaintext'''
    i = 0
    if np.count_nonzero(grille_arr == 'X') != 4:
        return None
    for row in grille_arr:
        for j in range(4):
            if row[j] == 'X':
                row[j] = plaintext[i]
                i += 1
    return grille_arr
        

def grille_encrypt_BACKUP(plaintext: str, grille: List[str]) -> Optional[str]:
    grille_list_of_chars = list(''.join(grille))
    if grille_list_of_chars.count('X') != 4:
        return None
    
    grille_lists = list(map(list, grille))
    
    grille_arr1 = np.array(grille_lists)
    grille_arr11 = grille_arr1.copy()
    grille_arr2 = np.rot90(grille_arr1, 1, (1,0))
    grille_arr12 = grille_arr2.copy()
    grille_arr3 = np.rot90(grille_arr1, 2, (1,0))
    grille_arr13 = grille_arr3.copy()
    grille_arr4 = np.rot90(grille_arr1, 3, (1,0))
    grille_arr14 = grille_arr4.copy()

    # replace X with chars from plaintext
    grille_arr11 = replacings(grille_arr11, plaintext[:4])
    grille_arr12 = replacings(grille_arr12, plaintext[4:8])
    grille_arr13 = replacings(grille_arr13, plaintext[8:12])
    grille_arr14 = replacings(grille_arr14, plaintext[12:16])
    
    # copy all grilles over the first one
    grille_arr11[grille_arr11=='.'] = grille_arr12[grille_arr11=='.']
    grille_arr11[grille_arr11=='.'] = grille_arr13[grille_arr11=='.']
    grille_arr11[grille_arr11=='.'] = grille_arr14[grille_arr11=='.']
    
    result16 = ''.join(np.ma.compressed(grille_arr11))
    if '.' in result16:
        return None
    
    if len(plaintext) == 16:
        if '.' in result16:
            return None
        return result16
    elif len(plaintext) == 32:
        plaintext1 = plaintext[0:16]
        plaintext2 = plaintext[16:33]
        r1 = grille_encrypt(plaintext1, grille)
        r2 = grille_encrypt(plaintext2, grille)
        result32 = r1 + r2
        if '.' in result32:
            return None
        return result32
    elif len(plaintext) == 64:
        plaintext1 = plaintext[0:16]
        plaintext2 = plaintext[16:32]
        plaintext3 = plaintext[32:48]
        plaintext4 = plaintext[48:64]
        r1 = grille_encrypt(plaintext1, grille)
        r2 = grille_encrypt(plaintext2, grille)
        r3 = grille_encrypt(plaintext3, grille)
        r4 = grille_encrypt(plaintext4, grille)
        result64 = r1 + r2 + r3 + r4
        print(result64)
        if '.' in result64:
            return None
        return result64
        

def grille_encrypt_1sheet(plaintext: str, grille: List[str]) -> Optional[str]:
    #result = ''
    grille_list_of_chars = list(''.join(grille))
    if grille_list_of_chars.count('X') != 4:
        return None
    
    grille_lists = list(map(list, grille))
    
    grille_arr1 = np.array(grille_lists)
    grille_arr11 = grille_arr1.copy()
    grille_arr2 = np.rot90(grille_arr1, 1, (1,0))
    grille_arr12 = grille_arr2.copy()
    grille_arr3 = np.rot90(grille_arr1, 2, (1,0))
    grille_arr13 = grille_arr3.copy()
    grille_arr4 = np.rot90(grille_arr1, 3, (1,0))
    grille_arr14 = grille_arr4.copy()

    # replace X with chars from plaintext
    grille_arr11 = replacings(grille_arr11, plaintext[:4])
    grille_arr12 = replacings(grille_arr12, plaintext[4:8])
    grille_arr13 = replacings(grille_arr13, plaintext[8:12])
    grille_arr14 = replacings(grille_arr14, plaintext[12:16])
    
    # copy all grilles over the first one
    grille_arr11[grille_arr11=='.'] = grille_arr12[grille_arr11=='.']
    grille_arr11[grille_arr11=='.'] = grille_arr13[grille_arr11=='.']
    grille_arr11[grille_arr11=='.'] = grille_arr14[grille_arr11=='.']
    
    result16 = ''.join(np.ma.compressed(grille_arr11))
    
    return result16
    
    
def grille_encrypt(plaintext: str, grille: List[str]) -> Optional[str]:
    result = ''
        
    while len(plaintext) >= 16:
        result16 = grille_encrypt_1sheet(plaintext, grille)
        print(f'result16 = {result16}')
        
        if result16 == None:
            return None
        
        if '.' in result16:
            return None
        
        result += result16
        print(f'intermediate_result = {result}')
        plaintext = plaintext[16:]
    
    print(f'final_result = {result}')    
    return result



if __name__ == "__main__":
    print("Example:")
    #print(grille_encrypt("cardangrilletest", [".X..", ".X..", "...X", "X..."]))

    # These "asserts" are used for self-checking and not for an auto-testing
    print('\n1\n')
    assert (grille_encrypt("cardangrilletest", [".X..", ".X..", "...X", "X..."]) == "actilangeslrdret")
    print('\n2\n')
    assert (grille_encrypt("quickbrownfoxjumpsoverthelazydog", ["X...", "...X", "..X.", ".X.."])== "qxwkbnjufriumcoopyeerldsatoogvhz")
    print('3\n')
    assert (grille_encrypt("quickbrownfoxjumpsoverthelazydog", [".XX.", ".XX.", "..X.", "X..."])== None)
    assert grille_encrypt("cardangrilletest", ["...X", "....", "....", "...."]) == None
    assert grille_encrypt("pythonsstandardlibraryisveryextensiveofferingawiderangeofstuffxx",["XX..","X...",".X..","...."]) == "pyontstsahradlndibryrivseaxeterynseoifefgvarwiindengrefofafsxxtu"
    assert grille_encrypt("youshouldreadeliezeryudkowskysrationalityfromaitozombiesitsgreat",["..X.","...X","....","X..X"]) == None
    assert grille_encrypt("theexampleaboveisaverysimpleandinsecurecaseofastencilcipherinsuchaciphercertainlettersonapagearepartofthesecretmessagetheyarehid",["....","X..X","..X.","...X"]) == "loxvteehaaebmipemarnspdalyvesiieafuansssereoetcchnlseeunrcciicpicapihenarhctelriaeraeprtastgoeneeroepstaefrctmhteegheyisaesrtdha"

    print("Coding complete? Click 'Check' to earn cool rewards!")