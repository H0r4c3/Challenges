'https://py.checkio.org/en/mission/letter-queue/'

'''
We will emulate the queue process with Python. You are given a sequence of commands:
- "PUSH X" -- enqueue X , where X is a letter in uppercase.
- "POP" -- dequeue the front position. if the queue is empty, then do nothing.
The queue can only contain letters.
'''

from typing import List

def letter_queue_(commands: List[str]) -> str:
    queue = list()
    for item in commands:
        if "PUSH" in item:
            queue.append(item[-1])
        if ("POP" in item) and len(queue):
            del queue[0]
            
    return "".join(queue)



# Another Solution (not allowed on checkio!!!)
from queue import Queue
def letter_queue(commands: List[str]) -> str:
    my_queue = Queue()
    for item in commands:
        if "PUSH" in item:
            my_queue.put(item[-1])
        if ("POP" in item) and my_queue.qsize():
            my_queue.get()
            
    print(my_queue.queue)
    
    return "".join(my_queue.queue)


# Best Solution:
# https://py.checkio.org/mission/letter-queue/publications/veky/python-3/double-ended/?ordering=most_voted&filtering=all

import collections
def letter_queue(commands):
    queue = collections.deque()
    for command in commands:
        if command.startswith("PUSH"):
            queue.append(command[-1])
        elif queue:
            queue.popleft()            
    return "".join(queue)
    





# Best Solution: 
# https://py.checkio.org/mission/letter-queue/publications/bravebug/python-3/first/share/71bdef9f59c3e9539d334566658f18f6/

def letter_queue_(commands):
    result = []
    for command in commands:
        if "PUSH" in command:
            result.append(command[-1])
        if "POP" in command and len(result):
            result.pop(0)
    return "".join(result)


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")