'https://py.checkio.org/en/mission/ghosts-age/'

'''
After some experimenting, Nikola thinks he has discovered the law of ghostly opacity. 
On every birthday, a ghost's opacity is reduced by a number of units equal to its age when its age is a Fibonacci number 
or increased by 1 if it is not.

For example:
A newborn ghost -- 10000 units of opacity.
1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).
3 year -- 9997 - 3 = 9994 (3 is a Fibonacci number).
4 year -- 9994 + 1 = 9995 (4 is not a Fibonacci number).
5 year -- 9995 - 5 = 9990 (5 is a Fibonacci number).
Help Nicola write a function which will determine the age of a ghost based on its opacity. 
You are given opacity measurements as a number ranging from 0 to 10000 inclusively.
'''

import math
'''
A  function that returns true if x is perfect square
'''
def isPerfectSquare(x):
    root = int(math.sqrt(x))
    return root * root == x

def isFibo(n):
    '''
    A number n is Fibonacci if and only if one or both of (5*n*n + 4) or (5*n*n - 4) is a perfect square
    '''
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

def list_opacity(n):
    '''
    Calculates the list of opacities
    '''
    list_opacities = list()
    list_opacities.append(10000)
    
    for age in range(1, n):
        if isFibo(age):
            list_opacities.append(list_opacities[age-1] - age)
        else:
            list_opacities.append(list_opacities[age-1] + 1)
            
    return list_opacities
    

def checkio(opacity):
    '''
    opacity = previous_opacity - age if age is Fibo
    opacity = previous_opacity + 1 if age is not Fibo
    list_opacity = [10000, 9999, 9997, 9994, 9995, 9990, ..., 0]
    age = list_opacities.index(opacity)
    '''
    list_opacities = list_opacity(10000)
    #print(list_opacities)
    
    print(list_opacities.index(opacity))
    return list_opacities.index(opacity)


# def calculate_opacity(age):
#     '''
#     Calculates the opacity for an age
#     '''
#     if age == 0:
#         return 10000
#     else:
#         if isFibo(age):
#             return calculate_opacity(age-1) - age
#         else:
#             return calculate_opacity(age-1) + 1
        
# print(calculate_opacity(5))


# Best Solution: 
# https://py.checkio.org/mission/ghosts-age/publications/vmiimu/python-3/9thuw/?ordering=most_voted&filtering=all

import math

def checkio(opacity):
  def is_fib(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n

  y,o = 0, 10000
  while True:
    o = (o-y) if is_fib(y) else (o+1)
    
    if o == opacity:
      return y
    else:
      y += 1


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
    print('Done!')