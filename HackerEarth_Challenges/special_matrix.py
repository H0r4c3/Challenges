'https://www.hackerearth.com/challenges/competitive/sept-circuits-21/algorithm/special-matrix-2-e2e9f0f4/'

import math

# Write your code here
T = int(input())
N = [None]*T
M = [None]*T

for i in range(T):
    dimensions = input()
    dimensions_list = dimensions.split()
    N[i] = int(dimensions_list[0])
    M[i] = int(dimensions_list[1])

def prime_factors(n):
    prime_fac = list()
    
    if n==0: return 0
    if n==1: return 1
    if n==2: return 1
    if n==3: return 1
    if n==4: return 1
    
    for i in range(2, n + 1):
        if n % i == 0:
            count = 1
            for j in range(2, (i//2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            if(count == 1):
                prime_fac.append(i)
    return prime_fac

def sum_elem(N, M):
    sum = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            sum = sum + len(prime_factors(i+j))
    return sum

for i in range(T):
    print(sum_elem(N[i], M[i]))