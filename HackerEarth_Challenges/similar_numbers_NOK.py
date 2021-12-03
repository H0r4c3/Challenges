'https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/numbers-2-a9a00311/'

'''
You are given a telephone number of length . Assume that the two phone numbers are similar if the following conditions are met:

They are different.
The number of positions that contains different digits does not exceed .
The difference between the corresponding figures in the numbers does not exceed 1.
Your task is to find how many such numbers are similar to this phone number. Since the answer can be very large, print it modulo .

Input format

The first line indicates two space-separated numbers N, K.
The next line contains N digits.

Output format
Print one number denoting the answer modulo 10 la puterea 9 + 7.

Explanation for 012:
Next telephone numbers suit us: 001, 002, 003, 011, 013, 021, 022, 023, 102, 111, 112, 113, 122.
'''

def similar_numbers(N, K, s):
    result = 0
    my_list = list(map(int, list(s))) # [0, 1, 2]
    all_posib = [[item-1, item, item + 1] for item in my_list] # -> [[-1, 0, 1], [0, 1, 2], [1, 2, 3]]
    for item in all_posib: 
        if item[0] == -1:
            item[0] = 0
        if item[1] == -1:
            item[1] == 0
        if item[2] == -1:
            item[2] == 0
    # -> [[0, 0, 1], [0, 1, 2], [1, 2, 3]]
            
    print(all_posib)
    
    
    
    return all_posib

if __name__ == '__main__':
    # A = list(map(int, input().split()))
    # N = A[0]
    # K = A[1]
    
    N = 3
    K = 2
    s = '012345'
    
    result = similar_numbers(N, K, s)
    print(result) # -> 13 (001, 002, 003, 011, 013, 021, 022, 023, 102, 111, 112, 113, 122)
    
    # check the result
    #assert (similar_numbers(N, K, s)) == 13, "The result should be 13!"
    
    
    
    