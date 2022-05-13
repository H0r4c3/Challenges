'https://py.checkio.org/en/mission/the-secret-room/'

'''
As input your function will receive an integer - the total number of doors in the current room. 
You will need to sort the door numbers in the order in which these numbers, expressed in words, go in the alphabetical order. 
And then return the position number of the last door (the door with the highest number). The count starts from the 1st position (not from the 0th). 
The maximum number of doors is 1000. The numbers after 100 are written in the format like - 'one hundred twenty nine'.
'''
def number_2_word(n):
    digits_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
 
    if n==0:
        return ""
     
    else:
        # compute spelling for the last digit
        small_ans = digits_list[n % 10]
 
        # keep computing for the previous digits and add the spelling for the last digit
        ans = number_2_word(int(n/10)) + small_ans + " "
     
    return ans



# My Solution using num2words module
import num2words
def secret_room_(number):
    words_dict = dict()
    for nr in range(1, number+1):
        words = num2words.num2words(nr).replace('-', ' ')
        words_dict[nr] = words
    print(words_dict)
    
    words_dict_sorted = sorted(words_dict.items(), key = lambda x: x[1])
    words_dict_sorted = {key : value for key, value in words_dict_sorted}
    print(words_dict_sorted)
    
    # search for the position of 'number' in words_dict_sorted
    result = list(words_dict_sorted.keys()).index(number) + 1
    
    print(result)
    return result



# Another Solution
def convert(num):
    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens = ("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if num < 0:
        return "minus "+ convert(-num)

    if num < 20:
        return  units[num] 

    if num < 100:
        return  tens[num // 10]  + units[int(num % 10)] 

    if num < 1000:
        return units[num // 100]  + "hundred " +convert(int(num % 100))

    if num < 1000000: 
        return  convert(num // 1000) + "thousand " + convert(int(num % 1000))

    if num < 1000000000:    
        return convert(num // 1000000) + "million " + convert(int(num % 1000000))

    return convert(num // 1000000000) + "billion " + convert(int(num % 1000000000))

def secret_room(number):
    words_dict = dict()
    for nr in range(1, number+1):
        words = convert(nr)
        words_dict[nr] = words
    print(words_dict)
    
    words_dict_sorted = sorted(words_dict.items(), key = lambda x: x[1])
    words_dict_sorted = {key : value for key, value in words_dict_sorted}
    print(words_dict_sorted)
    
    # search for the position of 'number' in words_dict_sorted
    result = list(words_dict_sorted.keys()).index(number) + 1
    
    print(result)
    return result



# Best Solution: 
# https://py.checkio.org/mission/the-secret-room/publications/Phil15/python-3/sum-bool/share/742db8081375f73c7130d480e5989528/

BELOW_20 = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
            'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
            'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def word(nb):
    """Write numbers 1 to 1000 in words (and 0 --> '')."""
    if 0 <= nb < 20:
        res = [BELOW_20[nb]]
    elif 20 <= nb < 100:
        tens, below_ten = divmod(nb, 10)
        res = [TENS[tens - 2], BELOW_20[below_ten]]
    elif 100 <= nb < 1000:
        hundreds, below_hundred = divmod(nb, 100)
        res = [BELOW_20[hundreds], 'hundred', word(below_hundred)]
    else:
        res = ['one', 'thousand']
    return ' '.join(elem for elem in res if elem) # remove possible None / 0.

secret_room_ = lambda door: sum(word(nb) < word(door) for nb in range(door))




if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1 #five, four, one, three, two
    assert secret_room(3) == 2 #one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")