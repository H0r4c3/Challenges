'https://py.checkio.org/en/mission/long-non-repeat/'

'''
You need to find the first longest substring with all unique letters. 
For example, in substring "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one, so the answer is "abc".
'''

# Solution #1:
from collections import Counter
def check_unique(substring):
    freq = Counter(substring)
    if len(list(freq)) == len(substring):
        return True
    else:
        return False

from itertools import combinations
def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    if line == '':
        return ''
    
    length = len(line) + 1
    sub_list = [line[x:y] for x, y in combinations(range(length), r=2)]
    print(sub_list)
    
    sub_list_unique = [substring for substring in sub_list if check_unique(substring)]
    print(sub_list_unique)
    
    result = sorted(sub_list_unique, key=len, reverse=True)[0]
    
    return result


'''
Approach: The idea is to traverse the string and for each already visited character store its last occurrence in a hash table(Here unordered_map is 
used as a hash with key as character and value as its last position). The variable st stores the starting point of the current substring, maxlen stores 
the length of maximum length substring, and start stores the starting index of maximum length substring. While traversing the string, check whether the 
current character is present in the hash table or not. If it is not present, then store the current character in the hash table with value as the current index. 
If it is already present in the hash table, this means the current character could repeat in the current substring. For this check, if the previous occurrence of 
character is before or after the starting point st of the current substring. If it is before st, then only update the value in the hash table. 
If it is after st, then find the length of current substring currlen as i-st, where i is the current index. Compare currlen with maxlen. 
If maxlen is less than currlen, then update maxlen as currlen and start as st. 
After complete traversal of the string, the required the longest substring without repeating characters is from s[start] to s[start+maxlen-1]. 
'''

# Solution #2:
def non_repeat_(line):
    """
        the longest substring without repeating chars
    """
    if line == '':
        return ''
 
    n = len(line)
 
    # starting point of current substring.
    st = 0
    # maximum length substring without repeating characters.
    maxlen = 0
    # starting index of maximum length substring
    start = 0
    # Hash Map to store last occurrence of each already visited character
    pos = {}
    # Last occurrence of first character is index 0
    pos[line[0]] = 0
 
    for i in range(1, n):
 
        # If this character is not present in hash, then this is first occurrence of this character, store this in hash.
        if line[i] not in pos:
            pos[line[i]] = i
        else:
            # If this character is present in hash, then this character has previous occurrence,
            # check if that occurrence is before or after starting point of current substring.
            if pos[line[i]] >= st:
 
                # find length of current substring and update maxlen and start accordingly.
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
 
                # Next substring will start after the last occurrence of current character to avoid its repetition.
                st = pos[line[i]] + 1
             
            # Update last occurrence of current character.
            pos[line[i]] = i
         
    # Compare length of last substring with maxlen and update maxlen and start accordingly.
    if maxlen < i - st:
        maxlen = i - st
        start = st
     
    # The required longest substring without repeating characters is from string[start] to string[start + maxlen -1].
    return line[start : start + maxlen]
 

    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    assert non_repeat("") == None
    print('"Run" is good. How is "Check"?')