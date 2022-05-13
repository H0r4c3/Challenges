'https://py.checkio.org/en/mission/birthday-party/share/806d4908b4e9babfd530f32d2acc9511/'

'''
I was hoping you could help me calculate the party date by the given birthday date, but, as I said before, the date should meet specific requirements:

It should always be the closes weekend to my birthday.
I don't want to celebrate before the birthday.
But I'm ok with marking in the day.
Input: Date of my birthday.

Output: Date of the party.
'''

import datetime

def birthday_party(birthday: datetime.date) -> datetime.date:
    nr_day = birthday.weekday()
    
    if nr_day == 5 or nr_day == 6:
        return birthday
    
    nr_party_day = 5 - nr_day
    
    partyday = birthday + datetime.timedelta(nr_party_day)
    
    print(nr_day)
    
    return partyday


# Best Solution: 
# https://py.checkio.org/mission/birthday-party/publications/oduvan/python-3/keep-testing-match/

import datetime

def birthday_party_(birthday: datetime.date) -> datetime.date:
    # your code here
    match birthday.weekday():
        case 5 | 6:
            return birthday
        case weekday:
            return birthday + datetime.timedelta(days=5-weekday)


print('Example:')
print(birthday_party(datetime.date(2022, 1, 5)))

assert birthday_party(datetime.date(2022, 1, 5)) == datetime.date(2022, 1, 8)
assert birthday_party(datetime.date(2022, 2, 21)) == datetime.date(2022, 2, 26)
assert birthday_party(datetime.date(2022, 3, 26)) == datetime.date(2022, 3, 26)
assert birthday_party(datetime.date(2022, 4, 17)) == datetime.date(2022, 4, 17)
assert birthday_party(datetime.date(2022, 3, 30)) == datetime.date(2022, 4, 2)