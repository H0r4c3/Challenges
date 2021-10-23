'https://www.hackerearth.com/challenges/competitive/python-interview-prep/problems/f40faffcf0f6441199806c08670d90ef/'

'https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/little-jhool-and-too-many-products-cd26d94a/?utm_source=header&utm_medium=search&utm_campaign=he-search'

'Test nr. 2 - Pyton (Easy)'

'''
You are given two numbers: A and S
Write a program to determine the number of ways in which the numbers that are greater than and
equal to S can be added to get the sum A.
Input:
First line: T denoting the number of test cases
For each test case:
    First line: Two space-separated integers A and S
'''

# T = int(input())
# A = [None]*10
# S = [None]*10

# for i in range(T):
#     nrs = input()
#     nrs_list = nrs.split()
#     A[i] = int(nrs_list[0])
#     S[i] = int(nrs_list[1])


def count_perm(n, s):
    sol = [0]*(n+1)
    sol[0] = 1

    for i in range(s, n):
        for j in range(i, n+1):
            sol[j] += sol[j-i]
    
    return sol[n]

# for i in range(T):
#     print(count_perm(A[i], S[i]))

A = 2
S = 1
result = count_perm(A, S)
print(result)