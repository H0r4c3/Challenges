'https://py.checkio.org/en/mission/feed-pigeons/'

'''
I start to feed one of the pigeons. 
A minute later, two more fly by and, a minute after that, another 3. Then 4, and so on (Ex: 1+2+3+4+...). 
One portion of food lasts a pigeon for a minute, but in case there's not enough food for all the birds, 
the pigeons who arrived first ate first. Pigeons are hungry animals and eat without knowing when to stop. 
If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?
'''

def checkio(number):
    food_eaten = {1 : 1, 2 : 1*2 + 2*1, 3 : 1*3 + 2*2 + 3*1, 4 : 1*4 + 2*3 + 3*2 + 4*1}
    pigeons_total = {1 : 1, 2 : 1+2, 3 : 1+2+3, 4 : 1+2+3+4}
    pigeons_fed_with_at_least_1_portion = {1 : 1, 2 : 1+2, 3 : 1+2+3, 4 : 1+2+3+4} # if there are enough portions left for all pigeons
    
    
    # Calculate the number of portions needed for all pigeons after m minutes
    #s = 1*1 + (1*2 + 2*1) + (1*3 + 2*2 + 3*1) + (1*4 + 2*3 + 3*2 + 4*1) + ... + (1*m + 2*(m-1) + 3*(m-2) + ... + m*(m-(m-1)))
    
    # m = minute
    m = 400
    
    food_eaten_in_every_minute = {m : sum([m for m in range(1, m+1)]) for m in range(1, m+1)}
    print(f'food_eaten_in_every_minute = {food_eaten_in_every_minute}')
    
    portions_needed_total = {m : sum([sum([m for m in range(1, m+1)]) for m in range(1, m+1)]) for m in range(1, m+1)}
    print(f'portions_needed_total = {portions_needed_total}')
    
    pigeons = {m : sum([m for m in range(1, m+1)]) for m in range(1, m+1)}
    print(f'pigeons = {pigeons}')
    
    # calculate the total number of portions needed for all pigeons in the minute when the given portions are eaten
    for value in portions_needed_total.values():
        print(f'potions = {value} comparing with number = {number}')
        if value >= number:
            portions_needed = value
            print(f'portions_needed = {portions_needed}')
            break
    
    # calculate the minute when all the portions are eaten
    for key, value in portions_needed_total.items():
        if value == portions_needed:
            minute = key
            
    print(f'minute = {minute}')
        
    # calculate the number of pigeons in that minute
    nr_of_pigeons = pigeons[minute]
    print(f'nr_of_pigeons = {nr_of_pigeons}')
        
    remaining_portions = number - portions_needed_total[minute-1] if minute >1 else number
    print(f'remaining_portions = {remaining_portions}')
    
    pigeons_from_before = nr_of_pigeons - minute
    
    if remaining_portions < pigeons_from_before:
        print(f'result=pigeons_from_before = {pigeons_from_before}')
        return pigeons_from_before
    else:
        print(f'remaining_portions = {remaining_portions}')
        return  remaining_portions



# Best Solution: 
# https://py.checkio.org/mission/feed-pigeons/publications/bourbaka/python-3/first/share/a957b336ca5c3e6e18b60038255bde58/

def checkio_(number):
    pigeons = 0    
    i = 1
    while True:
        if number <= pigeons:
            return pigeons
        pigeons += i
        if number < pigeons:
            return number     
        number -= pigeons
        i += 1
        
        
# Recursion Solution
# https://py.checkio.org/mission/feed-pigeons/publications/caynan/python-3/recursion/?ordering=most_voted&filtering=all

def checkio_(n, pigeon = 1, last = 0):
    if n <= last:
        return last
    if n <= pigeon:
        return n
        
    return checkio(n - pigeon, 2 * pigeon - last + 1, pigeon)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
    assert checkio(18) == 8, "4th example"
    
    print('Done!!!')