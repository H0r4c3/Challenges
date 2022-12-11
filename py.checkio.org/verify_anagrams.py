'https://py.checkio.org/en/mission/verify-anagrams/'

'''
You are given two words or phrase. Try to verify are they anagrams or not.

Input: Two arguments as strings.

Output: Are they anagrams or not as boolean (True or False)
'''

def verify_anagrams(a, b):
    #a, b = a.replace(' ', ''), b.replace(' ', '')
    a, b = sorted(a.lower().replace(' ', '')), sorted(b.lower().replace(' ', ''))
    
    print(a)
    print(b)
    
    return a==b


if __name__ == '__main__':
    print("Example:")
    print(verify_anagrams('Programming', 'Gram Ring Mop'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('Kyoto', 'Tokyo') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")