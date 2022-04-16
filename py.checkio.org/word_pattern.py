'https://py.checkio.org/en/mission/word-pattern/'

'''
You are given a pattern as a positive integer and a command as a word. 
For the comparison, the drone should convert the integer pattern into binary form, append zeros to left for 
the command length and compare this combination with the command.
1 is a letter. 0 is a digit.
If the pattern and the command are coincided, then return True, else -- False. 
If pattern is longer than a command, then they are not coincided (For example - 8 = 1000 and "a").
'''

import re

def check_command(pattern, command):
    pattern_bin = bin(pattern)[2:]
    
    if len(pattern_bin) > len(command):
        return False
    
    # Add 0s to the left of the pattern_bin
    new_pattern_bin = '0' * (len(command) - len(pattern_bin)) + pattern_bin
    print(new_pattern_bin)
    
    # Replace digits with 0 and non-digits with 1
    command_bin = re.sub('\d', '0', command)
    command_bin = re.sub('\D', '1', command_bin)
    print(command_bin)
    
    return new_pattern_bin == command_bin


# Best Solution: 
# https://py.checkio.org/mission/word-pattern/publications/tom-tom/python-3/one/?ordering=most_voted&filtering=all

def check_command(pattern, command):
    '''
    Converts the 'command' string, from binary to decimal number
    '''
    return pattern == int(''.join('0' if c.isdigit() else '1' for c in command), 2)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_command(42, "12a0b3e4") == True, "42 is the answer"
    assert check_command(101, "ab23b4zz") == False, "one hundred plus one"
    assert check_command(0, "478103487120470129") == True, "Any number"
    assert check_command(127, "Checkio") == True, "Uppercase"
    assert check_command(7, "Hello") == False, "Only full match"
    assert check_command(8, "a") == False, "Too short command"
    assert check_command(5, "H2O") == True, "Water"
    assert check_command(42, "C2H5OH") == False, "Yep, this is not the Answer"
    print('Done!!!')