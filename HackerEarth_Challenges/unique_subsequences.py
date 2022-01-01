'https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/unique-subsequence-264057c9/'

'''
You are given a string S that contains N characters. 
Your task is to determine the maximum possible size of the subsequence T of S such that no two adjacent characters in T are the same.

Input format

First line: A single integer T denoting the number of test cases
For each test case:
First line: Single integer N denoting the size of the string
Second line: S denoting the string
Output format

For each test case, print a single line containing one integer that represents the maximum size of the subsequence that satisfies the provided condition.
'''

def unique_subsequences_1(N, S):
    result = 0
    counter_list = list()
    x = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            counter_list.append(i-x)
            x = i + 1
            
    counter_list.append(N-x)
    print(counter_list)
    print(sum(counter_list))
            
    return sum(counter_list)

def unique_subsequences_2(N, S):
    duplicates = 0
    
    for i in range(N-1):
        if S[i] == S[i+1]:
            duplicates += 1
    
    return (N - duplicates)


if __name__ == '__main__':
    S = 'abaadeffonecdurc'
    S = 'ababa'
    S = 'aaaac'
    #S = 'typxhovlyoxaznskpihumdtjfmyhdxfpkttoznimyazfpoammhtjxmvgdagndbtwxsicmllpsjuedljffvekxxahecyestqrxvjmaucfjbcbymsslgcixqecwxowgakqtlnspoiwbigmexivwlhtuzibybbqioagtedwltavsvlcfaxaefubklvijuaxfyaydtsdjaksppdceuzunibxpnvdprrfpcqaqppluigxdoasnktlkhhuydxgpwaosgsybmyheurcaccuugeyqhdwehvnuyyedtyvieegwsjhkwqnfmifbyiufmbfiimqtmcmtspkzmlaubpwoluuaytkfhzpjxirqqhhttjxvbkohlxjjjsjxdlcvetrkcudvjnmrvrmwfghxzfcbpqsimnzynntbarpefbwxmqtsnhzbfzgykpxzwtucbmieaosdgmaprotitkndfvhlkajkxlsvfsvdqxciderotzvftcudkvcdxxmpgssqttceauzbnhycookltposldogkolvdgtwhoxdhgvsmzwaikltfpinstveqsrseiuhuuzvzgvmipcbanpirxnuhwlujcgznzhdrricfiqromcvlghgqafpdednhkmiqhtxssxfiwolbedsphnpciqbhmoxraxfpecmztzpsjitforhaqdtcdwngcacrbyzlqwovksuhvzqrhwzhoklauiqjmtfjaidwcsjftuyrvfgtjtunmcmcrljjweojjskvftmfkukzaiybmtqutmoaytxzcqlnsysaszqjfzmkqogrsucinhwsfdbryvidaonftlnwxfqhrmghiqxeejdaczdmrppgezrvmphzicycohbpvivzeqnvxhuihxitvprfixbgufyxmluicryjutkftycljkksqtoijwsrgfghbtlelzvopeqxvzxklswzedyuevgqzgbslcczyindlzkkntgijvaxaiiliiltlktlzclyifieemdslu'
    # Result = 960
    
    N = len(S)
    
    result = unique_subsequences_2(N, S)
        
    print(result)
    
    
    # T = int(input().strip()) # nr. of testcases

    # for _ in range(T):
    #     N = int(input()) # length of the string S
    #     S = input() # string

    #     result = unique_subsequences(N, S)
        
    #     print(result)