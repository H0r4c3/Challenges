'https://www.hackerrank.com/challenges/making-anagrams/problem?isFullScreen=true'

'''
Given two strings,  and , that may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. 
Any characters can be deleted from either of the strings.
'''

def makingAnagrams(s1, s2):
    
    for char in s1:
        if char in s2:
            s1 = s1.replace(char, '', 1)
            s2 = s2.replace(char, '', 1)
    
    print(s1)
    print(s2)
    
    result = len(s1) + len(s2)
    
    print(result)
    return result


if __name__ == '__main__':
    s1 = 'absdjkvuahdakejfnfauhdsaavasdlkj'
    s2 = 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'
    
    #s1 = 'abcd'
    #s2 = 'aabb'
    
    assert makingAnagrams(s1, s2) == 19
    
    print('Done!!!')