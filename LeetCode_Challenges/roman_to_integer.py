'https://leetcode.com/problems/roman-to-integer'

'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Given a roman numeral, convert it to an integer.
'''

import timeit
from collections import OrderedDict

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = OrderedDict()
    
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        for i in range(len(s) - 1):
            if roman.get(s[i]) < roman.get(s[i+1]):
                result -= roman.get(s[i])
            else:
                result += roman.get(s[i])

        result += roman.get(s[-1])

        return result
    
my_obj = Solution()
assert my_obj.romanToInt('III') == 3
assert my_obj.romanToInt('LVIII') == 58
print('Done!!!')


# calculate the speed of my solution
my_time = timeit.timeit("my_obj.romanToInt('LVIII')", number = 500_000, globals = globals())
print(f'my_obj.romanToInt(LVIII) repeated 500_000 times = {my_time} seconds')