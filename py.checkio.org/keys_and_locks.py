'https://py.checkio.org/en/mission/keys-and-locks/'

'''
As input you are getting two multi-line strings - one is a schematic image of the keyhole, the second - of the key. 
Your task is to return True if the key fits the lock and False if otherwise. 
The key and keyhole are represented by the '#' symbols, and '0' shows the empty space around the key and the door material around the keyhole. 
Pay attention that the key and keyhole can be displayed both vertically and horizontally.
'''

# My Solution:

import numpy as np

def rot90(arr, n):
        return np.rot90(arr, n)

def transform(arr):
    '''delete the '0' rows'''
    for n in range(4):
        arr = np.rot90(arr, n) # n = 1 = counterclockwise
        while all(symbol == '0' for symbol in arr[0]):
            arr = arr[1:]
            
    return arr
    

def keys_and_locks(lock, some_key):
    lock_list = [list(item) for item in lock.split()]
    lock_arr = np.array(lock_list)
    
    some_key_list = [list(item) for item in some_key.split()]
    some_key_arr = np.array(some_key_list)
    
    # rotations without transformations
    if np.array_equal(lock_arr, some_key_arr):
        return True
    
    some_key_arr1 = rot90(some_key_arr, 1)
    if np.array_equal(lock_arr, some_key_arr1):
            return True
        
    some_key_arr2 = rot90(some_key_arr, 2)
    if np.array_equal(lock_arr, some_key_arr2):
            return True
        
    some_key_arr3 = rot90(some_key_arr, 3)
    if np.array_equal(lock_arr, some_key_arr3):
            return True
    
    lock_arr, some_key_arr = transform(lock_arr), transform(some_key_arr)
    
    for n in range(1, 4):
        if np.array_equal(lock_arr, some_key_arr):
            return True
        
        some_key_arr = np.rot90(some_key_arr, n)
        
    return False
    
    



# Best Solution: 
# https://py.checkio.org/mission/keys-and-locks/publications/Tinus_Trotyl/python-3/first/share/be2adf0b51ff77d5cdb0fe190a0c7153/

def turn90(key):
    return [''.join([line[::-1][i] for line in key])for i in range(len(key[0]))]if key else[]

def trim(key):
    for n in range(4):
        while key and not '#' in key[0]: key = key[1:]
        key = turn90(key)
    return key
    
def keys_and_locks_(lock, key):
    lock, key = trim(lock.split()), trim(key.split())
    for n in range(4):
        if lock == key: break
        key = turn90(key)
    return lock == key



# Another Best Solution: 
# https://py.checkio.org/mission/keys-and-locks/publications/tom-tom/python-3/rotating-images/?ordering=most_voted&filtering=all

def keys_and_locks_(lock, some_key):
    def prepare(image):
        return strip(rotate(strip(([1 if c == '#' else 0 for c in row] for row in image.split()))))
    
    def strip(image):
        return tuple(filter(any, image))
    
    def rotate(image):
        return tuple(zip(*image[::-1]))
    
    lock, some_key = map(prepare, (lock, some_key))
    return some_key in (lock, rotate(lock), rotate(rotate(lock)), rotate(rotate(rotate(lock))))


# Another Best Solution:
# https://py.checkio.org/mission/keys-and-locks/publications/juestr/python-3/first/?ordering=most_voted&filtering=all

def keys_and_locks_(lock, key):
    
    def rot90(x):
        return list(zip(*reversed(x)))
    
    def norm(x):
        x = x.strip().splitlines()
        for i in range(4):
            x = rot90(x)
            while all(c == '0' for c in x[0]):
                x = x[1:]
        return x

    lock, key = norm(lock), norm(key)
    for i in range(4):
        if lock == key:
            return True
        key = rot90(key)
    return False


if __name__ == '__main__':
    print("Example:")
    print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000''') == True

    assert keys_and_locks('''
###0
00#0''',
'''
00000
00000
#0000
###00
0#000
0#000''') == False

    assert keys_and_locks('''
0##0
0#00
0000''',
'''
##000
#0000
00000
00000
00000''') == True

    assert keys_and_locks('''
###0
0#00
0000''',
'''
##00
##00''') == False
    
    
    assert keys_and_locks('''
0#00000##0
0########0
0#00000##0''',
'''
0##00000#0
0########0
0##00000#0''')

    print("Coding complete? Click 'Check' to earn cool rewards!")