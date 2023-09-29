''

'''
Find the maximum sum of elements possible of array B, after performing such operations.
'''

class Solution:
    def maximumSum(self, n, A):
        C = sorted(A)
        B = [(i+1)*c for i, c in enumerate(C)]
        return sum(B)
    
my_obj = Solution()

assert my_obj.maximumSum(2, [2, 1]) == 5
print('Done!!!')