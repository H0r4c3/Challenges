'https://app.codility.com/programmers/trainings/9/binary_gap/'

'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones 
at both ends in the binary representation of N.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.
'''
import re

def solution(N):
    binary_N = bin(N)[2:]
    print(binary_N)
    
    #repetitions = re.findall(r'10+1', binary_N)
    repetitions = re.findall(r'(?<=1)(0+)1', binary_N)
    print(repetitions)
    
    if not repetitions:
        return 0
    
    gap = max(repetitions, key=len)
    gap = gap.strip('1')
    print(gap)
    
    return len(gap)

assert solution(8) == 0 # 8 = 1000
assert solution(401) == 3 # 401 = 110010001
assert solution(145) == 3 # 145 = 10010001
assert solution(305) == 3 # 305 = 100110001
assert solution(72) == 2 # 72 = 1001000
print('Done!!!')