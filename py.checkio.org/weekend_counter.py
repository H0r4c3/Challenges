'https://py.checkio.org/en/mission/weekend-counter/'

'''
You should count the initial and final dates if they fall on a Saturday or Sunday.
'''

from datetime import date, timedelta

def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    diff = to_date - from_date
    print(diff.days)
    
    days_list = [(from_date + timedelta(days=i)).weekday() for i in range(diff.days + 1) if (from_date + timedelta(days=i)).weekday() in [5, 6]]
    print(days_list)
    
    return len(days_list)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
    print('Done!')