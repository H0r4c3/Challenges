def decor(func):
    
    def wrap():
        print("============")
        func()
        print("============")
    
    return wrap

@decor
def print_text():
    print("Hello, world!")

print_text()
#decorated = decor(print_text)
#decorated()

def decor1(func):
    def wrap1(x):
        print('***')
        func(x)
        print('***')
        print('END OF PAGE')
    return wrap1

import re

def find_identical_consecutive_chars(string):
    pattern = r'(.)\1+'
    matches = re.findall(pattern, string)
    return matches

# Example usage:
s = "aaabbcccdddeeeee"
result = find_identical_consecutive_chars(s)
print(result)

print([1, 2, 4].reverse())


def func(x=[ ]):
    x.append(1)
    return x

print(func(), end= ' ')
print(func(), end= ' ')
print(func())