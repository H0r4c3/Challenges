'https://py.checkio.org/en/mission/not-in-order/share/fdfd83d2a61293ec2cc97b7ce9664d34/'

'''
You are given a list of integers. Your function should return the number of elements, 
which are not at their places as if the list would be sorted ascending. 
For example, for the sequence 1, 1, 4, 2, 1, 3 the result is 3, since elements at indexes 2, 4, 5 
(remember about 0-based indexing in Python) are not at their places as in the same sequence sorted ascending - 1, 1, 1, 2, 3, 4.
'''

def not_order(data: list[int]) -> int:
    no = 0
    
    print(data)
    
    data_sort = sorted(data)
    print(data_sort)
    
    pairs = zip(data, data_sort)
    for item in pairs:
        if item[0] != item[1]:
            no += 1
    print(no)
    return no


print("Example:")
print(not_order([1, 1, 4, 2, 1, 3]))

assert not_order([1, 1, 4, 2, 1, 3]) == 3
assert not_order([]) == 0
assert not_order([1, 1, 1, 1, 1]) == 0
assert not_order([1, 2, 3, 4, 5]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")