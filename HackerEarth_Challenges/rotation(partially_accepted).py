'https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/rotation-1-38ecf5a7/'

'''
You are given two strings S and T of the same length N. Your task is to convert the string S into T by doing some operations. 
In an operation, you can delete the first character of the string S and append any character at the end of the string. 
You are required to determine the minimum number of operations to convert S into T.

Input format:
First line: Single integer  denoting the length of the strings
Second line: String S
Third line: String T
Output format:
Print a single integer that represents the answer to the question.
'''

import difflib
def rotation_(S, T):
    # Partially accepted
    
    seq_mat = difflib.SequenceMatcher(a=S, b=T)
    match = seq_mat.find_longest_match(alo=0, ahi=len(S), blo=0, bhi=len(T))
    common = S[match.a : match.a + match.size]
    print(match)
    print(common)
    
    return match.a
    
    
def rotation(S, T):
    counter = 0
    for i in range(N):
        if(T.find(S[i : N])== -1):
            counter+=1

    return counter


if __name__ == '__main__':
    # N = int(input())
    # S = input() # string
    # T = input() # string

    N = 7
    S = 'aaxaabc'
    T = 'aabcaax'
    
    N = 113
    S = 'ndafmffmuuwjzqpquwjhuftohawpfegsjvnxwipwqlswvawogjuyiqtzsgpwgosegmuuhpzwchejuiitumyescxxyecnsatcbfpseqzowvdjyvchg'
    T = 'zqpquwjhuftohawpfegsjvnxwipwqlswvawogjuyiqtzsgpwgosegmuuhpzwchejuiitumyescxxyecnsatcbfpseqzowvdjyvchgavqnonmkwgqp'
    result = 12
    
    result = rotation(S, T)
    
    print(result) # -> 3 or 12