'https://py.checkio.org/en/mission/knapsack-problem-2/share/9883dbd1752cd52cd44b2685a45c31ac/'

'''
This mission is dedicated to a famous and classical Knapsack Problem.

You are given a list of kinds of items that you want to put into knapsack. 
Item of each kind is a tuple of its value, weight and maximum amount (optional). 

You need to find a subset of items, such that:

- the total value of the items in subset is as large as possible;
- the total weight of items in subset is at most weight, that is capacity of the knapsack;
- for each kind of items you can select at most given amount items. If its not given - there is no restriction for amount.
'''

def knapsack(weight: int, items: list[tuple[int, int] | tuple[int, int, int]]) -> int:
    # sort the 'items' list after report value / weight
    items_sort = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    value = 0
    
    for item in items_sort:
        # If the amount its not given, add amount = infinite for this item.
        if len(item) == 2:
            item = item + (float('inf'),)
        
        if weight >= item[1]:
            nr = weight // item[1]
            if nr >= item[2]:
                value += item[0] * item[2]
                weight -= item[1] * item[2]
                if weight == 0:
                    return value
            else:
                nr = weight // item[1]
                value += item[0] * nr
                weight -= item[1] * nr
                if weight == 0:
                    return value    
    return value


print("Example:")
#print(knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]))

# These "asserts" are used for self-checking
assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
assert knapsack(8, [(10, 10, 3)]) == 0
assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12

print("The mission is done! Click 'Check Solution' to earn rewards!")