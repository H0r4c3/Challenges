'https://py.checkio.org/en/mission/missing-number/'

'''
You are given a list of integers, which are elements of arithmetic progression - the difference between 
the consecutive elements is constant. But this list is unsorted and one element is missing
'''

def missing_number(items: list[int]) -> int:
    items.sort()
    
    # make a list with differences between consecutive items in sorted list
    diff = [items[i+1] - items[i] for i in range(len(items) - 1)]
    print(diff)
    
    # index of the maximum difference
    idx_max = diff.index(max(diff))
    print(idx_max)
    
    # sum of item in position of max arithmetic progression and the arithmetic progression
    result = items[idx_max] + int(max(diff) / 2)
    print(result)
    
    return result


print("Example:")
print(missing_number([1, 4, 2, 5]))

assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")