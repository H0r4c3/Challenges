'https://py.checkio.org/en/mission/sun-angle/'

'''
Your task is to find the angle of the sun above the horizon knowing the time of the day. 
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. 
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 
6:00 PM is the time of the sunset so the angle is 180 degrees. 
If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".
'''

from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    hours, minutes = map(int, time.split(':'))
    minutes = hours*60 + minutes
    
    if minutes in range(360, 1080):
        return (minutes - 360) * 90 / 360
    if minutes in range(0, 360):
        return "I don't see the sun!"
    if minutes in range(1080, 1440):
        return "I don't see the sun!"



if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"