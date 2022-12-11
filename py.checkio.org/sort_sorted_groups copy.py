'https://py.checkio.org/en/mission/sort-sorted-groups/share/7aedd8d424baa5b208998719df2419c9/'

'''
You are given a list of integers. Your goal is to find all sorted groups (group of numbers with distinct sorting order or single value) 
inside the list, sort input list by these groups and return this sorted list with groups unpacked.

For example, [5, 1, 5, 0, 5] --> [[5, 1], [5, 0], [5]] --> [[5], [5, 0], [5, 1]] --> [5, 5, 0, 5, 1].
'''

def decide_order(elements: list[int]) -> list[str]:
    '''
    Create a list with changes in direction
    '''
    order_list = list()
    for i in range((len(elements) - 1)):
        if elements[i] < elements[i+1]:
            order = 'asc'
            order_list.append(order)
        elif elements[i] > elements[i+1]:
            order = 'desc'
            order_list.append(order)
        else:
            order_list.append(order)
            
    print(order_list)
    return(order_list)

def dict_order(elements: list[int]) -> list[str]:
    '''
    Create a dictionary with changes in direction having
    as keys the index where the changes happen
    '''
    change_order_dict = dict()
    etalon_order = list()
    
    # find the first order
    for i in range((len(elements) - 1)):
        if elements[i] < elements[i+1]:
            etalon_order = 'asc'
            break
        elif elements[i] > elements[i+1]:
            etalon_order = 'desc'
            break
        else:
            etalon_order = 'flat'
    
    print(f'etalon_order = {etalon_order}')
    
    change_order_dict[0] = etalon_order
        
    # compare the order with the etalon order
    for i in range((len(elements) - 1)):
        if elements[i] < elements[i+1]:
            order = 'asc'
            if order != etalon_order:
                change_order_dict[i+1] = order
            etalon_order = 'asc'
        elif elements[i] > elements[i+1]:
            order = 'desc'
            if order != etalon_order:
                change_order_dict[i+1] = order
            etalon_order = 'desc'
        else:
            print(f'Flat! Compare with next char...')
    
    print(change_order_dict)
    return(change_order_dict)


def sorted_groups_(items: list[int]) -> list[int]:
    print(items)
    change_order_dict = dict_order(items)
    print(change_order_dict)
    
    idx = list(change_order_dict.keys())
    print(idx)
    
    # slice the list using the keys from change_order_dict and add the pieces to result list
    result_list = [items[idx[i] : idx[i+1]] for i in range(len(idx) - 1)] # [items[0:2], items[2:4], items[4:]]
    result_list.append(items[idx[-1] : ])
    
    # sort the list
    result_list = sorted(result_list)
    print(result_list)
    
    # flatten the list
    result_list = [item for sublist in result_list for item in sublist]
    print(result_list)
    
    return result_list

def find_the_etalon_order(items):
    '''find the first change order'''
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
    
    return 'equal', 0

def create_list_of_lists(items):
    list_of_lists = list()
    print(items)
    
    etalon_order, idx = find_the_first_change_order(items)
    
    if etalon_order == 'equal':
        return items
    
    # slice the list using the index of the change_order
    new_items = items[:idx] 
    list_of_lists.append(new_items) # [items[0:2], items[2:4], items[4:]]
    
    rest_items = items[idx:]
    list_of_lists = create_list_of_lists(rest_items)
    print(list_of_lists)
    
    return list_of_lists

def sorted_groups(items: list[int]) -> list[int]:
    
    list_of_lists = create_list_of_lists(items)
    
    # sort the list
    result_list = sorted(list_of_lists)
    print(result_list)
    
    # flatten the list
    result_list = [item for sublist in result_list for item in sublist]
    print(result_list)
    
    return result_list


print("Example:")
#print(sorted_groups([5, 1, 5, 0, 5]))

#assert sorted_groups([]) == []
#assert sorted_groups([5]) == [5]

#assert sorted_groups([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 4, 3, 2, 1, 0] 
# [[1,2,3,4,5], [4,3,2,1], [2,3,4]] # slice [[0:6], [6:11], [11:-1]]

assert sorted_groups([5, 1, 5, 0, 5]) == [5, 5, 0, 5, 1] # [5, 1, 5, 0, 5] --> [[5, 1], [5, 0], [5]] --> [[5], [5, 0], [5, 1]] --> [5, 5, 0, 5, 1]
# slice [[0:2], [2:4], [4:]]
# [0, 1, 2, 3]
assert sorted_groups([5, 5, 1]) == [5, 5, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")