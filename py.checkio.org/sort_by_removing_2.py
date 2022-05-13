'https://py.checkio.org/en/mission/sort-by-removing/'

'''
Your goal is to create the fastest sorting algorithm ever - Sort By Removing.

You just need to remove all elements from a given array that are in the incorrect order. As always, we have some conditions:

it's an asc sorting;
the first element should always stay in the result list;
the result of an empty list is an empty list;
the elements are always integers.
'''

def sort_by_removing(values: list) -> list:
    if values:
        new_values = [values[0]]
    else:
        return []
        
    for item in values[1:]:
        if item >= new_values[-1]:
            new_values.append(item)
    
    print(new_values)      
    return new_values

        


if __name__ == '__main__':
    print("Example:")
    #print(sort_by_removing([3, 5, 2, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_removing([3, 5, 2, 6]) == [3, 5, 6]
    assert sort_by_removing([7, 6, 5, 4, 3, 2, 1]) == [7]
    assert sort_by_removing([3, 3, 3, 3]) == [3, 3, 3, 3]
    assert sort_by_removing([5, 6, 7, 0, 7, 0, 10]) == [5, 6, 7, 7, 10]
    assert sort_by_removing([1, 5, 2, 3, 4, 7, 8]) == [1, 5, 7, 8]
    assert sort_by_removing([1, 7, 2, 3, 4, 5]) == [1, 7]
    assert sort_by_removing([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")