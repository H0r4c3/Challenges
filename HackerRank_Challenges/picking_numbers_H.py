'https://www.hackerrank.com/challenges/picking-numbers/problem'

import logging
from itertools import combinations

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\HackerRank_Challenges\picking_numbers_H.log'
  
#Create and configure logger

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

logger = logging.getLogger('main')


def pickingNumbers(a):
    if len(a) == 1:
        return 1
    
    # list with all combinations
    all_comb = [list(item) for i in range(1, len(a)+1) for item in combinations(a, i)]
    logger.debug(f'all_comb = {all_comb}')
    
    # eliminate the items with length = 1
    all_comb = [item for item in all_comb if len(item) != 1]
    print(all_comb)
    
    all_comb_ok = [None]*n
    
    for item in all_comb:
        c = 1
        logger.debug(f'item for verify = {item}')
        print(item)
        for i in range(0, len(item)-1):
            if abs(item[i] - item[i+1]) > 1:
                break
            else:
                c = c + 1
            if c == len(item):
                all_comb_ok.append(item)
            
    logger.debug(f'all_comb_ok = {all_comb_ok}')
    print(all_comb_ok)
    
    all_comb_ok_len = [len(item) for item in all_comb_ok if item != None]
    logger.debug(f'all_comb_ok_len = {all_comb_ok_len}')
    print(all_comb_ok_len)
    
    return max(all_comb_ok_len)
                

a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
a1 = [4, 6, 5, 3, 3, 1]
a1 = [1, 2, 2, 3, 1, 2]
a1 = [3]
a1 = [1, 3, 5, 7]
a1 = [1, 2, 3, 4]
a = [4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]

n = len(a)

max_len = pickingNumbers(a)
print(max_len)