'https://py.checkio.org/en/mission/i-love-python/'

'''
This mission is simple to solve. You are given a function called "i_love_python" which will only return the phrase - "I love Python!"
'''

# My Solution: using dataclass (for level)

from dataclasses import dataclass

def i_love_python():
    """
        Let's explain why do we love Python.
    """
    @dataclass
    class PythonFTW:
        text: str
            
    my_obj = PythonFTW('I love Python!')
    
    print(my_obj.text)
    return (my_obj.text)
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
    print('Done!!!')