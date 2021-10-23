'https://www.hackerrank.com/challenges/mars-exploration/problem?h_r=internal-search'

s = 'SOSSPSSQSSOR'



def marsExploration(s):
    message = 'SOS'

    mult = len(s) // len(message)
    rest = len(s) % len(message)

    mess = message*mult + message[0:rest+1]
    
    counter = 0
    for i in range(len(s)):
        if s[i] != mess[i]:
            counter += 1
    return counter
            
counter = marsExploration(s)
print(counter)
