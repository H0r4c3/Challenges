'https://py.checkio.org/en/mission/common-tail/'

'''
You are given two lists of integers. Elements are unique inside each list. 
These lists may have common element(s). But we are interested in the common element(s) at the end of the lists. 
Your function should return an element, from what a common part starts and there are no different element(s) 
after this part - the first element of the last common part (common tail). If there is no such 
element (lists don't end with common element) your function should return None. 
'''

def common_tail(a: list[int], b: list[int]) -> int | None:
    print(a, b)
    
    try:
        if a[-1] != b[-1]:
            return None
    except:
        return None
    
    z = list(zip(a[::-1], b[::-1]))
    print(z)
    
    for item in z:
        if item[0] != item[1]:
            idx = z.index(item)
            return (z[idx-1])[0]
        
    return a[0]


print("Example:")
print(common_tail([1, 2, 3, 4], [5, 6, 3, 4]))

# These "asserts" are used for self-checking
assert common_tail([], [1, 2, 3]) == None
assert common_tail([1], [1]) == 1
assert common_tail([3], [1, 2, 3]) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")