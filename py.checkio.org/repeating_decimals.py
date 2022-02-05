'https://py.checkio.org/en/mission/repeating-decimals/'

'''
You should write a function for the converting a fraction into decimal representation. 
If the decimal is repeating, you should represent it using the brackets format seen above. 
You are given two integers, the first is the fractions numerator and the second is its denominator. 
For this task, you will need to return the fraction in decimal representation as a string. 
The integer results (as 0 or 2) must be ended with a dot.

Input: Two arguments. A numerator and a denominator as integers.

Output: The decimal representation of the fraction in the bracket format as a string.
'''

def convert(numerator, denominator):
    decimal_repeat = ''
 
    # the position of the remainder in decimal_repeat
    rem_position = {}
 
    # if numerator == 0:
    #     print('0.')
    #     return '0.'
    
    rem = numerator % denominator
    
    if rem == 0:
        result = str(numerator // denominator) + '.'
        print(result)
        return result
 
    while ((rem != 0) and (rem not in rem_position)):
 
        rem_position[rem] = len(decimal_repeat)
        rem = rem * 10
        res_part = rem // denominator
        decimal_repeat += str(res_part)
        rem = rem % denominator
 
    if rem == 0:
        print('None')
        return str(numerator / denominator)
    else:
        result = str(numerator // denominator) + '.' + str(decimal_repeat[ : rem_position[rem]]) + '(' + str(decimal_repeat[rem_position[rem] : ]) + ')'
        print(result)
        return result


def convert_(numerator, denominator):
    number, decimals = str(numerator // denominator), ""
    remainder , remainders = numerator % denominator, []
    while remainder and remainder not in remainders:
        decimals = decimals + str(10 * remainder // denominator) 
        print(decimals)
        remainders.append(remainder)
        remainder = 10 * remainder % denominator
    repeat = remainders.index(remainder) if remainder in remainders else -1
    if repeat + 1: 
        decimals = decimals[:repeat] + "(" + decimals[repeat:] + ")"
    print(decimals[:repeat])
    return number + '.' + decimals


# https://www.geeksforgeeks.org/find-recurring-sequence-fraction/
def convert_(numerator, denominator):
 
    # Initialize result
    res = ""
 
    # Create a map to store already seen
    # remainders. Remainder is used as key
    # and its position in result is stored
    # as value. Note that we need position
    # for cases like 1/6.  In this case,
    # the recurring sequence doesn't start
    # from first remainder.
    mp = {}
 
    # Find first remainder
    rem = numerator % denominator
 
    # Keep finding remainder until either
    # remainder becomes 0 or repeats
    while ((rem != 0) and (rem not in mp)):
 
        # Store this remainder
        mp[rem] = len(res)
 
        # Multiply remainder with 10
        rem = rem * 10
 
        # Append rem / denominator to result
        res_part = rem // denominator
        res += str(res_part)
 
        # Update remainder
        rem = rem % denominator
 
    if (rem == 0):
        return ""
    else:
        print(res[mp[rem]:])
        return res[mp[rem]:]
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
    assert convert(1, 97) == "0.(010309278350515463917525773195876288659793814432989690721649484536082474226804123711340206185567)", "96 repeated digits"
    assert convert(4,2) == "2."
