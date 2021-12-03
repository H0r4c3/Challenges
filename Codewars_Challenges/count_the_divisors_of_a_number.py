'https://www.codewars.com/kata/542c0f198e077084c0000c2e?utm_source=newsletter'

'''
Count the number of divisors of a positive integer n.
'''

def divisors(n):
    divlist = [] 
    i = 1 
    if i <= n: 
        rest = n % i 
        if rest == 0: 
            divlist.append(i)
        i += 1
    
    return divlist
    

n = 30
divlist = divisors(n)
print (f'The divisors of the given number are:  {divlist}') # -> [1,2,3,5,6,10,15,30]