'https://py.checkio.org/en/mission/next-birthday/'

'''
You have to write a function that receives a "today" date and a dictionary of family birthdates, and for the person(s) whose birthday is 
next (today or later), return the number of days between "today" and that birthday, and the age they will be.

Note about leap days: If someone is born on February 29th, then he or she will celebrate birthdays on March 1st when necessary.
'''

from typing import Dict, Tuple

Date = Tuple[int, int, int]


def next_birthday(today: Date, birthdates: Dict[str, Date]) -> Tuple[int, Dict[str, int]]:
    ...


# Best Solution: 
# https://py.checkio.org/mission/next-birthday/publications/Oksana_Antropova/python-3/calendarisleapyear-with-explanations/?ordering=most_voted&filtering=all

from typing import Dict, Tuple
from datetime import date
import calendar

Date = Tuple[int, int, int]

def leap_date(year: int, month: int, day: int) -> date:
    """"
    Changes February 29th for March 1st if the year is common
    """
    if (month, day) == (2, 29) and not calendar.isleap(year):
        month, day = 3, 1
    return date(year, month, day)

def next_celebration(today: date, born: date) -> date:
    """
    Finds the date of next celebration:
    - processes the leap dates;
    - if the celebration this year has already passed adds one to the year of next celebration
    """
    born = leap_date(today.year, born.month, born.day)
    year = today.year + ((born.month, born.day) < (today.month, today.day))
    return leap_date(year, born.month, born.day)

def next_birthday(today: Date, birthdates: Dict[str, Date]) -> Tuple[int, Dict[str, int]]:
    today = date(*today)
    next_celebrations = {name : next_celebration(today, date(*birthday)) 
                            for name, birthday in birthdates.items()}
    nearest_celebration = min(next_celebrations.values())
    diff = (nearest_celebration - today).days            
    return (diff, {name : date.year - birthdates[name][0] 
                for name, date in next_celebrations.items() if date == nearest_celebration})


# Best Solution: 
# https://py.checkio.org/mission/next-birthday/publications/veky/python-3/birth-certifidate/?ordering=most_voted&filtering=all

from datetime import date, timedelta

class Person:
    def __init__(self, name, birth_date, today):
        self.name = name
        birth_date, today = date(*birth_date), date(*today)
        nbd = birthday_in_year(birth_date, today.year)
        if nbd < today: nbd = birthday_in_year(birth_date, today.year + 1)
        self.following_age = nbd.year - birth_date.year
        self.days_till_birthday = (nbd - today).days

def birthday_in_year(birth_date, year):
    try: return birth_date.replace(year)
    except ValueError: return birthday_in_year(birth_date + timedelta(1), year)

def next_birthday(today, birthdates):
    people = {Person(name, ymd, today) for name, ymd in birthdates.items()}
    min_days = min(person.days_till_birthday for person in people)
    return min_days, {person.name: person.following_age for person in people
                                   if person.days_till_birthday == min_days}


if __name__ == '__main__':
    FAMILY = {
        'Brian': (1967, 5, 31),
        'Léna': (1970, 10, 3),
        'Philippe': (1991, 6, 15),
        'Yasmine': (1996, 2, 29),
        'Emma': (2000, 12, 25),
    }

    TESTS = [
        ((2020, 9, 8), (25, {'Léna': 50})),
        ((2021, 10, 4), (82, {'Emma': 21})),
        ((2022, 3, 1), (0, {'Yasmine': 26})),
    ]

    for nb, (day, answer) in enumerate(TESTS, 1):
        user_result = tuple(next_birthday(day, FAMILY.copy()))
        if user_result != answer:
            print(f'You failed the test #{nb}.')
            print(f'Your result: {user_result}')
            print(f'Right result: {answer}')
            break
    else:
        print('Well done! Click on "Check" for real tests.')