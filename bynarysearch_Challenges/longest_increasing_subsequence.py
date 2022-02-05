'https://binarysearch.com/problems/Longest-Increasing-Subsequence'

'''
Given an unsorted list of integers nums, return the longest strictly increasing subsequence of the array.

Bonus: Can you solve it in \mathcal{O}(n \log n)O(nlogn) time?
'''


# https://helloacm.com/teaching-kids-programming-greedy-algorithm-to-find-longest-increasing-subsequence-in-onlogn-via-binary-search/

import bisect
class Solution:
    def solve(self, nums):
        lis = []
        for n in nums:
            i = bisect.bisect_left(lis, n)
            if i == len(lis):
                lis.append(n)
            else:
                lis[i] = n
        return len(lis)
    
obj1 = Solution()
print(obj1.solve([10,9,2,5,3,7,101,18]))