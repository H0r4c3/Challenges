'https://www.hackerrank.com/challenges/repeated-string/problem?h_r=internal-search'

from collections import Counter

# 1. Method
def repeatedString(s, n):
    counter = 0
    if len(s) == 1:
        counter = n
        return counter
    m = n//len(s)+1
    rep_s = m*s
    for item in rep_s[0:n+1]:
        if item == 'a':
            counter +=1
    return counter

# the string repeated 'm' times 
s = 'aba'

# the first n chars where 'a' will be searched
n = 10

counter = repeatedString(s, n)
print(counter)


# 2. Method
def repeatedString2(s, n):
    counter = 0
    if len(s) == 1:
        if s == 'a':
            counter = n
            return counter
        else:
            counter = 0
            return counter
    
    freq = Counter(s)['a']
    m = n//len(s)
    rest = n% len(s)
    s_rest = s[0:rest]
    freq_rest = Counter(s_rest)['a']
    
    counter = freq*m + freq_rest
    return counter

# the string repeated 'm' times 
s = 'aba'

# the first n chars where 'a' will be searched
n = 10

counter = repeatedString2(s, n)
print(counter)