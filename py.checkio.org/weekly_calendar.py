'https://py.checkio.org/en/mission/weekly-calendar/'

'''
You are given four integers as input values. (A year, month, day and the first day of the week [0: Monday...6: Sunday])
You must return a list (or an iterable) of the week that includes the date in the input values.
This begins with the first day of the week.
'''


from typing import List
from datetime import date
from calendar import Calendar


def weekly_calendar(year: int, month: int, day: int, firstweekday: int) -> List[int]:
    the_day = date(year, month, day)
    the_month = Calendar(firstweekday=firstweekday).monthdatescalendar(year, month)
    
    for week in the_month:
        if the_day in week:
            the_week = week
            
    list_of_days = [d.day for d in the_week]
    
    print(list_of_days)
    return list_of_days
    


# Best Solution:
# https://py.checkio.org/mission/weekly-calendar/publications/kurosawa4434/python-3/calendarmonthdatescalendar/share/0ba66bc880758f0fa096f30594836467/

from typing import List
from calendar import Calendar
from datetime import date


def weekly_calendar_(year: int, month: int, day: int, firstweekday: int) -> List[int]:

    tgt_date = date(year, month, day)
    for week in Calendar(firstweekday=firstweekday).monthdatescalendar(year, month):
        if tgt_date in week:
            return [d.day for d in week]



if __name__ == '__main__':
    print("Example:")
    #print(list(weekly_calendar(2020, 1, 1, 0)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(weekly_calendar(2020, 1, 1, 0)) == [30, 31, 1, 2, 3, 4, 5], "01/01/2020 Monday"
    assert list(weekly_calendar(2020, 9, 20, 6)) == [20, 21, 22, 23, 24, 25, 26], "09/20/2020 Sunday"
    assert list(weekly_calendar(2020, 9, 30, 0)) == [28, 29, 30, 1, 2, 3, 4], "09/30/2020 Monday"
    assert list(weekly_calendar(2020, 2, 29, 2)) == [26, 27, 28, 29, 1, 2, 3], "02/29/2020 Wednesday"
    print("Coding complete? Click 'Check' to earn cool rewards!")