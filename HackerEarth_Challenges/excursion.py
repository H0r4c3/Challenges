'https://www.hackerearth.com/challenges/competitive/data-structures-and-algorithms-coding-contest-November/algorithm/excursion-2d080f3a/'

'''
A group of students wants to visit a tour in some city . In total, the group has  boys and  girls. To do this, they need to stay in a hotel.

Calculate the number of rooms you need to book in the hotel, if each hotel room has  seats, provided that the boys can not live with the girls in the same room.

Input format

The first line specifies a number  denoting the number of test cases.
In each line of the test case, there are three numbers, .
Output format

For each test case, print one number denoting the number of rooms to be booked at the hotel.
'''

'https://www.hackerearth.com/challenges/competitive/data-structures-and-algorithms-coding-contest-November/problems/'


def excursion(N, M, K):
    result = 0
    if N % K != 0 and M % K != 0:
        r1 = 1
        r2 = 1
    elif N % K != 0 and M % K == 0:
        r1 = 1
        r2 = 0
    elif N % K == 0 and M % K != 0:
        r1 = 0
        r2 = 1
    elif N % K == 0 and M % K == 0:
        r1 = 0
        r2 = 0
        

    result = N // K + r1 + M // K + r2

    return result


if __name__ == '__main__':
    # T = int(input().strip()) # nr. of testcases

    # for _ in range(T):
    #     A = list(map(int, input().split())) # list of integers
    #     N = A[0]
    #     M = A[1]
    #     K = A[2]

    #     result = excursion(N, M, K)
        
    #     print(result)
    
    #A = '13 7 2'
    N = 13
    M = 7
    K = 2
    
    result = excursion(N, M, K)
    print(result)
    