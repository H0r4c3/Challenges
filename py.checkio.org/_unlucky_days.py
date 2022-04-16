'https://py.checkio.org/en/mission/unlucky-days/'

'''
Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.
'''

from datetime import datetime

def checkio(year: int) -> int:
    jan = datetime(year, 1, 13).weekday() # -> number of the day in week
    jan = datetime(year, 1, 13).strftime("%A") # what is the name of the day in 13th of January, year = year
    print(jan)
    
    result = 0
    
    for month in range(1, 13):
        if datetime(year, month, 13).strftime("%A") == 'Friday':
            print(year, month)
            result +=1
    
    print(result)
    return result



# Best Solution:
# https://py.checkio.org/mission/unlucky-days/publications/Merzix/python-3/first/share/bf3ac371a83a2babbc88aa7743bd55eb/
from datetime import datetime


def checkio_(year):
    return sum(datetime(year, month, 13).weekday() == 4 for month in range(1, 13))


# Clear Solution:
# https://py.checkio.org/mission/unlucky-days/publications/thealfest1/python-3/simple/share/7152453a4c435fe1f7b93dfe8d6a670e/
from datetime import date

def checkio_(year):
    return sum(1 for m in range(1, 13) if date(year, m, 13).weekday() == 4)



if __name__ == '__main__':
    print("Example:")
    print(checkio(2015))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
    print("Coding complete? Click 'Check' to earn cool rewards!")