'https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-sum-4-f8d12458/'

'''
You are given an array of integers , you need to find the maximum sum that can be obtained by picking some non-empty subset of the array. 
If there are many such non-empty subsets, choose the one with the maximum number of elements. 
Print the maximum sum and the number of elements in the chosen subset.
'''

N = int(input())
A = input()

array=[int(x) for x in A.split()]

sum1=count=0

for i in array:
    if i>=0:
        count+=1
        sum1 += i

if count == 0:
    print(f'{max(array)} 1')
else:
    print(sum1,count)