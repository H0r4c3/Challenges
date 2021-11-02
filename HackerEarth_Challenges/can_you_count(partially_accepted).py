'https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/can-you-count-11795975/'

'''
You are given a string s consisting of lowercase English letters and/or '_' (underscore).
You have to replace all underscores (if any) with vowels present in the string.

The rule you follow is:
Each underscore can be replaced with any one of the vowel(s) that came before it.

You have to tell the total number of distinct strings we can generate following the above rule.
'''
# 1. Method

def output_strings(s):
    my_list = list(s.split('_'))
    
    if len(my_list) == 1:
        return 1
    
    my_list = my_list[0:-1]
    
    
    result = 1
    vowels = set()
    for item in my_list:
        if 'a' in item:
            vowels.add('a')
        if 'e' in item:
            vowels.add('e')
        if 'i' in item:
            vowels.add('i')
        if 'o' in item:
            vowels.add('o')
        if 'u' in item:
            vowels.add('u')
        
        result = result*len(vowels)
    
    return result

# 2. Method using regex
import re

def output_strings2(s):
    result = 1
    all_vowels = set()
    r = re.compile('[a-z]*_')
    my_list = re.findall(r, s)
    print(my_list)
    
    if '_' not in my_list:
        return 1
    
    for item in my_list:
        v = re.compile('[aeiou]')
        vowels = set(re.findall(v, item))
        print(vowels)
        all_vowels.update(vowels)
        print(all_vowels)
        result = result * len(all_vowels) 
         
    return result



s = 'ab_ae_' # -> 2
s = 'oga_kuuapa_fe_' # -> 24
s = 'ueo_aa' # -> 3
s = 'apbauisk_'

result = output_strings2(s)
print(result)


# t = input()
# for _ in range(t):
#     s = input()
#     result = output_strings(s)
#     print(result)