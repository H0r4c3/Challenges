'https://leetcode.com/problems/search-insert-position/'

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
    

nums = [1,3,5,6]
target = 5
        
my_obj = Solution()
result = my_obj.searchInsert(nums, target)
print(result)

