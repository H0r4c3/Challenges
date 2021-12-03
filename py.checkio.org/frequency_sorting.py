'https://py.checkio.org/en/mission/frequency-sorting/'

'''
Your mission is to sort the list by the frequency of numbers included in it. 
If a few numbers have an equal frequency - they should be sorted according to their natural order. 
For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]
'''

from typing import List
from collections import Counter
from itertools import repeat

def frequency_sorting(numbers: List[int]) -> List[int]:
    result = list()
    
    numbers_sorted = sorted(numbers)
    
    counts = Counter(numbers_sorted)
    counts_list = counts.most_common()
    
    for item in counts_list:
        result.extend(repeat(item[0], item[1]))
    
    return result


if __name__ == "__main__":
    print("Example:")
    print(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4,4,4,3,3,11,11,7,13,], "Not sorted"
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10,10,21,21,55,55,99,99,], "Reversed"