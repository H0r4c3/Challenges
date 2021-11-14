'https://py.checkio.org/en/mission/date-and-time-converter/'

'''
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.
'''

def date_time(time: str) -> str:
    month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    
    day = time[0:2]
    month = time[3:5]
    year = time[6:10]
    hours = time[11:13]
    minutes = time[14:16]
    
    # transformations
    day = str(int(day))
    month = month_dict[int(month)]
    
    if int(minutes) > 1 or int(minutes) == 0:
        hours = str(int(hours)) + ' hours '
    else:
        hours = str(int(hours)) + ' hour '
    
    if int(minutes) > 1 or int(minutes) == 0:
        minutes = str(int(minutes)) + ' minutes'
    else:
        minutes = str(int(minutes)) + ' minute'
    
    result = day + ' ' + month + ' ' + year + ' year ' + hours + minutes
    
    return result


if __name__ == "__main__":
    
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"), "Millenium"
    assert (date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"), "Victory"
    assert (date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"), "Somebody was born"