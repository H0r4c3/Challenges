'https://py.checkio.org/en/mission/calls-home/'

'''
Each call is represented as a string with date, time and duration of the call in seconds in the following format:
"YYYY-MM-DD hh:mm:ss duration"
The date and time here are the start of the call.
Space-Time Communications Co. has several rules on how to calculate the cost of calls:

First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
After 100 minutes in one day, each minute costs 2 coins per minute;
All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
Calls count to the day when they began. For example, if a call was started 2014-01-01 23:59:59, then it should be counted to 2014-01-01;
'''

from typing import List
from math import ceil
from collections import defaultdict

def total_cost(calls: List[str]) -> int:
    days_dict = defaultdict(list)
    result = 0
    
    for call in calls:
        day, _, duration_seconds = call.split()
        
        # create a dictionary having key = day, and value = list with the durations of calls for that day
        days_dict[day].append(ceil(int(duration_seconds) / 60))
        print(days_dict)
    
    for key, duration_minutes in days_dict.items():
        # if a day has many calls, sum the durations
        duration_minutes = sum(duration_minutes)
        print(key, duration_minutes)
        cost_minutes = 100 + (duration_minutes - 100) * 2 if duration_minutes > 100 else duration_minutes
        print(key, cost_minutes)
        result += cost_minutes
        
    print(result)
    return result



# Best Solution:
# https://py.checkio.org/mission/calls-home/publications/saklar13/python-3/first/share/a2b0fdfa57555067cce868c54d01435f/

def total_cost_(calls):
    days = {}
    for call in calls:
        day, _, duration = call.split()
        duration = (int(duration) + 59) // 60
        days[day] = days.get(day, 0) + duration
    return sum(max(x, x*2 - 100) for x in days.values())



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
    
    print('Done!!!')