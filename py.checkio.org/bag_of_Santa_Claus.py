'https://py.checkio.org/en/mission/bag-of-santa-claus/'

'''
Your function will be called many times in the same environment. 
For each step you are given a value of the current gift, the quantity if gifts in the current bag and a number of the current gift (counted from 1). 
For each step you should make a choice to take a gift or not -- True or False.

Your function will be checked repeatedly for different bags containing anywhere from 10 to 1000 gifts. 
We will count only the best gifts from each bag as the second rate gifts are not for us. All calls are running in the same environment, so be careful with globals. 
You should choose 700+ the best gifts from 2000 bags.

Input: Three arguments.
current_gift - a value of the current gift as an float.
gifts_in_bag - the quantity of gifts in a bag as an integer.
gift_number - a number of the current gift as an integer (from 1 to gifts_in_bag).
Output: Do you accept the current gift or not as a boolean value.
'''

def choose_good_gift(current, n, i):
    
    
    return True



# Best Solution: 
# https://py.checkio.org/mission/bag-of-santa-claus/publications/_Chico_/python-3/first/share/4208cdf397f1283ca4a11009a70e18a1/

def choose_good_gift(current, n, i):
    global max_gift
    # ignore first int(n*0.3678) gifts, and record max value.
    if i < int(n * 0.3678):
        max_gift = current if i == 1 else max(current, max_gift)
        return False
    # When the best to date is founded, accept the gift.
    return i == n or current > max_gift


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    from random import random, randint, uniform

    scale = (random() + random()) ** randint(0, 1024)

    standings = gift_count = best_gifts = 0
    bag_count = 2000
    for i in range(bag_count):
        gifts_in_bag = randint(10, 1000)
        gift_count += gifts_in_bag

        gifts = []
        selected_gift = None
        for i in range(gifts_in_bag):
            new_gift = uniform(0., scale)
            gifts.append(new_gift)
            decision = choose_good_gift(new_gift, gifts_in_bag, i + 1)
            if decision:
                selected_gift = new_gift
                gifts.extend([uniform(0., scale) for _ in range(gifts_in_bag - i - 1)])
                break
        if selected_gift is None:
            priority = len(gifts)
        else:
            priority = sum(selected_gift < x for x in gifts)
        standings += priority
        best_gifts += not priority
    print('You do won {:n} best gifts from {:n} bags with {:,} gifts!\n'
          'It seems like for bags of {:n} gifts -\n'
          'you would choose the second best gift, silver ;)'
          .format(best_gifts, bag_count, gift_count, round(gift_count / standings) + 1))
