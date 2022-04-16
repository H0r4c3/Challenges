'https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/master-cf6dadd7/'

'''
Harry was studying a magic book that categorizes the magic spells into 3 categories - Good , Worst and Bad. 
If any spell contains all the vowels in alphabetical order then that spell is categorized as Good. 
If it contains the vowels in reverse alphabetical order , then that spell is categorized as Worst. 
All the other spells that do not fall in any of the categories before are categorized as Bad. 

Now Harry tries to evaluate himslef by solving a spell categorization exercise at the end of the book , but 
since he is confused can you help him by solving the problems.

Note: The spell is a word of lower case English alphabets only. If there are no vowels in the string, then the spell is classified as "Good".

Input Format

The first line of input consists of an integer  denoting the number of spells that need to be classified. Each of the next  lines contains a word .

Output Format

For each string, output the category to which the spell belongs in a new line.
'''

def magic_spells(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    vowels_in_s = [item for item in s if item in vowels]
    vowels_str = ''.join(vowels_in_s)
    print(vowels_str)
    vowels_str_asc = ''.join(sorted(vowels_in_s, reverse=False))
    print(vowels_str_asc)
    vowels_str_desc = ''.join(sorted(vowels_in_s, reverse=True))
    
    if vowels_str == vowels_str_asc:
        print('Good')
        return 'Good'
    elif vowels_str == vowels_str_desc:
        return 'Worst'
    else:
        return 'Bad'


if __name__ == '__main__':
    assert magic_spells('discount') == 'Good'
    assert magic_spells('weak') == 'Worst'
    assert magic_spells('goalkeeper') == 'Bad'
    
    print('Done!!!')
    
    
    
    
# Solution for the site
'''
def magic_spells(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    vowels_in_s = [item for item in s if item in vowels]
    vowels_str = ''.join(vowels_in_s)
    vowels_str_asc = ''.join(sorted(vowels_in_s, reverse=False))
    vowels_str_desc = ''.join(sorted(vowels_in_s, reverse=True))
    
    if vowels_str == vowels_str_asc:
        return 'Good'
    elif vowels_str == vowels_str_desc:
        return 'Worst'
    else:
        return 'Bad'


if __name__ == '__main__':
    N = int(input().strip()) # nr. of testcases

    for _ in range(N):
        s = input() # string
        result = magic_spells(s)
        print(result)
'''
