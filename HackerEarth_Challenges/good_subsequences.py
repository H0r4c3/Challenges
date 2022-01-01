'https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/good-sequences-46c31a23/'

'''
You are given a string  consisting of lowercase alphabets. A good subsequence of this string is a subsequence which contains distinct characters only.

Input format

First line: An integer  denoting the number of test cases
Each of the next  lines: String 
Output format

For each test case, print the number of good subsequences of the maximum length modulo .
Answer for each test case should come in a new line.
'''
from collections import Counter

def good_subsequences(S):
    
    number = 1
    val = Counter(S).values()
    
    print(Counter(S))
        
    for i in val:
        number = number * i
    
    print(number%(10**9+7))
    result = number%(10**9+7)
    
    return result
    

if __name__ == '__main__':
    S = 'aaa'
    S = 'abba' # -> 4
    #S = 'abcd'
    
    N = len(S)
    
    result = good_subsequences(S)
        
    print(result)
    
    
    # T = int(input().strip()) # nr. of testcases

    # for _ in range(T):
    #     S = input() # string

    #     result = unique_subsequences(N, S)
        
    #     print(result)