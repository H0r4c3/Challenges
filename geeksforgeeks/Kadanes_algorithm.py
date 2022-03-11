'https://practice.geeksforgeeks.org/contest/interview-series-facebook-0641/problems/#'
'https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1'

'''
Kadane's Algorithm
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

Function to find the sum of contiguous subarray with maximum sum.
'''

# Solution: 
# https://towardsdatascience.com/maximum-subarray-problem-and-kadanes-algorithm-4cb1ce91be72

#Function to find the sum of contiguous subarray with maximum sum.
def maxSubArraySum(arr, N):
    for i in range(1, N):
        if arr[i-1] > 0:
            arr[i] += arr[i-1]
    return max(arr)

if __name__ == "__main__":
    
    a = [1, 3, 8, -2, 6, -8, 5]
    print(maxSubArraySum(a, len(a)))
    
    
'''
Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
'''


# Best Solution: https://www.interviewbit.com/blog/maximum-subarray-sum/

def maximumSubarraySum(arr):
       n = len(arr)
       maxSum = -1e8
       currSum = 0

       for i in range(0, n):
           currSum = currSum + arr[i]
           if currSum > maxSum:
               maxSum = currSum
           if currSum < 0:
               currSum = 0
      
       return maxSum

if __name__ == "__main__":
    # Your code goes here
    print(maximumSubarraySum([1, 3, 8, -2, 6, -8, 5]))
    
    
    
# https://www.alphacodingskills.com/algo/kadane-algorithm.php
# function for kadane's algorithm
def kadane(MyList):
  max_sum = 0
  current_sum = 0
  for i in MyList: 
    current_sum = current_sum + i
    if current_sum < 0:
      current_sum = 0
    if max_sum < current_sum:
      max_sum = current_sum
  return max_sum
  
# test the code                 
MyList = [-3, 1, -8, 12, 0, -3, 5, -9, 4]
print("Maximum SubArray is:",kadane(MyList))