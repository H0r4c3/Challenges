'https://py.checkio.org/en/mission/time-converter-12h-to-24h/'

'''
You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places. 
Your task is to convert the time from the 12-h format into 24-h by following the next rules:
- the output format should be 'hh:mm'
- if the output hour is less than 10 - write '0' before it. For example: '09:05'
'''

from datetime import datetime

def time_converter(time:str):
    time = time.replace('a.m.', 'AM').replace('p.m.', 'PM')
    print(f'time = {time}')

    in_time = datetime.strptime(time, "%I:%M %p")
    print(f'in_time = {in_time}')
    
    out_time = datetime.strftime(in_time, "%H:%M")
    print(f'out_time = {out_time}')
    
    return out_time


    

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")