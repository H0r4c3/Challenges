'https://py.checkio.org/en/mission/beat-the-previous/share/79c495d0677206e658b6edbefbc37bf9/'

'''
Given a string of digits guaranteed to only contain ordinary integer digit characters 0 to 9, create and return the list of increasing 
integers acquired from reading these digits in order from left to right. The first integer in the result list is made up from the first 
digit of the string. After that, each element is an integer that consists of as many following consecutive digits as are needed to make 
that integer strictly larger than the previous integer.
'''

def beat_previous(digits: str) -> list[int]:
    bigger = digits[0]
    result = [int(bigger)]
    digits = digits.replace(bigger, '', 1)
    # create a list of following consecutive digits
    fcd = [int(digits[0 : end]) for end in range(1, len(digits) + 1)]
    
    i = 0
    
    while i < len(fcd):
        if fcd[i] > int(bigger):
            bigger = fcd[i]
            result.append(bigger)
            digits = digits.replace(str(bigger), '', 1)
            fcd = [int(digits[0 : end]) for end in range(1, len(digits) + 1)]
        else:
            i+=1
            
    print(result)
    return result


print("Example:")
#print(beat_previous("123"))

# These "asserts" are used for self-checking
assert beat_previous("654321") == [6, 54, 321]
assert beat_previous("600005") == [6]
assert beat_previous("6000050") == [6, 50]
assert beat_previous("045349") == [0, 4, 5, 34]
assert beat_previous("77777777777777777777777") == [7, 77, 777, 7777, 77777, 777777]

print("The mission is done! Click 'Check Solution' to earn rewards!")

