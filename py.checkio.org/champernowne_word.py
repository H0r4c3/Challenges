'https://py.checkio.org/en/mission/champernowne-word/share/ad6c733a81de9b88fca82d423e09ce27/'

'''
The Champernowne word 1234567891011121314151617181920212223…, also known as the counting series, 
is an infinitely long string of digits made up of all positive integers written out in ascending order without any separators. 
This function should return the digit at position n of the Champernowne word. Position counting again starts from zero.
'''

import time

def counting_series(n: int) -> int:
    start_time = time.time()
    
    big_string = '1'
    number = 1
    while len(big_string) < n+1:
        number += 1
        big_string += str(number)
        #print(big_string)
    
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    
    return int(big_string[n])


# Best Solution: https://py.checkio.org/mission/champernowne-word/publications/kdim/python-3/generator/?ordering=most_voted&filtering=all

def counting_series_(n: int) -> int:
    def barbier(k=0):
        while True:
            k += 1
            yield from map(int, str(k))

    number = barbier()
    while n > 0:
        n -= 1
        next(number)
    return next(number)


# Another Best Solution: https://py.checkio.org/mission/champernowne-word/publications/Tinus_Trotyl/python-3/first/?ordering=most_voted&filtering=all

def counting_series(n: int) -> int:
    champword, count = "", 1
    while len(champword) < n + 1:
        champword, count = champword + str(count), count + 1
    return int(champword[n])


print("Example:")
#print(counting_series(1))

# These "asserts" are used for self-checking
assert counting_series(0) == 1
assert counting_series(10) == 0
assert counting_series(33) == 2
assert counting_series(100) == 5
assert counting_series(10000) == 7
assert counting_series(1000000) == 8
assert counting_series(10000000) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")