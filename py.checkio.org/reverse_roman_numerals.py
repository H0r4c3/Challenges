'https://py.checkio.org/en/mission/reverse-roman-numerals/'

'''
In this CheckiO mission Roman Numerals you have to convert a decimal number into its representation as a Roman number.
Here you have to do the same but the other way around.

You are given a Roman number as a string and your job is to convert this number into its decimal representation.

A valid Roman number, in the context of this mission, will only contain Roman numerals as per the below table and follow the rules of the subtractive notation.
Check out this Wikipedia article for more details on how to form Roman numerals.

Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)
Input: A Roman number as a string.

Output: The decimal representation of the Roman number as an int.
'''

from collections import OrderedDict

def reverse_roman(roman_string):
    roman = OrderedDict()
    
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    
    #roman_list = list(roman_string)
    #integers_list = [roman[key] for key in roman_list]
    #print(roman_list, integers_list)
    
    for i in range(len(roman_string) - 1):
        if roman.get(roman_string[i]) < roman.get(roman_string[i+1]):
            result -= roman.get(roman_string[i])
        else:
            result += roman.get(roman_string[i])
            
    result += roman.get(roman_string[-1])
    print(result)
            
    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!')