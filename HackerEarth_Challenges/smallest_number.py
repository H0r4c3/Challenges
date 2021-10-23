'https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/smallest-number-5-5b41ef1d/'

'''
You are given a string  that represents a number. This string consists of the following characters only:

You can perform the following operation:
Swap any two adjacent characters only if the absolute difference between the characters is 
Your task is to determine the smallest number that can be formed by using the provided operation. 
You can perform this operation any number of times (possibly zero). 
'''

def smallest_number_Horace_NOK(S):
    N = len(S)
    S = list(map(int, list(S)))
    for i in range(N-1):
        if abs(S[i] - S[i+1]) == 1:
            if S[i+1] < S[i]:
                S[i], S[i+1] = S[i+1], S[i]
                i = i + 1
            else:
                i = i + 1
        else:
            i = i + 1
    
    result = ''.join(map(str, S))
    
    return result


def smallest_number_OK(S):
    pre = S[ : S.find('3')] # slice S till the first '3'
    print(pre)

    suf = S[S.find('3') : ] # slice S after the first '3'
    print(suf)

    pre = pre + ''.join(x for x in suf if x == '2') # add to 'pre' a string made by '2' from 'suf'
    print(pre)

    suf = ''.join(x for x in suf if x != '2') # suff is made of numbers different from '2'
    print(suf)

    result =(''.join(sorted(pre)) + suf)
    
    return result


if __name__ == '__main__':
    #T = int(input().strip()) # nr. of testcases
    
    S = '213123'
    result = smallest_number_OK(S)
    print(result)
    
    
    # for _ in range(T):
    #     N = int(input().strip())
    #     S = input()

    #     result = smallest_number(S)
        
    #     print(result)