'https://py.checkio.org/en/mission/divide-gold/'

'''
each sailor except the Captain should receive exactly the same number of coins;
the captain should receive twice as many coins as a sailor.
'''

def captain_share(gold: int, sailors: int) -> int:
    return (gold / (sailors + 2)) * 2


print("Example:")
print(captain_share(15, 1))

# These "asserts" are used for self-checking
assert captain_share(15, 1) == 10
assert captain_share(28, 2) == 14
assert captain_share(54, 4) == 18

print("The mission is done! Click 'Check Solution' to earn rewards!")