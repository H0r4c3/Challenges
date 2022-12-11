'https://www.hackerrank.com/challenges/game-of-thrones/problem?h_r=internal-search'

'''
Given a string, determine if it can be rearranged into a palindrome. Return the string YES or NO.
'''

def gameOfThrones(s):
    repetitions = sorted([s.count(char) for char in set(s)])
    print(repetitions)
    
    if len(s) % 2 == 0 and all(map(lambda x : x%2, repetitions)):
        return 'YES'
    if len(s) % 2 != 0:
        odd_items = [item for item in repetitions if item%2]
        print(odd_items)
        if len(odd_items) < 2:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'
    
    
# Best Solution: 
# https://www.hackerrank.com/challenges/game-of-thrones/forum

def gameOfThrones_(s):
    return "YES" if len([i for i in set(s) if s.count(i)%2 != 0]) <2 else "NO"
        
        
if __name__ == '__main__':
    s = 'aabbccd' # -> abcdcba = Palindrome
    s = 'aaabbbb'
    s = 'cdefghmnopqrstuvw'
    
    assert gameOfThrones('aabbccd') == 'YES'
    assert gameOfThrones('aaabbbb') == 'YES'
    assert gameOfThrones('abc') == 'NO'
    print('Done!!!')