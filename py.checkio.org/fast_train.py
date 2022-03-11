'https://py.checkio.org/en/mission/fast-train/'

'''
You are planning the train schedule and you want to know the minimum time of traveling between the stations.

Starting speed is 0.
Speed limit is set for each section of the rail. You don't exceed it.
You must reach the target station at speed 1 (because it’s necessary to stop at the station).
You should return the minimum time (minutes) as an integer.
'''

from typing import List


# https://py.checkio.org/mission/fast-train/publications/Phil15/python-3/9-liner-bfs/share/83dc1b280ab8ce3387de33ca6ff2df3d/
def fast_train(sections: List[List[int]]) -> int:
    limit = sum(([speed] * dist for dist, speed in sections), [])
    q, end = [[1]], len(limit)
    while q: # queue of possible speeds lists
        speeds = q.pop(0)
        pos, speed = sum(speeds), speeds[-1] # current position/speed
        if pos == end and speed == 1: return len(speeds)
        q += [speeds + [s] for s in (speed + 1, speed, speed - 1)
              if 0 < s <= end - pos and all(s <= limit[pos + i] for i in range(s))]
        


if __name__ == '__main__':
    print("Example:")
    print(fast_train([(4, 3)]))

    assert fast_train([(4, 3)]) == 3
    assert fast_train([(9, 10)]) == 5
    assert fast_train([(5, 5), (4, 2)]) == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")