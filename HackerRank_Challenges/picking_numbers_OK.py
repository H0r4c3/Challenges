'https://www.thepoorcoder.com/hackerrank-picking-numbers-solution/'

# 1. Method

a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
a1 = [4, 6, 5, 3, 3, 1]
a1 = [1, 2, 2, 3, 1, 2]
a1 = [3]
a1 = [1, 3, 5, 7]
a1 = [1, 2, 3, 4]
a = [4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]

from collections import Counter
def pickingNumbers(a):
    a = Counter(a)
    maxi = 0
    for k in sorted(a):
        m = a[k] + a.get(k+1, 0)
        if maxi < m:
            maxi = m
    return maxi

# input()
# a = map(int,input().split())
print(pickingNumbers(a))



# 2. Method

from collections import Counter
def pickingNumbers(a):
    a = Counter(a)
    return max(a[k] + a.get(k+1, 0) for k in sorted(a))

print(pickingNumbers(a))



