'https://py.checkio.org/en/mission/the-best-number-ever/'

'''
You can return any number, but use the code to prove your number is the best!

Let's write an essay in python code which will explain why is your number is the best. 
Publishing the default solution will only earn you 0 points as the goal is to earn points through votes for your code essay.
'''

def checkio():
    ''''The best number is 2766 because is the ACE'''
    hex = '0x' + 'ace'
    result = int(hex, 16)
   
    print(result)
    return result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio(), (int, float, complex))
    print('Done!!!')

