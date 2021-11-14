'https://py.checkio.org/en/mission/days-diff/'

'''
You are given two dates as an array with three numbers - a year, month and day. For example: 19 April 1982 will be (1982, 4, 19). 
You should find the difference in days between the given dates. 
For example between today and tomorrow = 1 day. 
The difference will always be either a positive number or zero, so don't forget about the absolute value.
'''

from datetime import date

def days_diff(a, b):
    
    date1 = date(a[0], a[1], a[2])
    date2 = date(b[0], b[1], b[2])
    
    result = (date2 - date1).days
    
    if result < 0:
        result = (date1 - date2).days
        
    
    return result


if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")