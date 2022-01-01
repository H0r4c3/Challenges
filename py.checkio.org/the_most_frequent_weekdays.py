'https://py.checkio.org/en/mission/the-most-frequent-weekdays/'

'''
You are given a year as an integer (e. g. 2001). You should return the most frequent day(s) of the week in that particular year. 
The result has to be a list of days sorted by the order of days in a week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.

Input: Year as an int .

Output: The list of most common days sorted by the order of days in a week (from Monday to Sunday).
'''
import datetime

def most_frequent_days(a):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",  "Friday", "Saturday", "Sunday"]
    
    # first day in January
    jan = datetime.date(a, 1, 1).weekday()
    # last day in December
    dec = datetime.date(a, 12, 31).weekday()
    
    result = sorted(list(set([jan, dec])))
    
    return [days[i] for i in result]


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))
    print(most_frequent_days(2016))
    print(most_frequent_days(328))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']