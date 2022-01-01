'https://py.checkio.org/en/mission/most-numbers/'

'''
You are given an array of numbers (floats). You should find the difference between the maximum and minimum element. 
Your function should be able to handle an undefined amount of arguments. For an empty argument list, the function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. So we should check the result with ±0.001 precision.
Think about how to work with an arbitrary number of arguments.

Input: An arbitrary number of arguments as numbers (int, float).

Output: The difference between maximum and minimum as a number (int, float).
'''

def checkio(*args):
    my_list = list(args)
    
    if list(args) == []:
        return 0
    
    my_list_flat = [y for x in my_list for y in (x if isinstance(x, tuple) else (x,))]
    s = sorted(my_list_flat)
    print(s)
        
    return s[-1] - s[0]




# the best solution
# https://py.checkio.org/mission/most-numbers/publications/madmanbob/python-3/first/?ordering=most_voted&filtering=choice

def checkio_(*args):
    return max(args) - min(args) if args else 0




#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    print('Example:')
    print(checkio(1, 2, 3))
    
    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")