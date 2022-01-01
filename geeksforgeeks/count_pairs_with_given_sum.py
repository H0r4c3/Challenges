'https://practice.geeksforgeeks.org/contest/interview-series-jp-morgan-chase/problems/'

'''
Given an array of N integers K, find the number of pairs of elements in the array whose sum is equal to K.
'''

#User function Template for python3
from itertools import combinations
import numpy as np

class Solution1:
    def getPairsCount(self, arr, n, k):
        counter = 0
        arr.sort()
        comb = combinations(arr, 2)
        for item in comb:
            print(item)
            if item[0] + item[1] == k:
                counter += 1
        return counter
    

class Solution2:
    def getPairsCount(self, arr, n, k):
        counter = 0
        arr.sort()
        comb = combinations(arr, 2)
        for x, y in comb:
            print(x, y)
            if x + y == k:
                counter += 1
        return counter
    

from collections import Counter
class Solution:
    def getPairsCount(self, arr, n, k):
        already_seen = Counter()
        pairs = []
        for x in arr:
            for _ in range(already_seen[k - x]):
                pairs.append((x, k - x))
            already_seen[x] += 1
        return len(pairs)

    
    
my_obj = Solution()

arr = [1, 2, 3, 4, 5, 3]
n = len(arr)
k = 6
result = my_obj.getPairsCount(arr, n, k)
print(result) # -> 3