'https://binarysearch.com/problems/Count-Next-Element'

'''
Given a list of integers nums, return the number of elements x there are such that x + 1 exists as well.
'''
from collections import Counter

class Solution:
    
    def solve1(self, nums):
        nums = sorted(nums)
        counter = 0
        for item in nums:
            if (item+1) in nums:
                counter = counter + 1
        return counter
    
    def solve2(self, nums):
        nr_counts = Counter(nums)
        nums_set = set(nums)
        counter = 0
        for item in nums_set:
            if (item+1) in nums_set:
                counter = counter + nr_counts[item]
        return counter

nums = [3, 1, 2, 2, 7]

my_obj = Solution()
result = my_obj.solve2(nums)
print(result)