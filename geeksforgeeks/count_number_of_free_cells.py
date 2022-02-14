'https://practice.geeksforgeeks.org/contest/interview-series-intuit-1134/problems/'

import numpy as np

def countZero(n, k):
        my_arr = np.zeros((n, n))
        return(my_arr)

n = 3                        
my_arr = countZero(n, 1)
print(my_arr)

for i in range(n):
    my_arr[i][0] = 1
    my_arr[0][i] = 1
    
print(my_arr)

count = np.count_nonzero(my_arr == 0)
print(count)