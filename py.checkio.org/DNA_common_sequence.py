'https://py.checkio.org/en/mission/dna-common-sequence/'

'''
For this mission, we want to compare DNA strands and find the longest common base subsequence in the two strands. 
Subsequences are not required to occupy consecutive positions within the original sequences and letters can be placed at varying distances between each other. 
These strands can be represented as strings consisting of the letters "ACGT". 
For example the longest common sequence for strands "ACGTC" and "TTACTC" is "ACTC".

A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
'''
import re
from itertools import combinations

def subsequence_(s1, s2):
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

def all_combs_(my_list):
    combs_list= list()
    for i in range(len(my_list), 0, -1):
        combs = map(list, combinations(my_list, i))
        for item in combs:
            if item not in combs_list:
                combs_list.append(''.join(item))
                
    return combs_list

def all_combs_(my_string):
    combs_set= set()
    for i in range(len(my_string), 0, -1):
        combs_set = combs_set.union(map(lambda x: ''.join(x), combinations(my_string, i)))
                
    return combs_set
            
# My Solution = brute force = ErrorProcessOutOfSystemLimits!!! (need to be optimized!!!!!!!!)
def common_(first, second):
    combs_set1 = all_combs(first)
    combs_set2 = all_combs(second)
            
    print(combs_set1)
    print(combs_set2)
    
    subs = sorted(list(combs_set1.intersection(combs_set2)), key = len)
    print(subs)
    
    # check no common sequence       
    if subs == ['']:
        return ''
    
    # pick the longest strings
    result = [item for item in subs if len(item) == len(subs[-1])]
    print(result)
    
    # if there are multiple results, make a string from them
    result = ','.join(result)
    print(result)
    
    return result


# NEW Try / Solution: for a single string as result

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


# New Solution:
def common(my_string1, my_string2):
    for i in range(len(my_string1), 0, -1):
        common = list()
        combs1 = combinations(my_string1, i)
        combs1_list = list(combs1)
        print(combs1_list)
        combs2 = combinations(my_string2, i)
        combs2_list = list(combs2)
        print(combs2_list)
        common = [item for item in combs1_list if item in combs2_list]
        #common = filter(lambda x: x in combs1_list, combs2_list)
        print(list(common))
        if list(common):
            common = sorted(map(lambda x: ''.join(x), common))
            result = ','.join(common)
            print(result)
            return result
    return ''



# New Solution: using regex

def create_pattern(comb):
    pattern = ''
    for letter in comb:
        pattern += letter + '?'
    return pattern

def transformation(common_list):
    subs = sorted(list(set(common_list)), key = len)
    print(subs)
    
    # check no common sequence       
    if subs == ['']:
        return ''
    
    # pick the longest strings
    result = [item for item in subs if len(item) == len(subs[-1])]
    print(result)
    
    # if there are multiple results, make a string from them
    result = ','.join(sorted(result))
    print(result)
    
    return result
    

def common(first, second):
    common_list = list()
    for i in range(len(first), 0, -1):
        print(f'i = {i}')
        combs = combinations(first, i)
        #print(f'combs = {list(combs)}')
        for comb in combs:
            print(f'i = {i}')
            print(f'comb = {comb}')
            pattern = create_pattern(comb)
            print(f'pattern = {pattern}')
            match = re.findall(pattern, second)
            print(f'match = {match}')
            common_list.extend(match)
    print(f'common_list = {common_list}')
    result = transformation(common_list)
    
    return result

 
# BEST Solution: 
# https://py.checkio.org/mission/dna-common-sequence/publications/veky/python-3/dynamursion/?ordering=most_voted&filtering=all

'''
common is just a wrapper around recursive function cset,
    which returns a set of common subsequences of maximal length (CSOML)
    common just sorts (lexicographically) and joins (with ",") cset's result

cset (memoized recursive function) of sequences X and Y has three cases:
    if any of them is empty, the only common subsequence is the empty one
    else if they agree on first letter, every CSOML must start with that letter
    else, ignore first letter of each, recursively compute csets, union them,
        and return those sequences in the union having maximal length
'''

import functools

@functools.lru_cache(maxsize=None)
def cset(X, Y):
    if not (X and Y): return {""}
    if X[0] == Y[0]: return {X[0] + seq for seq in cset(X[1:], Y[1:])}
    seqs = cset(X, Y[1:]) | cset(X[1:], Y)
    return {seq for seq in seqs if len(seq) == max(map(len, seqs))}

common_ = lambda *args: ",".join(sorted(cset(*args)))



if __name__ == '__main__':
    #These "asserts" using only for self-checkp[;;;;;;;;;;;;;;-ing and not necessary for auto-testing
    #assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    #assert common("GCTT", "AAAAA") == "", "None"
    #assert common("CGTCGTCGT", "CGTACGT") == "CGTCGT"
    #assert common("GTCGCTGTGCAGGTCCGGGTTCA", "GCGACCCGAATCCAGCTATAGGTATATGTCAGTCGGCCGTTAGGT") == 'TGTCAGTCGGC'
    print('Done!!!')