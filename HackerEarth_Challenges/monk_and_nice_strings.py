'https://www.hackerearth.com/practice/codemonk/'

'''
Strings are arranged in an array A, and the Niceness value of string at position i is defined as 
the number of strings having position less than i which are lexicographicaly smaller than A[i].

Note: Array's index starts from 1.

Input:
First line consists of a single integer denoting N.
N lines follow each containing a string made of lower case English alphabets.

Output:
Print N lines, each containing an integer, where the integer in i-th line denotes Niceness value of string A[i].

Solution:
Number of strings having index less than 1 which are less than "a" = 0
Number of strings having index less than 2 which are less than "c": ("a") = 1
Number of strings having index less than 3 which are less than "d": ("a", "c") = 2
Number of strings having index less than 4 which are less than "b": ("a") = 1
'''

# N = int(input())
# A = list()

# for i in range(N):
#     A[i] = input()


def nice_string(A):
    print(0)
    for i in range(1, N):
        s = A[i]
        #print(f's = {s}')
        A_sliced = sorted(A[:i+1])
        #print(f'A_sliced = {A_sliced}')
        print(A_sliced.index(s))

A = ['a', 'c', 'd', 'b']
N = len(A)
result = nice_string(A)
#print(result)


# for i in range(N):
#     result = nice_string(A)
#     print(result)