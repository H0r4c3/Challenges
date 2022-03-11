'https://py.checkio.org/en/mission/simple-hashlib/'

'''
In a correctly designed system, a plain password is not stored in the database. 
Instead, a hash of the password is stored. You are going to verify a password and you will need to use 
the same one-way function to calculate the hash and do a comparison.

Input: Two arguments. A string to be hashed and a hash algorithm as a string (unicode utf8).

Output: Hexadecimal hash for for input string using given algorithm as a string.
'''
import hashlib
def checkio(hashed_string, algorithm):
    return  hashlib.new(algorithm, hashed_string.encode()).hexdigest()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
    print('Done!')