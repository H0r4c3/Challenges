'https://www.hackerrank.com/challenges/array-left-rotation/problem'

'''
A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. Given an integer, , rotate the array that many steps left and return the result.
'''

def rotateLeft(d, arr):
    n = len(arr)
    q = d % n
    
    arr_new = arr[q-n : ] + arr[ : q-n]
    
    return arr_new

arr = [1, 2, 3, 4, 5]
d = 4
n = len(arr)

result = rotateLeft(d, arr)
print(result)