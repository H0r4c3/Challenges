'https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/'

'''
You are provided an array  of size  that contains non-negative integers. Your task is to determine whether the number that is formed 
by selecting the last digit of all the N numbers is divisible by .
'''

# N = int(input())
# A = list(map(int, input().split()))

def divisibility(A):
    if A[-1] % 10 == 0:
        return 'Yes'
    else:
        return 'No'


A = [85, 25, 65, 21, 84]
A = [85, 25, 65, 21, 80]

result = divisibility(A)
print(result)