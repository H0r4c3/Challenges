'https://py.checkio.org/en/mission/the-fastest-horse/'

'''
We have some horse racing statistics (each horse’s time in each race)
You have to find the number of the horse which has the most wins.

Input: Racing time as an array of arrays.

Output: The number of the fastest horse that has the most wins (Important: in this task the horse numbers starts from "1", not from "0")
'''


def fastest_horse(horses: list) -> int:
    results = list()
    for i in horses:
        results.append(i.index(min(i)))
        
    result = max(results, key=results.count)
    
    print(result+1)
    return(result+1)
    


# Best Solution: 
# https://py.checkio.org/mission/the-fastest-horse/publications/novelworm/python-3/first/share/cafb17156972d642667a0256a1484abd/

def fastest_horse_(horses: list) -> int:
    res = [i.index(min(i)) + 1 for i in horses]
    return max(res, key=res.count)



if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    assert fastest_horse([["1:10","1:15","1:20"],["1:05","1:10","1:15"],["2:59","2:59","2:59"]]) == 1
    assert fastest_horse([["1:55","1:50","1:45","1:40","1:35"],["2:55","2:50","2:45","2:40","2:35"],["3:55","3:50","3:45","3:40","3:35"],["4:55","4:50","4:45","4:40","4:35"],["3:55","3:50","3:45","3:40","3:35"],["2:35","2:40","2:45","2:50","2:55"]]) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")