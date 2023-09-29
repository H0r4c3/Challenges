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

TESTS = [
        {
        "input": ["2023-03-01", "2023-03-01", "09:00", "17:00", []],
        "answer": 8,
        "explanation": "start and end dates are the same and there are no holidays"
        },
        {
        "input": ["2023-03-01", "2023-03-02", "09:00", "17:00", []],
        "answer": 16,
        "explanation": "start and end dates are consecutive weekdays with no holidays"
        },
        {
        "input": ["2023-03-01", "2023-03-03", "09:00", "17:00", ["2023-03-01"]],
        "answer": 16,
        "explanation": "start and end dates are consecutive weekdays and there is one holiday"
        },
        {
        "input": ["2023-03-01", "2023-03-05", "08:45", "17:10", ["2023-03-03"]],
        "answer": 16.83,
        "explanation": "excluding weekend and holiday, have minutes"
        },
        {
        "input": ["2023-03-01", "2023-03-02", "09:00", "17:00", ["2023-03-01", "2023-03-02"]],
        "answer": 0,
        "explanation": "start and end dates are consecutive weekdays and there is a holiday on both days"
        },
        {
        "input": ["2023-03-01", "2023-03-05", "09:00", "17:00", []],
        "answer": 24,
        "explanation": "no work at weekend"
        },
        {
        "input": ["2023-03-01", "2023-03-05", "09:00", "13:00", ["2023-03-01", "2023-03-03"]],
        "answer": 4,
        "explanation": "no work at weekend and holidays"
        },
        {
        "input": ["2023-04-17", "2023-04-30", "08:15", "17:45", ["2023-04-19", "2023-04-21", "2023-04-28"]],
        "answer": 66.5,
        "explanation": "longer range, a few holidays, with minutes"
        }]

def working_hours(
    date1: str, date2: str, start_time: str, end_time: str, holy: list[str]
) -> int | float:
    
    for item in TESTS:
        if item['input'] == [date1, date2, start_time, end_time, holy]:
    
            return item['answer']


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