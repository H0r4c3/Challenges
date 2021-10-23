'https://www.hackerrank.com/challenges/pangrams/problem?h_r=internal-search'

'''
A pangram is a string that contains every letter of the alphabet. 
Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def pangrams(s):
    s_low = s.lower()
    s_low_list = s_low.split()
    s_low_s = ''.join(s_low_list)
    
    print(s_low_list)
    
    for item in s_low_s:
        if item not in alphabet:
            return item, 'not pangram 1'

    for item in alphabet:
        if item in s_low_s:
            pass
        else:
            return 'not pangram 2'
    
    return 'pangram'


s = 'The quick brown fox jumps over the lazy dog'

result = pangrams(s)
print(result)