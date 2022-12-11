'https://py.checkio.org/en/mission/one-switch-strings/share/0d04e765af4e3f7c85c9e32b7c3c69c4/'

'''
You are given two strings and need to determine whether you can swap two letters in the first string to get the second string. 
If so - return True, if not - False.
'''

from itertools import combinations

def swap(line, i, j):
    line_list = list(line)
    line_list[i], line_list[j] = line_list[j], line_list[i]
    
    new_line = ''.join(line_list)
    
    return new_line

def switch_strings(line: str, result: str) -> bool:
    print(line)
    swaps_list = [line]
    
    combs = list(combinations(range(len(line)), 2))
    print(combs)
    
    for item in combs:
        i, j = item
        new_line = swap(line, i, j)
        swaps_list.append(new_line)
        
    print(swaps_list)
    
    if result in swaps_list:
        return True
    else:
        return False


print("Example:")
#print(switch_strings("btry", "byrt"))

assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False
assert switch_strings("true", "treu") == True
assert switch_strings('fox', 'fox') == True

print("The mission is done! Click 'Check Solution' to earn rewards!")