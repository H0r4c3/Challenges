'https://py.checkio.org/en/mission/leap-year-checking/'

'''
Check if the given year is leap year. A year is a leap year if it is divisible by 4, 
except for end-of-century years which must be divisible by 400. 
This means that the year 2000 was a leap year, although 1900 was not.
'''

def is_leap_year_(year: int) -> bool:
    '''
    If the year is evenly divisible by 4 and not evenly divisible by 100, or
    If the year is evenly divisible by 400,
    then it's a leap year. Otherwise, it's not a leap year.
    '''
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("Example:")
print(is_leap_year_(1891))


# Best Solution: https://py.checkio.org/mission/leap-year-checking/publications/mortonfox/python-3/first/?ordering=most_voted&filtering=all

from calendar import isleap

def is_leap_year(year: int) -> bool:
    return isleap(year)


# These "asserts" are used for self-checking
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False
assert is_leap_year(2020) == True
assert is_leap_year(2021) == False
assert is_leap_year(1600) == True
assert is_leap_year(1700) == False
assert is_leap_year(1800) == False
assert is_leap_year(2400) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
