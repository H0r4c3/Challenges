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

# MY SOLUTION is not optimized for the situation when the knapsack is not full at final!!!)

import logging

log_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\py.checkio.org\knapsack_problem.log'

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=log_path, 
                    filemode='w')

logger = logging.getLogger('main')

def knapsack(weight: int, items: list[tuple[int, int] | tuple[int, int, int]]) -> int:
    # sort the 'items' list after report value / weight, and, for same value, after quantity infinite
    print(items)
    logging.info(f'START')
    logging.info(f'items = {items}')
    items_sort = sorted(items, key=lambda x: (x[0]/x[1]), reverse=True)
    print(items_sort)
    logging.info(f'items_sort = {items_sort}')
    
    value = 0
    used_items, not_used_items = list(), list()
    
    for item in items_sort:
        # If the amount its not given, add amount = infinite for this item.
        if len(item) == 2:
            item = item + (float('inf'),)
        
        logging.info(f'Next item = (value, weight, amount) = {item}')
        logging.info(f'The weight of the knapsack = {weight}')
        if weight >= item[1]:
            logging.info(f'The weight of the knapsack >= weight of the item -> {weight} >= {item[1]}')
            nr = weight // item[1]
            logging.info(f'We could put in the knapsack {nr} of this item')
            
            if nr >= item[2]:
                logging.info(f'We do NOT have more than {nr} of this item')
                logging.debug(f'The amount we can take of this item = {item[2]} is NOT bigger than we could use = {nr}')
                
                used_items.append(item)
                logging.debug(f'used_items = {used_items}')
                
                value = value + item[0] * item[2]
                logging.debug(f'Sum value = {value}')
                weight = weight - item[1] * item[2]
                logging.debug(f'Rest weight = {weight}')
                if weight == 0:
                    print(value)
                    logging.debug(f'Final value = {value}')
                    return value
            else:
                logging.info(f'We have more nr. of pieces ({item[2]}) of this item: {item} than we can use ({nr}) ')
                item_l = list(item)
                used = nr
                rest = item[2] - nr
                item_l[2] = used
                used_items.append(item_l)
                item_l[2] = rest
                if rest > 0:
                    not_used_items.append(item_l)
                
                logging.debug(f'used_items = {used_items}')
                logging.debug(f'not_used_items = {not_used_items}')
                
                value = value + item[0] * nr
                logging.debug(f'Sum value = {value}')
                weight = weight - item[1] * nr
                logging.debug(f'Rest weight (should be 0) = {weight}')
                if weight == 0:
                    print(value)
                    logging.debug(f'Final value = {value}')
                    return value
        else:
            logging.info(f'The weight of the knapsack < weight of the item -> {weight} < {item[1]}')
            not_used_items.append(item)
            logging.debug(f'not_used_items = {not_used_items}')
            
    # if the knapsack is not full, we must modify the items to put in knapsack
    if weight != 0:
        logging.info(f'The knapsack is not full, remaining space = {weight}')
        # modify the quantity of some item
        
        # calculate the needed_weight for the first item in not_used_items
        logging.info(f'Calculate the needed_weight for the item {not_used_items[0]} from not_used_items')
        item_in = not_used_items[0]
        needed_weight = item_in[1] - weight
        logging.info(f'Must find an item with weight = {needed_weight} to be replaced from the knapsack')
        logging.info(f'Must search in used_items = {used_items}')
        
        # find the item to be replaced, starting with the last in used_items (must have the weight = needed_weight)
        for item_out in used_items[::-1]:
            if item_out[1] == needed_weight:
                logging.info(f'The item to be replaced from the knapsack = item_out = {item_out}')
                logging.info(f'The value to be replaced {item_out[0]} with the new value {item_in[0]}')
                value = value - item_out[0] + item_in[0]
                logging.debug(f'Final used_items - before modification = {used_items}')
                logging.debug(f'Final not_used_items - before modification = {not_used_items}')
                return value
            else:
                logging.info(f'The item {item_out} is not eligible for replacing (must have weight = {needed_weight}) in not_used_items')
                logging.debug(f'Final used_items = {used_items}')
                logging.debug(f'Final not_used_items = {not_used_items}')
    
    value = value + weight                   
    print(value)
    logging.debug(f'Final value = {value}')       
    return value



# BEST Solution: https://py.checkio.org/mission/knapsack-problem-2/publications/kdim/python-3/recursion/?ordering=most_voted&filtering=all
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

from functools import lru_cache
def knapsack_(weight: int, items: list[tuple[int, int] | tuple[int, int, int]]) -> int:
    items = [[v, w] for v, w, *n in items for _ in range(n.pop() if n else weight // w)]

    @lru_cache()
    def knp(w, n):
        if w == 0 or n < 0:
            return 0
        if items[n][1] > w:
            return knp(w, n - 1)
        else:
            return max(items[n][0] + knp(w - items[n][1], n - 1), knp(w, n - 1))

    return knp(weight, len(items) - 1)


print("Example:")
#print(knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]))

# These "asserts" are used for self-checking
#assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
#assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
#assert knapsack(8, [(10, 10, 3)]) == 0
#assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12
#assert knapsack(15, [(7, 4, 1), (8, 5, 1), (6, 3, 1), (9, 6, 1)]) == 24
#assert knapsack(20, [(10, 5, 1), (15, 8, 1), (7, 4, 1), (12, 6, 1), (4, 2, 1)]) == 38
#assert knapsack(40, [(10, 5, 3), (15, 8, 2), (7, 4, 1), (12, 6, 2), (4, 2, 4)]) == 78
assert knapsack(50, [(20, 10, 1), (15, 8, 2), (18, 12), (10, 5, 1), (8, 4), (5, 3, 4)]) == 100

print("The mission is done! Click 'Check Solution' to earn rewards!")