'https://py.checkio.org/en/mission/clock-angle/'

'''
You are given a time in 24-hour format and you should calculate a lesser angle between the hour and minute hands in degrees. 
Don't forget that clock has numbers from 1 to 12, so 23 == 11. 
The time is given as a string with the follow format "HH:MM", where HH is hours and MM is minutes. 
Hours and minutes are given in two digits format, so "1" will be written as "01". The result should be given in degrees with precision ±0.1.
'''

    
def clock_angle(time):
    '''
    The minute hand moves 360 degrees in 60 minute (or 6 degrees in one minute) and hour hand moves 360 degrees in 12 hours (or 0.5 degrees in 1 minute). 
    In h hours and m minutes, the minute hand would move (h*60 + m)*6 and hour hand would move (h*60 + m)*0.5. 
    '''
    h, m = [int(t) for t in time.split(':')]
    
    angle = abs((h * 30 + m * 0.5) - (m * 6)) # no negative angles
    print(angle)
    
    angle_min = min(abs(360-angle), angle) # the shorter of the two angles formed by measuring clockwise and counterclockwise.
    
    print(angle_min)
    return angle_min
    

    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
    print('Done!')