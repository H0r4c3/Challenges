'https://py.checkio.org/en/mission/excel-column-number/share/1c86fe4b43d5869bbc3d67d5c7ca6212/'

'''
Given a string that represents the column title as appears in an Excel sheet, return its corresponding column number.

Input: String.

Output: Int.
'''
from string import ascii_uppercase

def column_number(name: str) -> int:
    letters_numbers = {key:value+1 for value, key in enumerate(ascii_uppercase)}
    col_num = 0
        
    for i in range(0, len(name)):
            col_num = col_num + letters_numbers.get(name[i]) * 26**(len(name) - 1 - i)
        
    # if len(name) == 1:
    #     return letters_numbers.get(name[0]) * 26**0
    # elif len(name) == 2:
    #     col_num = letters_numbers.get(name[0]) * 26**1 + letters_numbers.get(name[1])
    # elif len(name) == 3:
    #     col_num = letters_numbers.get(name[0]) * 26**2 + letters_numbers.get(name[1]) * 26**1 + letters_numbers.get(name[2])
    # ...    
    # elif len(name) == n:
    #     col_num = letters_numbers.get(name[0]) * 26**(n-1) + letters_numbers.get(name[1]) * 26**(n-2) + ... + letters_numbers.get(name[n]) * 26**0
            
    return col_num


print("Example:")
print(column_number("AA"))
print(column_number("AAA"))
print(column_number("FXSHRXW")) # -> 2147483647

assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701
assert column_number("FXSHRXW") == 2147483647