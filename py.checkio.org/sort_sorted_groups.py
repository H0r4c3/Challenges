'https://py.checkio.org/en/mission/sort-sorted-groups/share/7aedd8d424baa5b208998719df2419c9/'

'''
You are given a list of integers. Your goal is to find all sorted groups (group of numbers with distinct sorting order or single value) 
inside the list, sort input list by these groups and return this sorted list with groups unpacked.

For example, [5, 1, 5, 0, 5] --> [[5, 1], [5, 0], [5]] --> [[5], [5, 0], [5, 1]] --> [5, 5, 0, 5, 1].
'''

def find_the_etalon_order(items):
    '''find the etalon order'''
    etalon_order = ''
    
    for i in range((len(items) - 1)):
        if items[i] < items[i+1]:
            etalon_order = 'asc'
            break
        elif items[i] > items[i+1]:
            etalon_order = 'desc'
            break
        else:
            etalon_order = 'flat'
    
    print(f'etalon_order = {etalon_order}')
    return etalon_order


def find_the_first_change_order(items):
    '''compare the order with the etalon order'''
    etalon_order = find_the_etalon_order(items)
    
    for i in range((len(items) - 1)):
        if items[i] < items[i+1]:
            order = 'asc'
            if order != etalon_order:
                change_order = 'desc'
                idx = i+1
                etalon_order = 'desc'
                print(change_order, idx)
                return change_order, idx
        elif items[i] > items[i+1]:
            order = 'desc'
            if order != etalon_order:
                change_order = 'asc'
                idx = i+1
                etalon_order = 'asc'
                print(change_order, idx)
                return change_order, idx
        else:
            print(f'Flat! Compare with next char...')
    
    return 'equal', len(items)


def create_list_of_lists(items):
    print(f'items = {items}')
    global list_of_lists
    
    etalon_order, idx = find_the_first_change_order(items)
    
    print(f'idx = {idx}')
    
    if etalon_order == 'equal':
        list_of_lists.append(items)
        return list_of_lists
    
    # slice the list using the index of the change_order
    new_items = items[:idx] 
    print(f'new_items = {new_items}')
    list_of_lists.append(new_items) # [items[0:2], items[2:4], items[4:]]
    print(f'list_of_lists = {list_of_lists}')
    
    rest_items = items[idx:]
    print(f'rest_items = {rest_items}')
    
    if len(rest_items) == 1:
        list_of_lists.append(list(rest_items))
        return list_of_lists
        
    list_of_lists = create_list_of_lists(rest_items)
    print(f'final_list_of_lists = {list_of_lists}')
    
    return list_of_lists

def sorted_groups(items: list[int]) -> list[int]:
    global list_of_lists
    list_of_lists = list()
    
    list_of_lists = create_list_of_lists(items)
    
    # sort the list
    result_list = sorted(list_of_lists)
    print(f'sorted list = {result_list}')
    
    # flatten the list
    result_list = [item for sublist in result_list for item in sublist]
    print(f'result_list = {result_list}')
    
    return result_list


# BEST Solution: 
# https://py.checkio.org/mission/sort-sorted-groups/publications/veky/python-3/sum-sorted-groups/?ordering=most_voted&filtering=all

def groups(list):
    output, old_ordering, old_element = [], 0, None
    for element in list:
        if old_element is None: ordering = 0
        elif old_element < element: ordering = 1
        elif old_element > element: ordering = -1
        if old_ordering * ordering < 0:
            yield output
            output, ordering = [], 0
        output.append(element)
        old_ordering, old_element = ordering, element
    yield output
    

sorted_groups = lambda input: sum(sorted(groups(input)), [])


print("Example:")
#print(sorted_groups([5, 1, 5, 0, 5]))

assert sorted_groups([]) == []
assert sorted_groups([5]) == [5]

assert sorted_groups([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 4, 3, 2, 1, 0] 
# [[0,1,2,3,4,5], [4,3,2,1,0], [1,2,3,4]] # slice [[0:6], [6:11], [11:-1]]

assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1] # [5, 1, 5, 0, 5] --> [[5, 1], [5, 0], [5]] --> [[5], [5, 0], [5, 1]] --> [5, 5, 0, 5, 1]
# slice [[0:2], [2:4], [4:]]
# [0, 1, 2, 3]
assert sorted_groups([5, 5, 1]) == [5, 5, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")