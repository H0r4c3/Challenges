'https://py.checkio.org/en/mission/number-factory/'

'''
You are given a two or more digits number N . 
For this mission, you should find the smallest positive number of X , such that the product of its digits is equal to N. 
If X does not exist, then return 0.

Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit. 
Also we can factorize it as 4*5 or 2*2*5. 
The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.
'''

def factors(n):
    facs = list()
    i, c = 0, 5
    c_list = [6, 7, 8, 9, 4, 2, 3]
    while (n > 1):
        if (n % c == 0):
            facs.append(c)
            n = n / c
        else:
            i += 1
            if i == 7:
                return sorted(facs)
            c = c_list[i]
    
    return sorted(facs)


def convert_into_integer(facs):
    facs_str = ''.join([str(item) for item in facs])
    facs_int = int(facs_str)
    
    return facs_int
    
    

def checkio(number):
    print(f'number = {number}')
    
    facs = factors(number)
    print(f'facs = {facs}')
    if len(facs) < 2:
        return 0
    
    # convert into integer
    facs_int = convert_into_integer(facs)
    print(f'facs_int = {facs_int}')
    
    return facs_int


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example" # 4*5
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(3645) == 5999, "7th example"
    assert checkio(1680) == 5678
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")