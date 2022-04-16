'https://py.checkio.org/en/mission/digit-stack/'

'''
We will emulate the stack process with Python. You are given a sequence of commands:
- "PUSH X" -- add X in the stack, where X is a digit.
- "POP" -- look and remove the top position. If the stack is empty, then it returns 0 (zero) and does nothing.
- "PEEK" -- look at the top position. If the stack is empty, then it returns 0 (zero).
The stack can only contain digits.

You should process all commands and sum all digits which were taken from the stack ("PEEK" or "POP"). Initial value of the sum is 0 (zero).
'''

def digit_stack_(commands):
    my_stack = list()
    result = list()
    for item in commands:
        if 'PUSH' in item:
            my_stack.append(item.split()[-1])
            print(my_stack)
        if 'POP' in item:
            if my_stack != []:
                result.append(my_stack.pop(-1))
        if 'PEEK' in item:
            if my_stack != []: 
                result.append(my_stack[-1])
                       
    print(result)
    return sum(map(int, result))


# OR:
def digit_stack(commands):
    my_stack = list()
    result = list()
    for item in commands:
        if 'PUSH' in item:
            my_stack.append(item.split()[-1])
            print(my_stack)
        if ('POP' in item) and my_stack:
            result.append(my_stack.pop(-1))
        if ('PEEK' in item) and my_stack:
            result.append(my_stack[-1])
                  
    print(result)
    return sum(map(int, result))




if __name__ == '__main__':
    print("Example:")
    print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
    assert digit_stack(["PEEK"]) == 0
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!");