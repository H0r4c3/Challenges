'https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/string-division/'

'''
Kevin has a string S consisting of N lowercase English letters.
Kevin wants to split it into 4 pairwise different non-empty parts. For example, string "happynewyear" can be splitted into "happy", "new", "ye" and "ar". 
He can't delete any characters or change the order of the characters.
Help Kevin and find if there exist at least one possible spliting.
'''

# def string_division(s):
#     if len(set(s)) >= 4:
#         return 'YES'
#     if len(s) < 4:
#         return 'NO'
    
#     n = 2
#     comb = [s[i:i+n] for i in range(0, len(s), n)]
#     my_set = set(comb)
#     print(my_set)
    
#     if len(my_set) >= 4:
#         return 'YES'
#     else:
#         return 'NO'
    
def string_division_OK(s):
    ss=set(list(s))
    if(len(ss)>=4 or len(s)>=10):
        print("YES")
    elif(len(ss)==3 and len(s)>=5):
        print("YES")
    elif(len(ss)==2 and len(s)>=7):
        print("YES")
    else:
        print("NO")


s = 'ababca'
s = 'llelllldhllqrl' # -> YES

result = string_division_OK(s)
print(result)


# T = int(input())
# for _ in range(T):
#     s = input()
#     result = string_division(s)
#     print(result)

