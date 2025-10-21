'https://py.checkio.org/en/mission/autopilot/share/94e0eacfa5d0d48fe6b7b90fb8de73fb/'

'''
Input: Three integers (int), which represent the current positions of the backs of cars A, B and C, respectively.

Output: An integer 1 if car B needs to accelerate; -1 if it needs to decelerate; or 0 if it needs to maintain its current speed.
'''

def speed_adjust(A: int, B: int, C: int) -> int:
    if (B-A) > (C-B):
        return -1
    elif (B-A) < (C-B):
        return 1
    else:
        return 0


print("Example:")
print(speed_adjust(2, 4, 6))

# These "asserts" are used for self-checking
assert speed_adjust(0, 2, 6) == 1
assert speed_adjust(0, 4, 6) == -1
assert speed_adjust(0, 3, 6) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")