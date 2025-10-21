'https://py.checkio.org/en/mission/sum-of-integers/'

'''
Calculate sum of integers from 1 to given N (including).
'''

def sum_upto_n(N: int) -> int:
    my_list = [number for number in range(N+1)]
    result = sum(my_list)
    print(result)
    
    return result


print("Example:")
print(sum_upto_n(11))

# These "asserts" are used for self-checking
assert sum_upto_n(1) == 1
assert sum_upto_n(2) == 3
assert sum_upto_n(3) == 6
assert sum_upto_n(4) == 10
assert sum_upto_n(5) == 15
assert sum_upto_n(10) == 55
assert sum_upto_n(20) == 210
assert sum_upto_n(100) == 5050
assert sum_upto_n(200) == 20100
assert sum_upto_n(500) == 125250

print("The mission is done! Click 'Check Solution' to earn rewards!")