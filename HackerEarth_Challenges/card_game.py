'https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/practice-problems/algorithm/card-game-1-44e9f4e7/'

'''
Two friends decided to play a very exciting online card game. At the beginning of this game, each player gets a deck of cards, in which each 
card has some strength assigned. After that, each player picks random card from his deck and they compare strengths of picked cards. 
The player who picked card with larger strength wins. There is no winner in case both players picked cards with equal strength.

First friend got a deck with n cards. The i-th his card has strength . Second friend got a deck with m cards. The i-th his card has strength .

First friend wants to win very much. So he decided to improve his cards. He can increase by 1 the strength of any card for 1 dollar. 
Any card can be improved as many times as he wants. The second friend can't improve his cards because he doesn't know about this possibility.

What is the minimum amount of money which the first player needs to guarantee a victory for himself?
'''

def card_game(a, b):
    a = list(map(int, a.split()))
    b = list(map(int, b.split()))
    
    m = len(a)
    n = len(b)
    
    a.sort()
    b.sort(reverse=True)
    
    money = 0
    
    for item in a:
        if item > b[0]:
            return money
        else:
            money = money + b[0] - item + 1
                
    
    return money

a = '1 3 10'
b = '3 4'

result = card_game(a, b)
print(result)