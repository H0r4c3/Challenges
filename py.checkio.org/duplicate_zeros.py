'https://py.checkio.org/en/mission/duplicate-zeros/'

'''
You are given a list of integers. Your task in this mission is to double all the zeros in the given list
'''
import numpy as np

def duplicate_zeros(donuts: list) -> list:
    donuts_z = [item if item != 0 else [0, 0] for item in donuts]
    print(donuts_z)
    donuts_zz = [y for x in donuts_z for y in (x if isinstance(x, list) else (x,))]
    print(donuts_zz)
    
    return donuts_zz


print("Example:")
#print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))

assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert duplicate_zeros([100, 10, 0, 101, 1000]) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")