'https://py.checkio.org/en/mission/working-hours-calculator/share/c78e01b3a78b87cdaad9f56e0873b404/'

'''
Write a function that takes two dates and two times as input and returns the total number of working hours between the two dates (incl. both). 
Times representing the start and end of a workday. 
Working hours are defined as the time between the end and start times, Monday through Friday, excluding holidays. 
So the function also takes an argument that specifies a list of holidays to exclude (could be empty).
Time may have minutes. Convert them into float as minutes/60 with two-digits precision.

Input: Five arguments: two dates as strings, two times as strings, holidays as list of strings.

Output: Number of total working hours as integer or float.
'''

import numpy as np
from datetime import datetime, timedelta

def working_hours(date1: str, date2: str, start_time: str, end_time: str, holy: list[str]) -> int | float:
    print(f'START: {date1}, {date2}, {start_time}, {end_time}, {holy}')
    
    # Get business days excluding weekends and holidays 
    # The busday_count() function doesn’t include the day of end dates
    business_days = np.busday_count(date1, date2, holidays=holy)
    print(f'business_days = {business_days}')
    
    # Get Day Number from weekday
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    weekno = date2.weekday()
  
    if weekno < 5:
        w = 1
        print("date2 is a Weekday")
    else:  
        # 5 Sat, 6 Sun
        w = 0
        print("date2 is a Weekend")
        
    business_days = business_days + w
    
    # Convert start_time string to datetime
    t1 = datetime.strptime(start_time, "%H:%M")
    print('Start time:', t1.time())
    
    # Convert end_time string to datetime
    t2 = datetime.strptime(end_time, "%H:%M")
    print('End time:', t2.time())
    
    # Calculate the number of hours between start_time and end_time
    delta = t2 - t1
    print(f'delta = {delta}')
    
    # Convert in hours with two-digits precision
    delta_minutes = delta.total_seconds() // 60
    print(f'nr_of_minutes = {delta_minutes}')
    delta_hours = delta_minutes // 60
    print(f'nr_of_hours = {delta_hours}')
    
    delta_hours = round(delta_hours, 2)
    print(f'nr_of_hours rounded = {delta_hours}')
    
    # Calculate the total number of hours
    nr_total_of_hours = business_days * 8 + delta_hours
    print(f'nr_total_of_hours = {nr_total_of_hours}')
    
    return nr_total_of_hours


print("Example:")
#print(working_hours("2023-03-01", "2023-03-01", "09:00", "17:00", []))

# These "asserts" are used for self-checking
assert working_hours("2023-03-01", "2023-03-01", "09:00", "17:00", []) == 8
assert working_hours("2023-03-01", "2023-03-02", "09:00", "17:00", []) == 16
assert working_hours("2023-03-01", "2023-03-03", "09:00", "17:00", ["2023-03-01"]) == 16
assert (
    working_hours("2023-03-01", "2023-03-05", "08:45", "17:10", ["2023-03-03"]) == 16.83
)

print("The mission is done! Click 'Check Solution' to earn rewards!")