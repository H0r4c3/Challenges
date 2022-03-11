'https://blog.finxter.com/google-interview-the-3-sum-problem/?tl_inbound=1&tl_target_all=1&tl_form_type=1&tl_period_type=3&utm_source=newsletter&utm_medium=email&utm_campaign=finxter_weekly_new_tutorials&utm_term=2021-10-28'

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Note: that the solution set must not contain duplicate triplets.
'''

'''
Example 1:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2],[-1, 0, 1]]
'''

# 1. Method = Naïve Approach: Brute Force Algorithm

'''
Approach: The simplest approach would be to use nested for loop. 
For this, we will traverse the array for each number. 
If we find the unique triplets that satisfy the conditions: nums[i] + nums[j] + nums[k] == 0, i != j, i != k, and j != k, 
then we can append the numbers into the list. Further, we will use the set to remove the duplicate triplets.

Complexity Analysis: In this method, we have considered every number three times by using nested for loops. 
This means we have to traverse the list thrice which accounts for the time complexity of O(n^3).
'''

def three_sum(nums):
    sets = []
    lst = []
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            for k in range(0, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j != k:
                    lst = sorted([nums[i], nums[j], nums[k]])
                    if lst not in sets:
                        sets.append(sorted([nums[i], nums[j], nums[k]]))
    return sets

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))



# 2. Method = Two Pointer Approach [An Efficient Solution]

'''
Approach: This approach is more efficient as compared to the brute force solution. 
The idea here is that, as you have to find unique triplets such that nums[i] + nums[j] + nums[k] == 0, re-arranging them would mean nums[j] + nums[k] = – nums[i]. 
We, will use this to our advantage and proceed with our algorithm such that: 

We first, sort the given list and then work upon the sorted list using two pointers that point at the start and end elements of the list. 
Here, we can have three conditions:

nums[j] + nums[k] > - nums[i]. In this case we have to shift the end pointer towards the left.
nums[j] + nums[k] < - nums[i]. In this case we have to shift the start pointer towards right.
nums[j] + nums[k] = - nums[i]. In this case we found a triplet. Hence, we store this value and move the pointer accordingly to search for more triplets if any.

Complexity Analysis: In this method, to get the value of nums[i] we use one loop that takes O(n) time. Further, 
inside that loop to get the value of sum nums[j] + nums[k] we used the two pointer approach that takes O(n) time. 
Hence, we have to undergo a nested loop which leads to a time complexity is O(n^2).


'''

def three_sum(nums):
    lst=[]
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
 
        j = i + 1
        k = len(nums) - 1
 
        test_sum  = 0 - nums[i]
 
        while j < k:
            sum = nums[j] + nums[k]
 
            if sum < test_sum:
                j += 1
            elif sum > test_sum:
                k -= 1
            else:
                lst.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
 
    return lst

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))