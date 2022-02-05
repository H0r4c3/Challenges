'https://py.checkio.org/en/mission/digits-doublets/'

'''
You are given the list of numbers with exactly the same length and you must find the shortest chain of numbers to link the first number to 
the last like you would with the words.

For Example. There is a list [123, 991, 323, 321, 329, 121, 921, 125, 999]. The shortest way from the first to the last is: 123 ⇒ 121 ⇒ 921 ⇒ 991 ⇒ 999

You should write a function that receives a list of numbers (positive integers) and returns the shortest route as a list of numbers.

Input: Numbers as a list of integers.

Output: The shortest chain from the first to the last number as a list of integers.
'''

def checkio(numbers):
    start = str(numbers[0])
    end = str(numbers[-1])
    list_numbers = list(map(str, numbers))
    
    def common_2_letters(string1, string2):
        common_letters = [letter1 for letter1, letter2 in zip(string1, string2) if letter1==letter2]
        
        if len(common_letters) == 2:
            return string2
      
        
    def common_list(string2, list_numbers): 
        result = [common_2_letters(string2, number) for number in list_numbers if common_2_letters(string2, number) != None]
        return result
    
    
    result1 = common_list(start, list_numbers.remove(start))
    print(result1)
    
    num = result1.pop(0)
    print(num)
    result2 = common_list(num, list_numbers.remove(num))
    print(result2)
    
    num = result1.pop(1)
    print(num)
    result3 = common_list(num, list_numbers.remove(num))
    print(result3)
    
    return result2

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"