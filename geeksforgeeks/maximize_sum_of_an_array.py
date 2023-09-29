'https://practice.geeksforgeeks.org/problems/maximize-arrii-of-an-array0026/1'

'''
Given an array A of N integers. Your task is to write a program to find the maximum value of ∑arr[i]*i, where i = 0, 1, 2,., n 1.
You are allowed to rearrange the elements of the array.
Note: Since output could be large, hence module 109+7 and then print answer.
'''

class Solution:
    def Maximize(self, a, n):
        s = sorted(a)
        result = sum([i*c for i, c in enumerate(s)])
        return result % (10**9 + 7)
    
my_obj = Solution()

assert my_obj.Maximize([5, 3, 2, 4, 1], 5) == 40
print('Done!!!')