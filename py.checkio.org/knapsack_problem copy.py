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

# MY SOLUTION is not optimized for a situation!!!!! (when the knapsack is not full at final!!!)

import logging

log_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\py.checkio.org\knapsack_problem.log'

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=log_path, 
                    filemode='w')

logger = logging.getLogger('main')

def knapsack(weight: int, items: list[tuple[int, int] | tuple[int, int, int]]) -> int:
    # sort the 'items' list after report value / weight
    print(items)
    logging.info(f'START')
    logging.info(f'items = {items}')
    items_sort = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    print(items_sort)
    logging.info(f'items_sort = {items_sort}')
    
    value = 0
    
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
            
            if nr > item[2]:
                logging.info(f'But we do NOT have {nr} of this item')
                logging.debug(f'The amount of this item = {item[2]} is smaller than we could use = {nr}')
                value = value + item[0] * item[2]
                logging.debug(f'Sum value = {value}')
                weight = weight - item[1] * item[2]
                logging.debug(f'Rest weight = {weight}')
                if weight == 0:
                    print(value)
                    logging.debug(f'Final value = {value}')
                    return value
            else:
                logging.info(f'We have more or exact nr. of pieces ({item[2]}) of this item: {item} than we can use ({nr}) ')
                #nr = weight // item[1]
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
            
    # if the knapsack is not full, we must rearrange the items
    if weight != 0:
        # modify the quantity of some item
        pass
                
    print(value)
    logging.debug(f'Final value = {value}')       
    return value


print("Example:")
#print(knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]))

# These "asserts" are used for self-checking
assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
assert knapsack(8, [(10, 10, 3)]) == 0
assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12
assert knapsack(15, [(7, 4, 1), (8, 5, 1), (6, 3, 1), (9, 6, 1)]) == 24
assert knapsack(20, [(10, 5, 1), (15, 8, 1), (7, 4, 1), (12, 6, 1), (4, 2, 1)]) == 38
assert knapsack(40, [(10, 5, 3), (15, 8, 2), (7, 4, 1), (12, 6, 2), (4, 2, 4)]) == 78
assert knapsack(50, [(20, 10, 1), (15, 8, 2), (18, 12), (10, 5, 1), (8, 4), (5, 3, 4)]) == 100

print("The mission is done! Click 'Check Solution' to earn rewards!")