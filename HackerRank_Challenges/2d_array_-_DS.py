'https://www.hackerrank.com/challenges/2d-array/problem'

'''
Given a  2D Array, :

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .
'''

def hourglassSum(arr):
    sums = list()
    
    # # row 0
    # # hourglass nr. 0 = column 0 (row 0)
    # sums[0] = sum(arr[0][0:3]) + sum(arr[1][1:2]) + sum(arr[2][0:3])
    
    # # hourglass nr. 1 = column 1 (row 0)
    # sums[1] = sum(arr[0][1:4]) + sum(arr[1][2:3]) + sum(arr[2][1:4])
    
    # # ...
    
    # # hourglass nr 4 = column i (row 0)
    # sums[4] = sum(arr[0][i:i+3]) + sum(arr[1][i+1:i+2]) + sum(arr[2][i:i+3])
    
    
    # # row 1
    # # hourglass nr. 5 = column 0 (row 1)
    # sums[5] = sum(arr[1][0:3]) + sum(arr[2][1:2]) + sum(arr[3][0:3])
    
    # # hourglass nr. 6 = column 1 (row 1)
    # sums[6] = sum(arr[1][1:4]) + sum(arr[2][2:3]) + sum(arr[3][1:4])
    
    # # ...
    
    # # hourglass nr. 8 = column i (row 1)
    # sums[8] = sum(arr[1][1:4]) + sum(arr[2][2:3]) + sum(arr[3][1:4])
    
    # # ...
    
    # # row j
    # # hourglass nr. 13 = column 0 (row j)
    # sums[13] = sum(arr[j][0:3]) + sum(arr[j+1][1:2]) + sum(arr[j+2][0:3])
    
    # # ...
    
    # # hourglass nr. 16 = column i (row j)
    # sums[16] = sum(arr[j][i:i+3]) + sum(arr[j+1][i+1:i+2]) + sum(arr[j+2][i:i+3])
    
    for j in range(4):
        for i in range(4):
            sums.append(sum(arr[j][i:i+3]) + sum(arr[j+1][i+1:i+2]) + sum(arr[j+2][i:i+3]))
    
    
    print(sums)
    
    result = max(sums)
    
    return result


arr = [[-9, -9, -9, 1, 1, 1], 
       [0, -9, 0, 4, 3, 2], 
       [-9, -9, -9, 1, 2, 3], 
       [0, 0, 8, 6, 6, 0], 
       [0, 0, 0, -2, 0, 0], 
       [0, 0, 1, 2, 4, 0]]

result = hourglassSum(arr)
print(result)