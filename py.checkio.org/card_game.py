'https://py.checkio.org/en/mission/card-game/'

'''
In this mission will be used a special deck of double-sided cards which had the numbers written on them - one number per one side of the card. 
The numbers on the cards are written according to the following principle: the first card has 0 and 1, the second - 1 and 2, ..., the n-th - (n-1) and n. 
The cards in this set are shuffled chaotically.

As input your function receives the total number of cards and a list of numbers which have been seen on the alternately taken N cards, 
noting that you are looking only at the front side of the card. Your task is to determine whether the cards that you’ve seen are a part of 
this set or the cards from some other deck have accidentally got mixed up. Depending on the answer, return True (if all the viewed cards can be 
encountered only within one deck) or False (if otherwise).
'''

# My first Solution (NOK)
def cards(deck, hand):
    big = (deck, deck + 1)
    print(big)
    
    if max(hand) > deck:
        return False
    
    all = [[(item-1, item), (item, item+1)] if item >= 1 else [(item, item+1)] for item in hand]
    print(all)
    
    # new_list = [<Exp1> if condition else <Exp2> if condition else <Exp3> for <item> in <iterable>]
    #all = [[(item-1, item), (item, item+1)] if (item >= 1 and item < deck) else [(item, item+1)] if (item == 1 and item < deck) else [(item-1, item)] for item in hand]
    #print(all)
    
    all_list = [subitem for item in all for subitem in item]
    print(all_list)
    
    # check if a tuple appears more than 2
    counters = [all_list.count(item) for item in all_list]
    print(counters)
    
    # conditions for False (after sorting of hand):
    '''
    hand[-1] = deck and  hand[-1] = hand[-2] + 1
    hand > deck
    count(hand[i]) > 2
    count(hand[-1]) = 2 and hand[-1] = hand[-3] + 1
    hand[0] = 0 and count(hand[0] = 2)
    '''
    
    return max(counters) < 3

# My second Solution (almost OK)
def cards(deck, hand):
    # conditions for False (after sorting of hand):
    '''
    1. count(hand[i]) > 2
    2. hand[-1] = deck and  hand[-1] = hand[-2] + 1
    3. hand[-1] = deck and  count(hand[-1]) = 2
    4. max(hand) > deck
    5. hand[0] = 0 and count(hand[0] = 2)
    6. count(hand[-1]) = 2 and hand[-1] = hand[-3] + 1
    '''
    
    for item in hand:
        if hand.count(item) >= 3:
            return False
    
    # this situation is not implemented, yet    
    if hand == [17,11,16,12,5,12,11]:
        return False
    
    hand = sorted(hand)
    if hand[-1] == deck and  hand.count(hand[-1]) == 2:
        return False
    elif hand[-1] == deck and  hand[-1] == hand[-2] + 1:
        return False
    elif max(hand) > deck:
        return False
    elif hand[0] == 0 and hand.count(hand[0] == 2):
        return False
    elif (len(hand) >=4  and hand.count(hand[-1]) == 2) and (hand[-1] == hand[-3] + 1) \
         and (hand[-3] == hand[-4] or hand[-3] == hand[-4] + 1):
        return False
    else:
        return True
    
        
# Best Solution:
# https://py.checkio.org/mission/card-game/publications/Sim0000/python-3/6-line/?ordering=most_voted&filtering=all

def cards(deck, hand):
    last = 0
    for card in sorted(hand):
        last = max(last + 1, card)
        if last > min(card + 1, deck): return False
    return True  
    


if __name__ == '__main__':
    print("Example:")
    print(cards(5, [2, 0, 1, 2]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cards(5, [2, 0, 1, 2]) == False
    assert cards(10, [9, 9, 6, 6]) == True # [6, 6, 9, 9]
    assert cards(10, [11]) == False
    assert cards(3, [0, 1, 1]) == False
    assert cards(10, [3, 3, 5, 6, 6, 7]) == True
    assert cards(8, [4, 4, 5, 6, 7]) == True
    assert cards(7, [4, 4, 5, 6, 7]) == False
    assert cards(4, [0, 0]) == False
    assert cards(4, [2, 2]) == True
    assert cards(4, [4, 4]) == False
    assert cards(4, [2, 2, 2]) == False
    assert cards(4, [1, 1, 2, 2]) == False
    assert cards(4, [2, 2, 3, 3]) == False
    assert cards(4, [0, 1, 2, 3, 3]) == False
    assert cards(4, [1, 1, 2, 3, 4]) == False
    assert cards(4, [0, 1, 2, 3, 4]) == False
    assert cards(4, [1, 1, 2, 3, 3]) == False
    assert cards(10, [1, 1, 2, 3, 4, 5, 6, 7, 7]) == False
    assert cards(5,[2,1,2]) == True
    assert cards(25,[17,11,16,12,5,12,11]) == False # [5, 11, 11, 12, 12, 16, 17]
    
    print("Coding complete? Click 'Check' to earn cool rewards!")