'https://www.hackerearth.com/challenges/competitive/december-circuits-21-2/problems/'

'https://www.hackerearth.com/challenges/competitive/december-circuits-21-2/algorithm/beautiful-numbers-4-20d7065b/'

'''
Any number is called beautiful if it consists of 2N digits and the sum of the first N digits is equal to the
sum of the last N digits. Your task is to find the count of beautiful numbers in the interval from L to R (including)
'''

def beautiful_numbers_H(A): # not always correct!!!
    A = list(map(int, A.split()))
    r = range(A[0], A[1]+1)
    result = 0
    for item in r:
        length = len(str(item))
        if length % 2 != 0:
            continue
        else:
            a = str(item)
            a1 = a[0 : length//2]
            a2 = a[length//2 : ]
            if sum(map(int, a1.split())) == sum(map(int, a2.split())):
                #print(item, sum(map(int, str(item)[0 : length//2].split())), sum(map(int, str(item)[length//2 : ].split())))
            #if sum(map(int, str(item)[0 : length//2].split())) == sum(map(int, str(item)[length//2 : ].split())):
                #print(a, a1, a2, '*** ', end='')
                result += 1

    return result

import numpy as np
def beautiful_numbers_(A): # time limit exceeded!!!!!!!
    A = list(map(int, A.split())) # list of integers
    
    r = range(A[0], A[1]+1)
    result = 0
    
    for item in r:
        sumfirst = 0
        sumsecond = 0
        s = str(item)
        length = len(s)
        
        if length % 2 != 0:
            continue
        else: 
            for i in range(length):
                
                # Add elements in first half sum
                if (i < length // 2):
                    sumfirst += int(s[i])
                # Add elements in the second half sum
                else:
                    sumsecond += int(s[i])
            
            if sumfirst == sumsecond:
                result += 1
        
    return result


import numpy as np
def split_interval(A):
    #A = list(map(int, A.split())) # list of integers
    
    #s = 10000 # superior limit
    s = A[-1]
    
    #n = 10 # number of parts

    #part = s // n # length of each part
    part = 1000
    #parts = []

    parts = [(i, i + part) for i in range(0, s, part)]
    return parts

    print(parts)
    
def check_sums(r):
    result = 0
    
    for item in r:
        sumfirst = 0
        sumsecond = 0
        s = str(item)
        length = len(s)
        
        if length % 2 != 0:
            continue
        else: 
            for i in range(length):
                
                # Add elements in first half sum
                if (i < length // 2):
                    sumfirst += int(s[i])
                # Add elements in the second half sum
                else:
                    sumsecond += int(s[i])
        
            if sumfirst == sumsecond:
                result += 1
                
        
    return result
    

def beautiful_numbers(A): # time limit exceeded!!!!!!!
    A = list(map(int, A.split())) # list of integers
    #parts = split_interval(A)
    parts = [(1, 99), (1000, 9999), (100000, 999999), (10000000, 99999999), 1000000000]
    # parts_NOK = [(100, 999), (10000, 99999), (1000000, 9999999), (100000000, 999999999)]
    r0 = range(parts[0][0], parts[0][1] + 1)
    r1 = range(parts[1][0], parts[1][1] + 1)
    r2 = range(parts[2][0], parts[2][1] + 1)
    r3 = range(parts[3][0], parts[3][1] + 1)
    
    #r = range(A[0], A[1]+1)
    result = 0
    
    if A[1] == 1000000000:
        result += check_sums(r0)
        print(result)
        result += check_sums(r1)
        print(result)
        result += check_sums(r2)
        print(result)
        result += check_sums(r3)
        
    if A[1] in r0:
        r0 = range(parts[0][0], A[1]+1)
        result += check_sums(r0) # 9
        
    if A[1] in r1:
        r1 = range(parts[1][0], A[1]+1)
        result += check_sums(r1) + 9 # 624
        
    if A[1] in r2:
        r2 = range(parts[2][0], A[1]+1)
        result += check_sums(r2) + 624 # 51036
        
    if A[1] in r3:
        r3 = range(parts[3][0], A[1]+1)
        result += check_sums(r3) + 51036
        
    
    return result
    
    
    # for item in r:
    #     sumfirst = 0
    #     sumsecond = 0
    #     s = str(item)
    #     length = len(s)
        
    #     if length % 2 != 0:
    #         continue
    #     else: 
    #         for i in range(length):
                
    #             # Add elements in first half sum
    #             if (i < length // 2):
    #                 sumfirst += int(s[i])
    #             # Add elements in the second half sum
    #             else:
    #                 sumsecond += int(s[i])
        
    #         if sumfirst == sumsecond:
    #             result += 1
                
        
    # return result
            
    


A = '1 99999999'
result = beautiful_numbers(A)
print(result)


# if __name__ == '__main__':
#     T = int(input().strip()) # nr. of testcases

#     for _ in range(T):
#         result = beautiful_numbers(A)
#         print(result)