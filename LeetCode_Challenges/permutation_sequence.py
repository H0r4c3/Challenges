'https://leetcode.com/problems/permutation-sequence/'

'''
Given n and k, return the kth permutation sequence of [0, 1, ..., n].
'''

import math
def getPermutation(n, k):
    numbers = list(range(1, n+1))
    permutation = ''
    k -= 1
    while n > 0:
        n -= 1
        # get the index of current digit
        index, k = divmod(k, math.factorial(n))
        permutation += str(numbers[index])
        # remove handled number
        numbers.remove(numbers[index])

    return permutation
    
    
result = getPermutation(3, 5)
print(result)