'https://py.checkio.org/en/mission/super-root/'

'''
The super root of a number N is the number x , such that x x = N .

The result should be accurate so that x x ≈ N±0.001 . Or N - 0.001 < x x < N + 0.001 .
'''
from math import pow

def super_root(number):
    
    
    return 0



# Best Solution:
# https://py.checkio.org/mission/super-root/publications/coells/python-3/second/share/e0bca1b9b8e8d91bc90971f6bb569fb7/

def super_root(n):
    x = 10
    while abs(x**x - n) >= 0.001: 
        x += n ** (x ** -1)
        x /= 2
    
    print(x)
    return x


# Best Solution: 
# https://py.checkio.org/mission/super-root/publications/Tinus_Trotyl/python-3/smack-in-the-middle/?ordering=most_voted&filtering=all

def super_root(number):
    m, M = 0, 10
    while True:
        root = (m + M) / 2 
        sqr = root ** root
        if round(sqr, 4) == number: return root
        m, M = (root, M) if sqr < number else (m, root)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
    print('Done!')