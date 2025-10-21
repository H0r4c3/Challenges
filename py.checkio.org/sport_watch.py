'https://py.checkio.org/mission/sport-watch/lang/zh-hans/share/47cfeb4c46caa66e90fc35acd1454f80/'

'''
The designers want the watch to warn the athlete that he or she must:

- slow down the pace of exercise if the current heart rate is more than three times the resting heart rate OR the current oxygen saturation is less than 95;
- increase the pace of exercise if the current heart rate is less than twice the resting heart rate AND the current oxygen saturation is greater than 97;
- maintain the pace of exercise if none of the above conditions occur.

Given the resting heart rate, the current heart rate and the current oxygen saturation obtained by the watch, 
write a program that produces the suggestion that the Watch should emit.

Input: Three integers (int).

Output: Integer (slow down - -1, increase - 1, maintain - 0).
'''

#1. Solution (using if, elif, else)
def pace_adjust_(h1: int, h2: int, s: int) -> int:
    if h2 > h1*3 or s < 95:
        return -1
    elif h2 < h1*2 or s > 97:
        return 1
    else:
        return 0
    

# 2. Solution (using match)
def pace_adjust(h1: int, h2: int, s: int) -> int:
    match (h1, h2, s):
        case _ if h2 > h1 * 3 or s < 95:
            return -1
        case _ if h2 < h1 * 2 or s > 97:
            return 1
        case _:
            return 0


print("Example:")
print(pace_adjust(60, 180, 97))

# These "asserts" are used for self-checking
assert pace_adjust(60, 190, 98) == -1
assert pace_adjust(70, 140, 92) == -1
assert pace_adjust(70, 130, 98) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")