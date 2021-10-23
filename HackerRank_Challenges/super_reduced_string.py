'https://www.hackerrank.com/challenges/reduced-string/problem'


import logging

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Misc\HackerRank_Challenges\super_reduced_string.log'

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

# def superReducedString(s):
#     st = ''
#     logging.info('Starting loop')
#     i = 0
#     while i < len(s):
#         logging.debug(f'i = {i}')
#         logging.debug(f's[i] = {s[i]}, s[i+1] = {s[i+1]}')
#         logging.debug(f's = {s}')
#         if s[i] == s[i+1]:
#             logging.debug(f's = {s}')
#             #s = s.replace(s[i], '')
#             del s[i]
#             logging.debug(f's after 1 deletion = {s}')
#             logging.debug(f's = {s}')
#             #s = s.replace(s[i], '')
#             logging.debug(f's after 2 deletions = {s}')
#             logging.debug(f's = {s}')
#         else:
#             i = i + 1
#             logging.debug(f'i = i + 1 = {i}')
#             logging.debug(f's = {s}')
#     return s

# def superReducedString2(s):
#     my_list = list(s)
#     prev_value = None
#     for item in my_list[:]: # the : means we're slicing it, making a copy in other words
#         if item == prev_value:
#             my_list.remove(prev_value)
            
#         else:
#             prev_value = item
#     return my_list

def superReducedString3(s):
    #ok_list = list()
    my_list = list(s)
    le = len(my_list)
    i = 0
    while i < le-1:
        print('1 DIFF i =', i, my_list[i], my_list[i+1])
        if my_list[i]==my_list[i+1]:
            print('2 Before REMOVE i =', i, my_list[i], my_list[i+1])
            print(my_list)
            #my_list.remove(my_list[i])
            del my_list[i]
            print('After First REMOVE', my_list)
            #my_list.remove(my_list[i])
            del my_list[i]
            print('After Second REMOVE', my_list)
            if my_list == []:
                st = ''
                return 'Empty String'
            i = i - 1
            if i < 0:
                i = 0
            le = le - 2
            print('3 After REM i =', i, my_list[i], my_list[i+1])
        else:
            #ok_list.append(my_list[i])
            i = i + 1
            
    st = ''.join(my_list)
    
    return st
            
            

s = 'abaabccddd'
s = 'zbaabccddd'
s = 'aaabccddd'
s = 'aa'
s = 'zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'
# result = tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh
s = 'abaabccddd'

result = superReducedString3(s)
assert result != 'tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh', 'Wrong!'

print(result)