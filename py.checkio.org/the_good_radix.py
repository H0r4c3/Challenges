'https://py.checkio.org/en/mission/good-radix/'

'''
You are given some number n written as a string with the radix equal to k (1 < k < 37) . We know that our number is divisible by (k - 1) without a remainder. You should find the minimal possible k , if it exists, or return 0.

For example: n = "18". As we can see k should be greater than 8.
If k == 9, then n = 17 in the decimal system and 17 % 8 == 1. The wrong radix.
If k == 10, then n = 18 in the decimal system and 18 % 9 == 0. We found the answer.
Input: A number as a string.

Output: The radix k as an integer.
'''
import re
import string

def checkio(number: str):
    regex = re.compile('[A-Z0-9]')
    number_list = regex.findall(number)
    
    alphabet = list(string.ascii_uppercase)
    numbers = list(range(10, 36))
    values = dict(zip(alphabet, numbers))
    
    print(number_list)
    
    number_converted = list()
    
    for item in number_list:
        if item in values:
            number_converted.append(values[item])
            
        else:
            number_converted.append(int(item)) 
            
    print(number_converted)
            
    max_nr = max(number_converted)
        
    for k in range(max_nr + 1, 37):
        rest = int(number, k) % (k - 1)
        if rest == 0:
            return k
    
    return 0


# https://py.checkio.org/mission/good-radix/publications/veky/python-3/the-good-solution/share/21ab5c4b0069066108b7e366eb956d5a/
def checkio_BEST(number):
    def good(base):
        from contextlib import suppress
        with suppress(ValueError): return not int(number, base) % (base - 1)
    return next(filter(good, range(2, 37)), 0)


if __name__ == '__main__':
    assert checkio("A23B") == 14, "It's not a hex"
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k does not exist"
    print('Local tests done')