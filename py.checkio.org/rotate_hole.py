'https://py.checkio.org/en/mission/rotate-hole/'

'''
The pipes are numbered from 0 to N-1. The initial positions of the backend mechanism are represented as an array with 1 and/or 0. 
Each element describes a cannon behind the pipe; the 0th element describe 0th pipe. 1 is a working cannon and 0 is a broken cannon.

Input: Two arguments.

A initial state as a list with 1 and/or 0
Pipe numbers for cannonballs as a list of integers

Output: The rotating variants as a list of integers or an empty list.
'''

def rotate(state, pipe_numbers):
    rotations = list()
    pipes_list = list()
    result = list()
    
    # make a list with all rotations of state to the right (with step = 1, step = 2, ..., step = len(state))
    
    # for i in range(len(state)):
    #     state_rotated = state[-i:] + state[:-i]
    #     rotations.append(state_rotated)
    rotations = [state[-i:] + state[:-i] for i in range(len(state))]
    print(rotations)
    
    # make a list with only the items in positions of pipe_numbers
        
    # for item in rotations:
    #     pipes = [item[idx] for idx in pipe_numbers]
    #     pipes_list.append(pipes)
    pipes_list = [[item[idx] for idx in pipe_numbers] for item in rotations]
    print(f'pipes_list = {pipes_list}')
    
    # find the indexes for the tuples with all elements = 1
    # for idx, item in enumerate(pipes_list):
    #     if item[0] == item[1] == 1:
    #         result.append(idx)
    
    result = [idx for idx, item in enumerate(pipes_list) if set(item) == {1}]
    print(result)
    
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    #assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
    print('Done!!!')