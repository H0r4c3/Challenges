'https://py.checkio.org/en/mission/short-string-conversion/'

'''
You are given two strings, line1 and line2. Answer, what is the smallest number of operations you need to do in order to transform line1 into the line2?

Possible operations:

Delete one letter from one of the strings.
Insert one letter into one of the strings.
Replace one of the letters in one of the strings with another letter.
'''

def steps_to_convert(line1, line2):
    print(f'line1 = {line1}')
    print(f'line2 = {line2}')
    
    enum = enumerate(zip(line1, line2))
    
    # list of indexes where letters are different
    idx_diff_list = [idx for idx, (letter1, letter2) in enum if letter1 != letter2]
    print(f'idx_diff_list = {idx_diff_list}')
    
    if (not idx_diff_list) or (line1 in line2):
        return abs(len(line1) - len(line2))
    else:
        return len(idx_diff_list)
    
    


#Best Solution: 
# https://py.checkio.org/mission/short-string-conversion/publications/kkkkk/python-3/compare-string-count-diffs-look-for-substrings-else-return-count-of-diffs/?ordering=most_voted&filtering=all

def steps_to_convert_(line1, line2):
    '''
    Compare string, count diffs, look for substrings, else return count of diffs
    '''
    
    diffs = [i for i, (c1, c2) in enumerate(zip(line1, line2)) if c1 != c2]
    if not diffs or line1 in line2:
        # Either the lines are the same or one line is a subset of the other.
        # If the lengths are different, then the steps needed to insert or delete letters is the lengths difference.
        return abs(len(line1) - len(line2))
    return len(diffs)


# Best Solution:
# https://py.checkio.org/mission/short-string-conversion/publications/przemyslaw.daniel/python-3/string-conversion/?ordering=most_voted&filtering=all

from functools import lru_cache

@lru_cache(maxsize=1000)
def steps_to_convert_(a, b):
    if len(a)*len(b) == 0:
        return max(len(a), len(b))

    p = steps_to_convert(a[1:], b[1:])
    if a[0] != b[0]:
        q = steps_to_convert(a[1:], b)
        r = steps_to_convert(a, b[1:])
        return 1+min(p, q, r)
    return p



if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert steps_to_convert("line1", "line1") == 0, "eq"
    assert steps_to_convert("line1", "line2") == 1, "2"
    assert steps_to_convert("line", "line2") == 1, "none to 2"
    assert steps_to_convert("ine", "line2") == 2, "need two more"
    assert steps_to_convert("line1", "1enil") == 4, "everything is opposite"
    assert steps_to_convert("", "") == 0, "two empty"
    assert steps_to_convert("l", "") == 1, "one side"
    assert steps_to_convert("", "l") == 1, "another side"
    print("You are good to go!")

