'https://py.checkio.org/en/mission/even-last/'

'''
You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.
'''

def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    if array == []:
        return 0
    
    result = sum([array[i] for i in range(0, len(array), 2)]) * array[-1]
    
    
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([-37,-36,-19,-99,29,20,3,-7,-64, 84, 36, 62, 26,-76, 55, -24, 84, 49, -65, 41])) # -> 41*(-37-19+29+3-64+36+26+55+84-65) = 1968
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"