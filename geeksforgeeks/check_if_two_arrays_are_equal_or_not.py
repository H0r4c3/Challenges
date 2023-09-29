'https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?page=1&curated[]=1&sortBy=submissions'

'''
Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. 
Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
'''

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self, A, B):
        
        A, B = sorted(A), sorted(B)
        z = zip(A, B)
        #print(list(z))
        
        for item in z:
            if item[0] - item[1] != 0:
                return False
        
        return True
    

my_object = Solution()

assert my_object.check([1,2,5,4,0], [2,4,5,0,1]) == 1
print('Done!!!')