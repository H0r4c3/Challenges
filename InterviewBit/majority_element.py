'https://www.interviewbit.com/problems/majority-element/'

'''
Problem Description

Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
'''

from collections import Counter

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n = len(A)
        char_counts = Counter(A)
        my_list = char_counts.most_common()
        #print(my_list)
        result = [item[0] for item in my_list if item[1] > n/2]
        for items in result:
            return items
        
my_obj = Solution()
A = [2, 1, 2]
result = my_obj.majorityElement(A)
print(result)