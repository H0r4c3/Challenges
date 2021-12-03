'https://py.checkio.org/en/mission/unix-match-part-2/'

'''
You need to find out if the given unix pattern matches the given filename.

Here is a small table that shows symbols that can be used in patterns.

[seq]	matches any character in seq, for example [123] means any character - '1', '2' or '3'
[!seq]	matches any character not in seq, for example [!123] means any character except '1', '2' and '3'
[]	seq without any chars will never match
Note that the expression in one pair of square brackets responds only for 1 character. So

('0123', '[!abc]123') == True, but ('00123', '[!abc]123') = False

Input: Two arguments. Both are strings.

Output: Bool.
'''

import re

def unix_match(filename: str, pattern: str) -> bool:
    
    pattern = re.sub('\.', '\.', pattern)
    pattern = re.sub('\*', '.+', pattern)
    pattern = re.sub('\?', '.', pattern)
    pattern = re.sub('\[\!\]', '\[\!\]', pattern)
    pattern = re.sub('\[\!', '[^', pattern)
    pattern = re.sub('\[\]', '[^.]', pattern)
    pattern = re.sub('\[\^\]', '\[!\]', pattern)
    
    #pattern = pattern.replace("*", "\\*").replace(".", "\\.").replace("[!", "[^").replace("[]", "[^.]").replace("[^]", "\[!\]")
    
    print(f'pattern = {pattern}')
    
    regex = re.compile(pattern)
    
    result = re.search(regex, filename)
    print(result)
    
    if result == None:
        return False
    else:
        return True


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    assert unix_match("[!]check.txt", "[!]check.txt") == True
    assert unix_match("checkio", "[c[]heckio") == True