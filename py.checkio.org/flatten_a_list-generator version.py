'https://py.checkio.org/en/mission/flatten-a-list-generator-version/'

'''
There is a list which contains integers or other nested lists which may contain yet more lists and integers which then… you get the idea. 
You should put all of the integer values into one flat list. 
The order should be as it was in the original list with string representation from left to right.
In this mission you should use the 'yield' to make your function a generator.
'''

def flat_list(array):
    def my_generator(array):
        for item in array:
            if isinstance(item, list):
                yield from flat_list(item)
            else:
                yield item
    result = list(my_generator(array))
    print(result)
    return result
    

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')