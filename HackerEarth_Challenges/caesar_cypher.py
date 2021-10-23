'https://www.hackerearth.com/problem/algorithm/caesar-cipher-5-6d64ed9d/'

'''
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts 
each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to 
the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Input Format:

The first line contains the integer, n, the length of the unencrypted string. 
The second line contains the unencrypted string, s. 
The third line contains k, the number of letters to rotate the alphabet by.
'''

import logging

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\HackerRank_Challenges\caesar_cipher.log'

#Create and configure logger
#logging.basicConfig(filename=path, format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

logger = logging.getLogger('main')


alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesarCipher(s, k):
    t = ''
    
    if k > 26:
            k = k % 26
    
    for i in range(n):
        if str(s[i]).islower():
            logging.debug(f's[i] = {s[i]}')
            ind = alphabet_lower.index(s[i])
            logging.debug(f'index of {s[i]} in alphabet_lower = {ind}')
            if ind + k > 25:
                ind = ind + k - 26
                logging.debug(f'ind = {ind}')
                t = t + alphabet_lower[ind]
            else:
                t = t + alphabet_lower[ind + k]
            logging.debug(f'index of {t[i]} in alphabet_upper = {ind+k}')
            logging.debug(f't = {t}')
        elif str(s[i]).isupper():
            logging.debug(f's[i] = {s[i]}')
            ind = alphabet_upper.index(s[i])
            logging.debug(f'index of {s[i]} in alphabet_upper = {ind}')
            if ind + k > 25:
                ind = ind + k - 26
                logging.debug(f'ind = {ind}')
                t = t + alphabet_upper[ind]
            else:
                t = t + alphabet_upper[ind + k]
            logging.debug(f'index of {t[i]} in alphabet_upper = {ind+k}')
            logging.debug(f't = {t}')
        else:
            t = t + s[i]
            logging.debug(f't = {t}')
    
    return t
        
    
    
s = 'Adfsfsdfsx - Baglljlz'
s = 'Xx - Zz'
s = 'middle-Outz'  # -> okffng-Qwvb
n = 20
n = 7
n = 11
k = 27

t = caesarCipher(s, k)
print(s)
print(t)