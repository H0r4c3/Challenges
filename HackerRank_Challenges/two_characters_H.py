'https://www.hackerrank.com/challenges/two-characters/problem'

from collections import Counter
from itertools import combinations

import logging

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\HackerRank_Challenges\two_characters_H.log'
  
#Create and configure logger
#logging.basicConfig(filename=path, format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

logger = logging.getLogger('main')

def letters_repetition(st):
    char_counts = Counter(st)
    print('Most common = ', char_counts.most_common())

    # create a dictionary from char_counts
    repeat_dict = {}
    for key, value in char_counts.items():
        repeat_dict[key] = value
    print('Repeat dict = ', repeat_dict)
     

def consecutive_position(st):
    ''' Find the letters that are repeated consecutive. These should be removed from the string'''
    ''' Add the position of the first letter in a list names "consec_positive" '''
    consec_position = list()
    for i in range(len(st)-1):
        if st[i]==st[i+1]:
            consec_position.append(i)
            break
    return consec_position


def remove_letters_after_pos(st, pos):
    ''' Remove the letter in position "pos" from the string "st" '''
    #st_rem = st.replace(st[pos], '')
    st_list = list(st)
    print("st_list for removing repeated letters = ", st_list)
    del st_list[pos]
    del st_list[pos]
    print("st_list after removing = ", st_list)
    st_rem = ''.join(st_list)
    print("st_rem = ", st_rem)
    return st_rem


def remove_consec_duplicates(st):
    global st_rem
    consec_position = consecutive_position(st)
    st_list = list(st)
    print('consec_pos = ', consec_position)
    if consec_position == []:
        st_rem = st
        print(st_rem)
        return st_rem
    else:
        del st_list[consec_position[0]]
        del st_list[consec_position[0]]
        st_rem = ''.join(st_list)
        print('st_rem = ', st_rem)
    
    remove_consec_duplicates(st_rem)
        
    
    


def combinations_of_two(st):
    ''' Creates a list with all combinations of two letters from the string "st" '''
    set_from_string = set(st)
    print("set_from_string = ", set_from_string)
    comb_two = list(combinations(set_from_string, 2))
    return comb_two

def letters_not_in_combinations_of_two(st, comb_two):
    letters_for_del_list = list()
    for item in comb_two:
        letters_for_del = set(st) - set(item)
        letters_for_del_list.append(list(letters_for_del))
    
    return letters_for_del_list


s1 = 'aabbccdd'
s3 = 'beabeefeab'
s4 = 'asvkugfiugsalddlasguifgukvsa'
s = 'asdcbsdcagfsdbgdfanfghbsfdab'

# 1. Remove consec_duplicates
logging.info('Call remove_consec_duplicates(s) method')
remove_consec_duplicates(s)

print('The string after remove_consec_duplicates = ', st_rem)
logging.debug(f'The string after remove_consec_duplicates = {st_rem}')

if len(st_rem) == 0:
    print(0)
    exit()
elif len(st_rem) == 1:
    print(1)
    exit()
elif len(st_rem) == 2:
    print(2)
    exit() 

#2. Create a set with the unique letters and make a list with all combinations of two letters
logging.info('Create a set with the unique letters and make a list with all combinations of two letters: combinations_of_two(st_rem) method')
comb_two = combinations_of_two(st_rem)
print('comb_two = ', comb_two)
logging.debug(f'comb_two = {comb_two}')

#3. Keep only the letters from combinations of two
logging.info('Create a list with the letters for removing from the st_rem in order to remain only the combinations of two letters')
letters_for_del_list = letters_not_in_combinations_of_two(st_rem, comb_two)
print('letters_for_del_list = ', letters_for_del_list)
logging.debug(f'letters_for_del_list = {letters_for_del_list}')

list_of_strings = list()
for item in letters_for_del_list:
    st_rem2 = st_rem[:]
    print('st_rem2 = ', st_rem2)
    for i in range(len(item)):
        st_rem2 = st_rem2.replace(item[i], '')
        print('st_rem2 after removing 1 char = ', st_rem2)
    list_of_strings.append(st_rem2)
print(list_of_strings)
logging.debug(f'list_of_strings made only of two letters = {list_of_strings}')

#4. Verify that the letters are alternative (not consecutive) and remove the wrong strings
logging.info('Verify that the letters are alternative (not consecutive) and remove the wrong strings')

list_of_strings_copy = list_of_strings[:]
for item in list_of_strings_copy:
    print(item)
    logging.debug(f'list_of_strings = {list_of_strings}')
    logging.debug(f'String to be verified = {item}')
    for i in range(len(item)-1):
        if item[i]==item[i+1]:
            logging.debug(f'String not ok = {item}')
            #print(item)
            logging.debug(f'if item {item} in list of strings {list_of_strings}')
            if item in list_of_strings:
                list_of_strings.remove(item)
                logging.debug(f'Item removed = {item}')
                logging.debug(f'list_of_strings after removing = {list_of_strings}')
            break
           
        else:
            #print('OK')
            logging.debug(f'String OK = {item}')
            pass
logging.debug(f'Remaining strings in list_of_strings = {list_of_strings}')

#5. Pick the longest string (and the combination of the two letters who generate it)
logging.info('Pick the longest string')

if len(list_of_strings) == 1:
    max_st = list_of_strings[0]
else:
    max_st = max(list_of_strings, key=len)
    
print("String Result = ", max_st)
print('Result =', len(max_st))

#print('TEST remove_consec_duplicates = ', remove_consec_duplicates('aabbHccdd'))


