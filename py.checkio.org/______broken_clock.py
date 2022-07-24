'https://py.checkio.org/en/mission/broken-clock/'

'''
We have a broken clock. We know how quickly it runs or lags over a specific period of time. 
At first, the clock is set to the correct time, but after a while it begins to display an incorrect time...
You are given three values. The first is the correct starting time. 
The second is the current time displayed on the broken clock (which is incorrect). 
Time is given as strings in the format "hh:mm:ss" (Examples: "01:16:59" and "23:00:13"). 
The third value is a description of the clock error in the format "+(-)N [second, minute, hour](s) at M [second, minute, hour](s)" . 
For Example "+1 second at 10 seconds" -- the clock is 1 second fast for every 10 seconds of actual 
time and "-5 minutes at 5 hours" -- the clock lags 5 minutes for every 5 hours of actual time.
'''
from datetime import datetime, timedelta

def split_error_description(error_description):
    '''
    Extract from error_description string 
    '''
    err_description_list = error_description.split()
    sign = err_description_list[0][0]
    deviation = err_description_list[0][1]
    deviation = int(deviation)*(-1) if sign == '-' else int(deviation)
    unit_deviation = err_description_list[1]
    reference = int(err_description_list[3])
    unit_reference= err_description_list[4]
    
    return deviation, unit_deviation, reference, unit_reference

def conversion_to_seconds(value, unit):
    '''
    Convert all units in seconds
    '''
    if 'minute' in unit:
        value = value * 60
    elif 'hour' in unit:
        value = value * 3600
    
    return value
    

def broken_clock(starting_time, wrong_time, error_description):
    start_time = datetime.strptime(starting_time, '%H:%M:%S')
    wrong_delta_time = datetime.strptime(wrong_time, '%H:%M:%S') - datetime.strptime(starting_time, '%H:%M:%S')
    #wrong_delta_seconds = int(wrong_delta_time.total_seconds())
    #print(wrong_delta_seconds)
    
    deviation, unit_deviation, reference, unit_reference = split_error_description(error_description)
    
    deviation = conversion_to_seconds(deviation, unit_deviation)
    print(f'deviation = {deviation}')
    
    reference = conversion_to_seconds(reference, unit_reference)    
    print(f'reference = {reference}')
    
    #correction = reference + deviation
    #print(f'correction = {correction}')
    #elapsed = int(wrong_delta_seconds / correction)
    #print(f'elapsed = {elapsed}')
    
    #total_time = elapsed * reference
    
    #result = datetime.strptime(starting_time, '%H:%M:%S') + timedelta(seconds = total_time)
    
    #print(str(result.time()))
    #return str(result.time())
    
    #return (start + (wrong - start) * reference / (deviation + reference)).strftime('%X')
    return (start_time + wrong_delta_time * reference / (deviation + reference)).strftime('%X')
    
    
    




# Best Solution: 
# https://py.checkio.org/mission/broken-clock/publications/Sim0000/python-3/first/share/c952e8aaf886265db91a571fbfd4b185/
from datetime import datetime

def broken_clock_(starting_time, wrong_time, error_description):
    timedic = {'second':1, 'minute':60, 'hour':3600, 'seconds':1, 'minutes':60, 'hours':3600}

    # analyze starting time and wrong time
    st = datetime.strptime(starting_time, '%H:%M:%S')
    wt = datetime.strptime(wrong_time, '%H:%M:%S')

    # analyze error_description
    n1, unit1, _, n2, unit2 = error_description.split()
    sec1 = int(n1) * timedic[unit1] # 1st seconds
    sec2 = int(n2) * timedic[unit2] # 2nd seconds

    # return correct time
    return (st + (wt - st) * sec2 / (sec1 + sec2)).strftime('%X')



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
    print('Done!!!')
    
    