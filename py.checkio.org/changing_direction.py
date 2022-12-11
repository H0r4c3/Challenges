'https://py.checkio.org/en/mission/changing-direction/'

'''
You are given a list of integers. Your task in this mission is to find, how many times the sorting direction was changed in the given list. 
If the elements are equal - the previous sorting direction remains the same, 
if the sequence starts from the same elements - look for the next different to determine the sorting direction.
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
            order = ''
            order_list.append(order)
    
    order_list = [item for item in order_list if item != '']        
    print(order_list)
    return(order_list)

def changing_direction_(elements: list[int]) -> int:
    result = 0
    
    order_list = decide_order(elements)
    
    for i in range((len(order_list) - 1)):
        if order_list[i] != order_list[i+1]:
            result += 1
        
    print(result)
    return result


# Best Solution:
# https://py.checkio.org/mission/changing-direction/publications/book1978/python-3/second/?ordering=most_voted&filtering=all

def changing_direction(e: list) -> int:
    print(e)
    
    d = [x - y for x, y in zip(e, e[1:]) if x != y]
    print(d)
    
    result = sum(x * y < 0 for x, y in zip(d, d[1:]))
    print(result)
    
    return result



# Best Solution:
# https://py.checkio.org/mission/changing-direction/publications/juestr/python-3/double-updown/?ordering=most_voted&filtering=all

def changing_direction_(elements: list) -> int:
    cmp = lambda a, b: (a > b) - (a < b) 
    updown = lambda xs: list(filter(None, map(cmp, xs, xs[1:])))
    return len(updown(updown(elements)))


print("Example:")
#print(changing_direction([1, 2, 3, 4, 5]))

#assert changing_direction([1, 2, 3, 4, 5]) == 0
#assert changing_direction([1, 2, 3, 2, 1]) == 1
#assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
assert changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")