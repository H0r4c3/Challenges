'https://py.checkio.org/en/mission/lightbulb-start-watching/'

'''
You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit. 
Now let's add one more parameter - the counting start time.

This means that the light continues to turn on and off as before. 
But now, as a result of the function, I want not only to know how long there was light in the room, but how long the room was lit, starting from a certain moment.

One more argument is added - start_watching , and if it’s not passed, we count as in the previous version of the program for the entire period
'''

from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    
    total_time = 0
    
    all_timers = sorted(els + [start_watching])
    i = all_timers.index(start_watching)
    
    for j in range(i + (i % 2 == 0), len(all_timers), 2):
        print(j)
        time_delta = (all_timers[j + 1] - all_timers[j]).total_seconds()
        total_time += time_delta
        
    return total_time



# another solution: 
# https://py.checkio.org/mission/lightbulb-start-watching/publications/Phil15/python-3/maxstart_watching-or-end-end/?ordering=most_voted&filtering=all
def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """how long the light bulb has been turned on"""
    return sum((max(start_watching or end, end) - max(start_watching or start, start)).total_seconds()
        for start, end in zip(els[::2], els[1::2]))



if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 5),
        )
    )

    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 5),
        )
        == 5
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 610
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 600
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
        )
        == 620
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 10, 11),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
                datetime(2015, 1, 12, 11, 10, 11),
                datetime(2015, 1, 12, 12, 10, 11),
            ],
            datetime(2015, 1, 12, 12, 9, 11),
        )
        == 60
    )

    print("The second mission in series is done? Click 'Check' to earn cool rewards!")