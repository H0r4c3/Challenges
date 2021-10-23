'https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/easy-sum-set-problem-7e6841ca/'

'''
In this problem, we define "set" is a collection of distinct numbers. 
For two sets  and , we define their sum set is a set . 
In other word,  set  contains all elements which can be represented as sum of an element in  and an element in . 
Given two sets, your task is to find set  of positive integers less than or equals  with maximum size such that . 
It is guaranteed that there is unique such set.
'''

# N = int(input()) # number of elements in set A
# A = set(map(int, input().split()))
# print(A)
# M = int(input()) # number of elements in set C
# C = set(map(int, input().split()))


def easy_sum(A, B, C):
    D = set()
    for item1 in A:
        for item2 in C:
            B.add(item2 - item1)
    for item1 in A:
        for item3 in B:
            if (item1 + item3) not in C:
                D.add(item3)
    B = B - D
    result = sorted(B)

    return result

A = {1, 2}
C = {3, 4, 5}
B = set()

result = easy_sum(A, B, C)
print(*result)