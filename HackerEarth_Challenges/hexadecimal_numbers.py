'https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/yet-another-easy-problem-1f3273a0/'

'''
You are given a range . You are required to find the number of integers  in the range such that  where  is equal to the sum of digits of  in its hexadecimal (or base 16) representation.

For example, F(27) = 1 + B = 1 + 11 = 12 (27 in hexadecimal is written as 1B). You are aksed T such questions. 
'''

# T = int(input())
# A = ''
# S = list()

# for i in range(T):
#     A[i] = input().strip()
#     S[i] = A[i].split()

import math

def sum_digits_string1(str1):
    sum_digit = 0
    for x in str1:
        if x == 'a':
            z = 10
        elif x == 'b':
            z = 11
        elif x == 'c':
            z = 12
        elif x == 'd':
            z = 13
        elif x == 'e':
            z = 14
        elif x == 'f':
            z = 15
        else:
            z = int(x)
            
        sum_digit = sum_digit + z

    return sum_digit

def sum_digits_string2(nr):
    sum_digits = 0

    for i in hex(nr)[2:]:
        sum_digits += int(i, 16)

    return sum_digits

def hexadecimal_numbers(A):
    s = A.split(' ')
    L = int(s[0])
    R = int(s[1])
    counter = 0
    
    # if R < 16:
    #     if L == 1:
    #         return R - L
    #     else:
    #         return R - L + 1
    
    # transform the integer in hexadecimal and make the sum of the digits
    for item in range(L, R+1):
        #h = hex(item).lstrip('0x')
        #print(f"{item} = {h}", end=' | ')
        
        #suma = sum_digits_string1(h)
        suma = sum_digits_string2(item)
        
        if math.gcd(item, suma)>1:
            counter = counter + 1
            
        
    return counter

A = '454 500'
A = '50 96895'
result = hexadecimal_numbers(A)
print(result)

# if __name__ == '__main__':
#     T = int(input().strip()) # nr. of testcases

#     for i in range(T):

#         result = sum_of_digits(A[i])
        
#         print(result)