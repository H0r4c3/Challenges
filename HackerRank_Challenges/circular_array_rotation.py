'https://www.hackerrank.com/challenges/circular-array-rotation/problem'

'''
John Watson knows of an operation called a right circular rotation on an array of integers. 
One rotation operation moves the last array element to the first position and shifts all remaining elements right one. 
To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a 
number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the values of the elements at the given indices.
'''

def circularArrayRotation(a, k, queries):
    res = list()
    le = len(a)
    k = k%le
    a2 = a[le-k:] + a[:le-k]
    print(a2)
    for item in queries:
        res.append(a2[item])
        
    return res

a = [3, 4, 5]
k = 2
queries = [1, 2]

result = circularArrayRotation(a, k, queries)
print('\n'.join(map(str, result)))