'https://www.hackerearth.com/problem/algorithm/maximize-sum-0423b95e/?source=list_view'

'''
You are given an array  of  integers. You want to choose some integers from the array subject to the condition that the number of distinct integers 
chosen should not exceed . 
Your task is to maximize the sum of chosen numbers.

In the second test case, we have K = 2, A = [2, 1, 2, 5] . We need to choose atmost 2 distinct integers, we choose 2 + 2 + 5. 
Note that the condition is choosing atmost  distinct integers. 
So we can choose repeated number as many times as we want. The sum is  and we output it.
'''

from collections import Counter
from itertools import combinations

import logging

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\HackerEarth_Challenges\maximize_the_sum.log'

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

logger = logging.getLogger('main')


# T = int(input())
# N = [None]*T
# K = [None]*T
# A = [None]*T
 
# for i in range(T):
#     NK = str(input())
#     NK_list = NK.split()
#     N[i] = int(NK_list[0])
#     K[i] = int(NK_list[1])
#     A[i] = list(map(int, input().split()))


N = 4
K = 2
K = 4
A = [2, 1, 2, 5]
A = [-3, 3, -8, 8, 3, -3, 7, -4]

def max_sum(K, A):
    A = [item for item in A if item>0]

    if K == 0:
        return 0
    if K == 1:
        return max(A)
    
    count = Counter(A)
    logging.debug(f'count = {count}')
    
    A_set = set(A)
    logging.debug(f'A_set = {A_set}')
    
    # if no repetitions in A
    if len(A) == len(A_set):
        logging.info(f'No repetitions')
        return sum((sorted(A, reverse=True))[0:K])
    
    # list of (number*repetitions)
    list_of_prod = [item*count[item] for item in A_set]
    logging.debug(f'list_of_prod = {list_of_prod}')
    logging.debug(f'sorted(list_of_prod, reverse=True) = {sorted(list_of_prod, reverse=True)}')
    logging.debug(f'(sorted(list_of_prod, reverse=True))[0:K] = {(sorted(list_of_prod, reverse=True))[0:K]}')
    logging.debug(f'sum = {sum((sorted(list_of_prod, reverse=True))[0:K])}')
    
    max_s = sum((sorted(list_of_prod, reverse=True))[0:K])
    
    return max_s
    

max_s = max_sum(K, A)
print(max_s)


# for i in range(T):
#     print(max_sum(K[i], A[i]))