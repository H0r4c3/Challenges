'https://py.checkio.org/en/mission/how-much-gold/'

'''
This bar appears to be made of various metal including gold, iron, copper and tin. 
The bar does not contain any other metal except these. We do not know the quantity of each metal in the bar, 
but we do know the proportions of the various alloys. For example: the gold and tin proportion is 1/2, 
gold and iron -- 1/3, gold and copper -- 1/4. "the gold and tin proportion is 1/2" means that 
gold and tin together (their sum, not their ratio!) are the 1/2 of the whole bar (the sum of them all). 
You should calculate the proportion of gold in the entire bar.
'''

from fractions import Fraction

METALS = ('gold', 'tin', 'iron', 'copper')


def checkio(alloys):
    """
        Find proportion of gold
    """
    gold = 0
    
    for item, value in alloys.items():
        if 'gold' in item:
            gold += value
        else:
            gold += 1 - value
    
    result = (gold - 1) / 2
    
    print(result)
    return result



# Best Solution: 
# https://py.checkio.org/mission/how-much-gold/publications/brownie57/python-3/first/share/12b95d35c340d75ac20b07ee0bd6db51/

def checkio_(alloys):
    bar = 0
    for i in alloys.keys():
        if 'gold' in i:
            bar += alloys[i]
        else:
            bar += 1 - alloys[i]
    return (bar - 1) / 2




#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({
        'gold-tin': Fraction(1, 2),
        'gold-iron': Fraction(1, 3),
        'gold-copper': Fraction(1, 4),
        }) == Fraction(1, 24), "1/24 of gold"
    assert checkio({
        'tin-iron': Fraction(1, 2),
        'iron-copper': Fraction(1, 2),
        'copper-tin': Fraction(1, 2),
        }) == Fraction(1, 4), "quarter"
    
    print('Done!!!')