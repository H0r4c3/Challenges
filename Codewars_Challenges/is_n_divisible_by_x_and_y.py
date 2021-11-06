'https://www.codewars.com/kata/5545f109004975ea66000086/train/python'

'''
Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
'''

def is_divisible(n,x,y):
    #your code here
    if n%x==0 and n%y==0:
        result = True
    else:
        result = False
        
    return result
        
n = 12
x = 3
y = 4

result = is_divisible(n, x, y)
print(result)