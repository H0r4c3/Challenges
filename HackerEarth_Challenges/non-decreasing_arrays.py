'https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/make-it-non-decreasing-7d3391fd/'

'''
You are given an array  consisting of  positive integers. Your task is to find an array  of length  satisfying the following conditions:

 for all 
, for all 
 is divisible by  for all 
 is minimum
You are given T test cases.
'''

def non_decreasing_array(A):
    N = len(A)
    B = [None]*N
    B[0] = A[0]
    for i in range(1, N):
        if A[i] > B[i-1]:
            B[i] = A[i]
        else:
            if B[i-1] % A[i] == 0:
                B[i] = B[i-1]
            else:
                B[i] = (B[i-1]//A[i] + 1) * A[i]
     
    result = B
    
    return result

A = [2, 1, 3] 
A = [7, 5, 7]
result = non_decreasing_array(A) # ->   2 2 3
print(*result)


# if __name__ == '__main__':
#     T = int(input().strip()) # nr. of testcases

    # for _ in range(T):
    #     N = int(input())
    #     A = list(map(int, input().split())) # list of integers

    #     result = non_decreasing_array(A)
        
    #     print(result)
    