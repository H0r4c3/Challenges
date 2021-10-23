'https://www.hackerearth.com/practice/codemonk/'

'''
Monk and Rotation

Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the 
right direction by K steps and then print the resultant array.

Input:
The first line will consists of one integer T denoting the number of test cases.
For each test case:
1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements of the array A.
'''

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
https://github.com/parasjain-12/HackerEarth-Solution/blob/master/Monk%20and%20Rotation.py
'https://github.com/parasjain-12/HackerEarth-Solution'

SOLUTION:

testCase  = int(input())
for _ in range(testCase):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    x = k%n
    print(*(l[n-x:]+l[:n-x]))
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
'''

# T = int(input())



# for i in range(T):
#     A = [None]*T
#     K = [None]*T
#     B = [None]*T
#     NK = input().split()
#     K = int(NK[1])
#     A[i] = input().split()


def rotate_array2(A, K):
    N = len(A)
    B = [None]*N
    
    if K > N:
        K = K % N
    
    if K == N:
        return ' '.join(map(str, A))

    for i in range(N):
        if i+K < N:
            B[i+K] = A[i]
        elif i+K==0:
            B[i+K]=A[i]
        else:
            B[i+K-N] = A[i]
    
    result = ' '.join(map(str, B))
    
    return result


def rotate_array2(A, K):
    x = 0
    N = len(A)
    B = [None]*N
    A_int = list(map(int, A))
    
    x = K % N
    B = A_int[N-x : ] + A_int[ : N-x]
    #print(*B)
    
    return B


T = 1
#A = [12777, 16915, 7793, 18335, 5386, 492, 16649, 1421, 2362, 10027, 8690, 59, 17763, 13926, 540, 3426, 9172, 15736, 5211, 15368, 2567, 16429, 5782, 1530, 2862, 5123, 14067, 3135, 13929, 19802, 14022, 3058, 13069, 18167, 1393, 18456, 15011, 18042, 16229, 17373, 4421, 4919, 13784, 18537, 15198, 14324, 18315, 4370, 6413, 3526, 16091, 8980, 19956, 1873, 6862, 19170, 6996, 17281, 2305, 925, 17084, 16327, 336, 6505, 10846, 1729, 1313, 5857, 16124, 13895, 19582, 545, 18814, 13367, 15434, 10364, 4043, 13750, 11087, 6808, 17276, 7178, 15788, 13584]
#K = 86
A = [1, 2, 3, 4, 5]
K = 2


result = rotate_array2(A, K)
print(*result)

# for i in range(T):
#     print(NK[i])
#     print(K)
#     print(A[i])
#    print(rotate_array(A[i], K))


