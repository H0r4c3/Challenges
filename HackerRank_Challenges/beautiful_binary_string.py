'https://www.hackerrank.com/challenges/beautiful-binary-string/problem?h_r=internal-search'

'''
Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring .

In one step, Alice can change a  to a  or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.
'''


def beautifulBinaryString(b):
    counter = 0
    s = '010'
    s_ok = '011'
    if s in b:
        b_new = b.replace(s, s_ok)
    
    for i in range(len(b)):
        if b[i] != b_new[i]:
            counter += 1
        
    return counter

b = '0101010'
result = beautifulBinaryString(b)
print(result)