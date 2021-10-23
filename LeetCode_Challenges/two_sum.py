'https://leetcode.com/problems/two-sum/'

from typing import List

# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6



#class Solution:
    # def __init__(self, nums, target):
    #     self.nums = nums
    #     self.target = target
    
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     self.nums = nums
    #     self.target = target
    #     #result = [(x, y) for x in self.nums for y in self.nums if (x!=y and x+y==self.target)]
    #     result = [[x,y] for x in range(len(self.nums)) for y in range(len(self.nums)) if (nums[x] + nums[y] == self.target and x!=y)]
    #     return result
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = []
        self.nums = nums
        self.target = target
        i=0
        for x in range(i, len(self.nums)):
            for y in range(i+1, len(self.nums)):
                if (nums[x] + nums[y] == self.target and x!=y):
                    my_list.append(x)
                    my_list.append(y)
                    break
                
            i = i + 1

        return my_list

my_obj = Solution()
print(str(my_obj.twoSum(nums, target)).replace(" ", ""))