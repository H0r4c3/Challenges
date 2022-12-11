'https://py.checkio.org/en/mission/adjacent-letters/'

'''
You are given a string, where all letters are of same case. This string could include adjacent letters - two the same letters together ("aa", "bb" etc). 
Your task in this mission is to remove both these letters. 
If after removing one pair a new appears - remove it as well! Each such pair should be removed from string until no one remains.
'''

def adjacent_letters(line: str) -> str:
    line_list = list(line)
    print(line_list)
    
    i = 0
    
    while i < len(line_list)-1:
        if line_list[i] == line_list[i+1]:
            line_list.pop(i)
            line_list.pop(i)
            print(line_list)
            i = 0
        else:
            i +=1
    
    print(line_list)
            
    return ''.join(line_list)


# Best Solution: 
# https://py.checkio.org/mission/adjacent-letters/publications/kurosawa4434/python-3/recursion/?ordering=most_voted&filtering=all

from re import sub, search

reg = r'(.)\1'


def adjacent_letters_(line: str) -> str:
    return line if not search(reg, line) else adjacent_letters(sub(reg, '', line))




print("Example:")

assert adjacent_letters("abbaca") == "ca"
assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")