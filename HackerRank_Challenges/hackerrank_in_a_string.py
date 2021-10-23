'https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem'

'''
We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. 
Remeber that a subsequence maintains the order of characters selected from a sequence.
'''
import re

def hackerrankInString(s):
    # Write your code here
    h = 'hackerrank'
    s_list = [item for item in s]
    print(s_list)
    for i in range(9):
        if (h[i] in s_list) and (h[i+1] in s_list):
            print(i)
            if s_list.index(h[i]) <= s_list.index(h[i+1]):
                s_list = s_list[s_list.index(h[i+1]) : ]
                print(s_list)
                i += 1
            else:
                return 'NO'
        else:
            return 'NO'
    return 'YES'

def hackerrankInString_OK(s):
    # . = any character
    # * = zero or more repetitions
    # h = letter
    # a = letter
    # ...
    if re.search(r'.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*', s):
        return 'YES'
    else:
        return 'NO'
        


s = 'rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'
s = 'hhaacckkekraraannk'
#s = 'hackerworld'
result = hackerrankInString_OK(s)
print(result)