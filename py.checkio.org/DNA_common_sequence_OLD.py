'https://py.checkio.org/en/mission/dna-common-sequence/'

'''
For this mission, we want to compare DNA strands and find the longest common base subsequence in the two strands. 
Subsequences are not required to occupy consecutive positions within the original sequences and letters can be placed at varying distances between each other. 
These strands can be represented as strings consisting of the letters "ACGT". 
For example the longest common sequence for strands "ACGTC" and "TTACTC" is "ACTC".

A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
'''

from itertools import combinations

def subsequence(s1, s2):
    '''
    Initialize the pointers i and j with zero, where i is the pointer to str1 and j is the pointer to str2.
    If str1[i] = str2[j] then increment both i and j by 1.
    Otherwise, increment only j by 1.
    If i reaches the end of str1 then return TRUE else return FALSE.
    '''
    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1
      
    # If i reaches end of s1, that mean we found all characters of s1 in s2,
    # so s1 is subsequence of s2, else not
    return i == n

# My Solution = brute force = time expired!!!
def common(first, second):
    combs_list = list()
    for i in range(len(first)):
        combs = combinations(first, i)
        for item in combs:
            if item not in combs_list:
                combs_list.append(''.join(item))
            
    print(combs_list)
    
    subs = list()
    for item in combs_list:
        if subsequence(item, second) and item not in subs:
            subs.append(item)
    
    # check no common sequence       
    if subs == ['']:
        return ''
    
    subs = sorted(subs, key=len)
    print(subs)
    
    # pick the longest strings
    result = sorted([item for item in subs if len(item) == len(subs[-1])])
    print(result)
    
    # if there are multiple results, make a string from them
    result = ','.join(result)
    print(result)
    
    return result


# NEW Try / Solution:

def subsequence_(s1, s2):
    '''
    Initialize the pointers i and j with zero, where i is the pointer to str1 and j is the pointer to str2.
    If str1[i] = str2[j] then increment both i and j by 1.
    Otherwise, increment only j by 1.
    If i reaches the end of str1 then return TRUE, else return FALSE.
    '''
    n, m = len(s1), len(s2)
    i, j = 0, 0
    sub = ''
    subs = list()
    while i < n:
        print(f's1[i] {s1[i]}  =  s2[j] {s2[j]} ?')
        if (s1[i] == s2[j]):
            sub += s1[i]
            print(sub)
            eq = j
            i += 1
            j += 1
            if j >= m:
                j = eq + 1
                subs.append(sub)
                print(subs)
                sub = ''
        else:
            j += 1
            if j >= m:
                j = eq + 1
                i += 1
                
    
    print(subs)
                
    return subs[0]

def common_(first, second):
    sub = subsequence(first, second)
    print(sub)
    



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    #assert common("GCTT", "AAAAA") == "", "None"
    #assert common("CGTCGTCGT", "CGTACGT") == "CGTCGT"
    #assert common("GTCGCTGTGCAGGTCCGGGTTCA", "GCGACCCGAATCCAGCTATAGGTATATGTCAGTCGGCCGTTAGGT")
    print('Done!!!')