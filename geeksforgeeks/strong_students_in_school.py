'https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-102/problems/'

'''
Input: 
N = 5, M = 4
A = {1 2 3 4 5}

Output:
4

Explanation:
The maximum four elements are 2,3,4 and 5. 
The minimum four elements are 1,2,3 and 4. 
The difference between two sums is 
(2 + 3 + 4 + 5) - (1 + 2 + 3 + 4) = 4.
'''

def diffSum(n, m, arr):
    arr1 = sorted(arr, reverse = True)
    arr2 = sorted(arr)
    max_m = sum(arr1[ : m])
    min_m = sum(arr2[ : m])
    result = max_m - min_m
    return result
    
n = 5
m = 4   
arr = [1, 2, 3, 4, 5]

result = diffSum(n, m, arr)
print(result) # 4