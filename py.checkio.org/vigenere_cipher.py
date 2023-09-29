'https://py.checkio.org/en/mission/vigenere-cipher/'

'''
In the Vigenère cipher, each letter of a message is shifted along some number of places with different shift values.
The alphabet used at each point depends on a repeating keyword.
'''

import numpy as np
import string

ALPHABET = list(string.ascii_uppercase)
#NUMBERS = list(range(0, 27))

def shifted_alphabet(shift):
    
    # shift the alphabet to the left
    sh_alphabet = ALPHABET[shift : ] + ALPHABET[ : shift]
    #print(sh_alphabet)
    
    return sh_alphabet

def make_tabula_recta():
    table = list()
    #table_head = {k:v for k, v in zip(ALPHABET, NUMBERS)}
    #print(table_head)
    
    for shift in range(0, 26):
        sh_alphabet = shifted_alphabet(shift)
        table.append(sh_alphabet)
    
    tabula_recta = np.array(table)
    
    return tabula_recta

def find_the_key(old_decrypted, old_encrypted):
    '''
    find the key:
    letter in old_decrypted (D) -> index of letter (D) in alphabet (3) -> column in tabula_recta [:,3] -> 
    -> letter in old_encrypted (F) -> index of letter (F), from old_encrypted, in column 3 (F has index 2) -> 
    -> letter in alphabet at index 2 (C) -> key = C
    '''
    
    key = list()
    idx_letter = -1
    
    for letter in old_decrypted:
        print(f'letter = {letter}')
        idx_letter += 1 
        
        idx_decrypted = ALPHABET.index(letter)
        print(f'idx_decrypted = {idx_decrypted}')
        
        #idx_decrypted = table_head[letter]
        
        col_tabula_recta = tabula_recta[:, idx_decrypted]
        print(f'col_tabula_recta = {col_tabula_recta}')
        
        letter_encrypted = old_encrypted[idx_letter]
        print(f'letter_encrypted = {letter_encrypted}')
        
        idx_encrypted = np.where(col_tabula_recta == letter_encrypted)[0][0]
        print(f'idx_encrypted = {idx_encrypted}')
        
        letter_key = ALPHABET[idx_encrypted]
        print(f'letter_key = {letter_key}')
        key.extend(letter_key)
        print(f'key = {key}')
    
    key = ''.join(key)
    
    return key

def make_sequence(key, length):
    '''Makes the sequence_key of length len(new_encrypted)'''
    sequence = key * (length//len(key) + 1)
    return sequence[:length]

def extract_key(sequence):
    '''Find the key string'''
    for i in range(1,len(sequence)+1):
        if make_sequence(sequence[:i], len(sequence)) == sequence: 
            return sequence[:i]
 
def use_key(new_encrypted, key):
    '''
    decode:
    letter in key (C) -> index of C in ALPHABET = 2 -> column in tabula_recta
    find letter from new_encrypted (D) in column of letter key (C) -> index of D
    letter in new_decrypted using the index of D (B)
    
    Encrypted: DLLCZXMFVRVGWFTF
    Key:       CHECKIOCHECKIOCH
    Message:   BEHAPPYDONTWORRY
    '''
    new_decrypted = list()
    idx_letter_key = -1
    
    for letter in new_encrypted:
        idx_letter_key += 1
        letter_key = key[idx_letter_key]
        print(f'letter_key = {letter_key}')
        
        idx_alphabet = ALPHABET.index(letter_key)
        
        col_tabula_recta = tabula_recta[:, idx_alphabet]
        print(f'col_tabula_recta = {col_tabula_recta}')
        
        idx_letter = np.where(col_tabula_recta == letter)[0][0]
        print(f'idx_letter = {idx_letter}')
        
        new_decrypted_letter = ALPHABET[idx_letter]
        print(f'new_decrypted_letter = {new_decrypted_letter}')
        
        new_decrypted.append(new_decrypted_letter)
        
    return ''.join(new_decrypted)
        
def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    global tabula_recta
    global table_head
    
    #table_head = {k:v for k, v in zip(ALPHABET, NUMBERS)}
    #print(table_head)
    
    tabula_recta = make_tabula_recta()
    #print(tabula_recta)
    
    print('--------------------')
    print('Finding KEY Started:')
    print('--------------------')
    key = find_the_key(old_decrypted, old_encrypted)
    print(f'key = {key}')
    
    key_ok = extract_key(key)
    print(f'key_ok = {key_ok}')
    
    key_sequence = make_sequence(key_ok, len(new_encrypted))
    print(key_sequence)
    
    print('--------------------')
    print('DECRYPTION Started:')
    print('--------------------')
    new_decrypted = use_key(new_encrypted, key_sequence)
    print(f'new_decrypted = {new_decrypted}')
    
    return new_decrypted



# Best Solution: 
# https://py.checkio.org/mission/vigenere-cipher/publications/TovarischZhukov/python-3/first/share/3511caa1af5fbfbf55f00ec86b8e3a9e/

def decode_vigenere_(old_decrypted, old_encrypted, new_encrypted):
    key = [chr (val+65) for i, elem in enumerate(old_decrypted) for val in range(26) if old_encrypted[i] == chr((val+ord(elem)-65)%26+65)]
    key= "".join(key)
    if len(old_encrypted) < len(new_encrypted) :
        for i in range(2, len(key)):
            k = key.find(key[:i], 1)
            if k == len(key[:i]):
                key = key[:i]
                break
    key = (len(new_encrypted)//len(key)+1)*key
    message = [chr (val+65) for i, elem in enumerate(new_encrypted) for val in range(26) if elem == chr((val+ord(key[i])-65)%26+65)]
    return "".join(message)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
    
    decode_vigenere("ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT", "PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI", "XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL")
    
    print('Done!')
