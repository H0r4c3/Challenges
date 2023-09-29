'https://py.checkio.org/en/mission/count-divisibles-in-range/'

'''
Given three integers start, end, n, so that start <= end, 
count how many integers between start and end, 
inclusive, are evenly divisible by n. 
'''
import math

def count_divisibles_(start: int, end: int, n: int) -> int:
    divs = [div for div in range(start, end+1) if div % n == 0]
    result = len(divs)
    
    print(result)    
    return result


# BEST SOLUTION
def count_divisibles(start: int, end: int, n: int) -> int:
    divs = (end // n) - ((start - 1) // n)
    return divs
    


print("Example:")
print(count_divisibles(1, 9, 3))

# These "asserts" are used for self-checking
assert count_divisibles(8, 12, 4) == 2
assert count_divisibles(7, 28, 4) == 6
assert count_divisibles(-77, 19, 10) == 9
assert count_divisibles(1, 999999999999, 5) == 199999999999
assert count_divisibles(0, 999999999999, 5) == 200000000000
assert count_divisibles(-1000000000000, 1000000000000, 12345) == 162008911

print("The mission is done! Click 'Check Solution' to earn rewards!")