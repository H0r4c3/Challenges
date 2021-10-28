'https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/special-substrings-9fb5dbe8/'

'''
You have a string S, but you like only special strings. So, you have to calculate the total number of special substrings in S.

A string T, of length L, is called special string, if either of the following property holds:

All characters of the string T are same. for example, 
The string has an odd length (i.e, L is odd) and all characters of T are same except the middle character, for example, .
Count the total number of special substrings in S.
'''

def special_substrings(test_str):
    counter = 0
    my_list = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)]
    for item in my_list:
        if len(item) == 1:
            counter += 1
            
        if len(item) == item.count(item) != 1:
            print(item)
            counter += 1
            
        if len(item) % 2 != 0:
            if item.count(item[0]) == len(item) - 1:
                if item[0] != item[len(item)//2]:
                    counter += 1
            
    return counter


from itertools import combinations

def special_substrings2(test_str):
    counter = 0
    my_list2 = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r = 2)]
    for item in my_list2:
        if len(item) == 1:
            counter += 1
            print(item)
            
        if len(item) == item.count(item) != 1:
            print(item)
            counter += 1
            print(item)
            
        if len(item) % 2 != 0:
            if item.count(item[0]) == len(item) - 1:
                if item[0] != item[len(item)//2]:
                    counter += 1
                    print(item)
            
    return counter
        

test_str = 'aaaaaaaaaa' # -> 55
#test_str = 'aba'

result = special_substrings2(test_str)
print(result)