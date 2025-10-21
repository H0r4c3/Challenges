'https://py.checkio.org/en/mission/divide-gold-rates-are-rising/share/4e7cb6cca48c3ebddcd02150df3f1c27/'

'''
So, the priority of checking cases should be the following:

Captain's double share, no kills;
The crew makes a riot against Captain;
Captain starts to kill sailors;
Captain kills all and take all gold.
'''

def winner_share_(gold: int, sailors: int) -> int:
    share = (gold / (sailors + 2)) * 2
    print(share)
    if type(share) is int:
        return share
    else:
        print('Another method')
        

def winner_share__(gold: int, sailors: int) -> int:
    share1 = gold / (sailors + 2)
    print(f'share1 = {share1}')
    share2 = gold / sailors
    print(f'share2 = {share2}')
    share3 = gold / (sailors + 1)
    print(f'share3 = {share3}')
    
    if share1 * (sailors + 2) == gold:
        return share1 * 2
    elif share2 * sailors == gold:
        return 0
    if share3 * (sailors + 1) == gold:
        return share3 * 2
    else:
        return gold
    
    
def winner_share(gold: int, sailors: int) -> int:
    share1 = gold / (sailors + 2)
    print(f'share1 = {share1}')
    if sailors != 0:
        share2 = gold / sailors
        print(f'share2 = {share2}')
    share3 = gold / (sailors + 1)
    print(f'share3 = {share3}')
    if sailors - 1 != 0:
        share4 = gold / (sailors - 1)
        print(f'share4 = {share4}')
    
    if gold % (sailors + 2) == 0:
        return share1 * 2
    elif gold % sailors == 0:
        return share2
    elif gold % (sailors + 1) == 0:
        return share3 * 2
    elif gold % (sailors - 1) == 0:
        return share4 * 2
    else:
        return gold
        


print("Example:")
#print(winner_share(15, 1))

# These "asserts" are used for self-checking
assert winner_share(15, 4) == 6
assert winner_share(16, 4) == 4
assert winner_share(100, 11) == 20
assert winner_share(15, 1) == 10
assert winner_share(28, 2) == 14
assert winner_share(54, 4) == 18
assert winner_share(10, 0) == 10

print("The mission is done! Click 'Check Solution' to earn rewards!")