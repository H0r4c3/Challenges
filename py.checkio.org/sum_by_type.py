'https://py.checkio.org/en/mission/sum-by-type/'

'''
You have a list. Each value from that list can be either a string or an integer. Your task here is to return two values. The first one is a concatenation of all strings from the given list. The second one is a sum of all integers from the given list.

Input: An array of strings and integers

Output: A list or tuple
'''

from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    sum = 0
    string = ""
    result = list()
        
    for item in items:
        if isinstance(item, int):
            sum += item
        elif isinstance(item, str):
            string += item
            
    result = (string, sum)
    
    return result

# Not finished
def sum_by_types_(items: list) -> Tuple[str, int]:
    result = [sum([item]) if str(item).isdigit else [item] for item in items ]
    print(result)
    
    return result
    


if __name__ == "__main__":
    print("Example:")
    print(sum_by_types([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")