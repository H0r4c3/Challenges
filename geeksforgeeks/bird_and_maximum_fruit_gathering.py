'https://practice.geeksforgeeks.org/problems/bird-and-maximum-fruit-gathering0509/1'

'''
There are N trees in a circle. Each tree has a fruit value associated with it. 
A bird has to sit on a tree for 0.5 sec to gather all the fruits present on the tree and then the bird can move to a neighboring tree. 
It takes the bird 0.5 seconds to move from one tree to another. 
Once all the fruits are picked from a particular tree, she can’t pick any more fruits from that tree. The maximum number of fruits she can gather is infinite.
'''

def maxFruits(arr,n,m):
        maxSoFar = 0
        if m >= n:
            return sum(arr)
            
        for i in range(m):
            maxSoFar += arr[i]
            
        maxSum = maxSoFar
        j = 0
        for i in range(m, n + m):
            maxSoFar = maxSoFar - arr[j] + arr[i%n]
            
            if maxSoFar > maxSum:
                maxSum = maxSoFar
                
            j += 1
                
        return maxSum
    
'''
Input:
N=7 M=3
arr[] = { 2 ,1 ,3 ,5 ,0 ,1 ,4 }
Output: 9
Explanation: 
She can start from tree 1 and move
to tree2 and then to tree 3.
Hence, total number of gathered fruits
= 1 + 3 + 5 = 9.
'''

