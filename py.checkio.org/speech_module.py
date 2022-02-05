'https://py.checkio.org/en/mission/speechmodule/'

'''
All the words in the string must be separated by exactly one space character. 
Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.

Output: The string representation of the number as a string.
'''

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

from num2words import num2words
def checkio(number):
    result = num2words(number)
    result = result.replace('-', ' ').replace('and', '').replace('  ', ' ')
    print(result)
    
    return result




def checkio(number):
    #global result
    result = []
    def three_digits(number):
        result.append(FIRST_TEN[(number // 100) - 1])
        result.append(HUNDRED)
        number = number % 100
        return number
    
    def two_digits_20(number):
        result.append(OTHER_TENS[(number // 10) - 2])
        number = number % 10
        return number
        
    def two_digits_10(number):
        result.append(SECOND_TEN[number - 10])
        number = 0
        return number
        
    def one_digit(number):
        result.append(FIRST_TEN[number - 1])
        return number
        
    if 100 <= number < 1000:
        number = three_digits(number)
    if 20 <= number <= 99:
        number = two_digits_20(number)
    elif 10 <= number <= 19:
        number = two_digits_10(number)
    if 1 <= number <= 9:
        number = one_digit(number)

    return ' '.join(result)



# Best Solution: https://py.checkio.org/mission/speechmodule/publications/makoto_yamagata/python-3/first/?ordering=most_voted&filtering=all

def checkio(number):

    n = number // 100
    t = [FIRST_TEN[n-1], HUNDRED] if n > 0 else []

    n = (number // 10) % 10
    t += [OTHER_TENS[n-2]] if n > 1 else []

    n = number % (10 if n > 1 else 20)
    t += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []

    return ' '.join(t)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')