'https://py.checkio.org/en/mission/when-is-friday/'

'''
Your task is to write a function that will count how many days are left from a certain date to Friday. 
The argument will be a particular date in a string format looking like this: 'dd.mm.yyyy', where 'dd' - day, 'mm' - month, and 'yyyy' - year.
For example, if that given day is Thursday, then the answer will be 1. If that day is Monday, the result is 4. 
And, if that day is Friday, the function should return 0.
'''

from datetime import datetime
def friday_(day):
    d = datetime.strptime(day, '%d.%m.%Y')
    nr = d.weekday()
    print(nr)
    
    result = 4 - nr if nr <= 4 else 6 - nr + 5
    print(result)

    return result


# another solution (using pandas)
import pandas as pd
def friday_(day):
    d = pd.Timestamp(day)
    nr = d.weekday()
    print(nr)
    result = 4 - nr if nr <= 4 else 6 - nr + 5
    print(result)

    return result


# Best solution: https://py.checkio.org/mission/when-is-friday/publications/flpo/python-3/4-dateweekday-7/?ordering=most_voted&filtering=all#comment-111185
import datetime

def friday(day):
    d, m, y = map(int, day.split('.'))
    date = datetime.date(y, m, d)
    print(date)
    
    return (4 - date.weekday()) % 7



if __name__ == '__main__':
    print("Example:")
    #print(friday('23.04.2018'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert friday('23.04.2018') == 4
    #assert friday('01.01.1999') == 0
    assert friday("11.11.1111") == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")