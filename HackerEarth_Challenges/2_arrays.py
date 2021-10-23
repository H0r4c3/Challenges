'https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/2-arrays-90c9019c/'

'''
ou are given  arrays  and , each of the size . Each element of these arrays is either a positive integer or . The total number of  that can appear over these  arrays are  and .

Now, you need to find the number of ways in which we can replace each  with a non-negative integer, such that the sum of both of these arrays is equal.
'''

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

def replacements(A, B):
    if A.count(-1) == B.count(-1):
        return 'Infinite'
    elif A.count(-1) == 1 and B.count(-1) == 0:
        if sum(A) + 1 > sum(B):
            return 0
        else:
            return 1
    elif A.count(-1) == 0 and B.count(-1) == 1:
        if sum(A) < sum(B) + 1:
            return 0
        else:
            return 1
    elif A.count(-1) == 2:
        if sum(A) + 2 > sum(B):
            return 0
        else:
            return sum(B) - sum(A)-1
    elif B.count(-1) == 2:
        if sum(A) < sum(B) + 2:
            return 0
        else:
            return sum(A) - sum(B)-1



A = [1, 2, -1, 4]
B = [3, 3, 3, 1]

A = [1, 2, 3, -1, -1]
B = [10, 11, 12, 13, 14]

result = replacements(A, B)
print(result)