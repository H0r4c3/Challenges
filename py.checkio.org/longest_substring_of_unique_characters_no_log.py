'https://py.checkio.org/en/mission/longest-substring-of-unique-characters/'

'''
Given a string, find the length of the longest substring without repeating characters.
'''

def longest_substr(s: str) -> int:
    length, result = 1, 1
    if s:
        etalon = s[0]
    else:
        return 0
    
    for i in range(1, len(s)):
        if s[i] not in etalon:
            length += 1
            if length > result: 
                result = length
            etalon += s[i]
        else:
            pos = etalon.index(s[i])
            etalon = etalon[pos+1:] + s[i]
            length = len(etalon)
    
    print(result)    
    return result


print("Example:")
#print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3
assert longest_substr('anviaj') == 5
assert longest_substr('ohomm') == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")