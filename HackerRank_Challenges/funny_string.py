'https://www.hackerrank.com/challenges/funny-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign'

'''
In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g. . 
Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. 
If the list of absolute differences is the same for both strings, they are funny.

Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.
'''

def funnyString(s):
    s_copy = s[::-1]
    s_ascii = [abs(ord(s[i+1]) - ord(s[i])) for i in range(len(s)-1)]
    s_copy_ascii = [abs(ord(s_copy[i+1]) - ord(s_copy[i])) for i in range(len(s_copy)-1)]
    
    if s_ascii == s_copy_ascii:
        return 'Funny'
    else:
        return 'Not Funny'


s1 = 'acxz'
s2 = 'bcxz'

result = funnyString(s2)
print(result)