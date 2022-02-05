'https://py.checkio.org/en/mission/the-first-working-day/'

'''
As the input you’ll get the date of the first vacation day in the format 'YYYY-MM-DD' and the total number of vacation days. 
Your task is to find out which day will be the first working day after the vacation. If it’ll be Saturday or Sunday then it should be the next Monday.
In this mission you have to ignore national holidays and consider only Saturdays and Sundays.
Also don't forget about February 29th in the leap year and the situation when the vacation starts at the end of December of the one year and ends at 
the beginning of the next year.
'''

from datetime import datetime
from datetime import timedelta

def vacation(date, days):
    start_date = datetime.strptime(date, "%Y-%m-%d")
    end_date = start_date + timedelta(days=days)
    
    # find out what day it is
    day_number = end_date.weekday()
    
    print(start_date)
    print(end_date)
    print(day_number)
    
    if day_number < 5:
        print(end_date.strftime('%Y-%m-%d'))
        return end_date.strftime('%Y-%m-%d')
    elif day_number == 5:
        end_date = end_date + timedelta(days=2)
        print(end_date.strftime('%Y-%m-%d'))
        return end_date.strftime('%Y-%m-%d')
    elif day_number == 6:
        end_date = end_date + timedelta(days=1)
        print(end_date.strftime('%Y-%m-%d'))
        return end_date.strftime('%Y-%m-%d')
  


if __name__ == '__main__':
    print("Example:")
    print(vacation('2018-07-01', 14))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert vacation('2018-07-01', 14) == '2018-07-16'
    assert vacation('2018-02-19', 10) == '2018-03-01'
    assert vacation('2000-02-28', 5) == '2000-03-06'
    assert vacation('1999-12-20', 14) == '2000-01-03'
    assert vacation('2020-07-27', 11) == '2020-08-07'
    print("Coding complete? Click 'Check' to earn cool rewards!")