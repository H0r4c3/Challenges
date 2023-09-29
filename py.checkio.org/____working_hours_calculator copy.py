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
    
    # Count the business days
    business_days = np.busday_count(date1, date2)
    print(f'business_days = {business_days}')
    
    date_format = '%Y-%m-%d'
    
    # Use the strptime(date_str, format) function to convert a date string into a datetime object
    date1 = datetime.strptime(date1, date_format)
    print(date1)
    date2 = datetime.strptime(date2, date_format)
    print(date2)
    
    # Calculate the number of days between the two dates
    nr_of_days = date2 - date1
    nr_of_days = nr_of_days.days
    print(f'nr_of_days = {nr_of_days}')
    
    # Eliminate the holidays
    nr_of_days_without_holy = nr_of_days - len(holy)
    print(f'nr_of_days_without_holy = {nr_of_days_without_holy}')
    
    # Eliminate the weekend days
    final_nr_of_days = nr_of_days_without_holy - business_days
    print(f'final_nr_of_days = {final_nr_of_days}')
    
    # Calculate the number of hours between end_time and start_time
    nr_of_hours = timedelta(hours = int(end_time.split(':')[0])) - timedelta(hours = int(start_time.split(':')[0]))
    nr_of_hours = nr_of_hours.seconds // 3600
    print(f'nr_of_hours = {nr_of_hours}')
    
    # Calculate the total number of hours
    nr_total_of_hours = final_nr_of_days * 8 + nr_of_hours
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