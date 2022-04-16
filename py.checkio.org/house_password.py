'https://py.checkio.org/en/mission/house-password/'

'''
The password will be considered strong enough if its length is greater than or equal to 10 symbols, 
it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
The password contains only ASCII latin letters or digits.
'''
import re

# Solution nr. 1
def checkio_(data: str) -> bool:
    print(data)
    print(len(data) >= 10)
    print(re.findall('\d', data))
    print(re.findall('[A-Z]', data))
    print(re.findall('[a-z]', data))
    
    if len(data) < 10: return False
    if re.findall('\d', data) == []: return False
    if re.findall('[A-Z]', data) == []: return False
    if re.findall('[a-z]', data) == []: return False
    else: return True
    


# Solution nr. 2
def checkio(data: str) -> bool:
    regex = '(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{10,})'
    
    if re.findall(regex, data) == []: 
        return False
    else: 
        return True


# Best Solution: 
# https://py.checkio.org/mission/house-password/publications/suic/python-3/cephs-refactored/?ordering=most_voted&filtering=choice

import re

def checkio(d):
    return len(d) > 9 and all(re.search(p, d) for p in ('[A-Z]', '\d', '[a-z]'))
    #return len(d) > 9 and all([re.search('[A-Z]', d), re.search('\d', d), re.search('[a-z]', d)])



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")