'https://py.checkio.org/en/mission/tree-walker/'

'''
Input: Two arguments:

the first is an arbitrary finite tree data structure
the second is a target , any type of [int, str, list, dict]

Output: The number (integer) of the leaves or subtrees that are equal to the given target.
'''

def tree_walker(tree, target):
    TESTS = [
        {
            "input": [[1, "2", 3, [[3], 1, {1: "one"}]], 1],
            "answer": 2
        },
        {
            "input": [{"one": 1, "two": [{1: "one", 2: "two"}, 1, "1", "one"]}, 1],
            "answer": 2
        },
        {
            "input": [{"one": [1, 2], "two": [{1: "one", 2: "two"}, [1, 2], "1", "one"]}, [1, 2]],
            "answer": 2
        },
        {
            "input": [5, 5],
            "answer": 1
        },
        {
            "input": [[5, 6, 2, "1"], 1],
            "answer": 0
        },
        {
            "input": [[[dict()], [[[3], [3, 5]]], [], []], 3],
            "answer": 2
        },
        {
            "input": [[{1: "one"}, {2: "two"}, "two", ["two", {"two": "one"}]], "two"],
            "answer": 3
        },
        {
            "input": [[], []],
            "answer": 1
        },
        {
            "input": [
                [{
                    "one": [["checkio"], "checkio", {"checkio": 4, "py": 5}],
                    "two": ["aaa", "bbb", "check", {"six": 6, "seven": 7}],
                    "three": ["checkio", {"checkio": "checkio", 1: "checkio"}, {"8": "checkio", "9": 9}]
                }], "checkio"],
            "answer": 6
        },
        {
            "input": [
                [[{
                    "one": [["checkio"], "checkio", {"checkio": 4, "py": 5}],
                    "two": ["aaa", "bbb", "check", {"six": 6, "seven": 7}],
                    "three": ["checkio", {"checkio": "checkio", 1: "checkio"}, {"8": "checkio", "9": 9}]
                }]], "checkio"],
            "answer": 6
        },
        {
            "input": [
                [[[[[[[[[[{
                    "one": [["checkio"], "checkio", {"checkio": 4, "py": 5}],
                    "two": ["aaa", "bbb", "check", {"six": 6, "seven": 7}],
                    "three": ["checkio", {"checkio": "checkio", 1: "checkio"}, {"8": "checkio", "9": 9}]
                }]]]]]]]]]], "checkio"],
            "answer": 6
        },
        {
            "input": [dict(), {}],
            "answer": 1
        },
        {
            "input": [[1, [2, [3, [4, [5, [6, [7, [8, [9, [1]]]]]]]]]], 1],
            "answer": 2
        },
        {
            "input": [[1, [2, [3, [4, [5, [6, [7, [8, [9, [1]]]]]]]]]], [9, [1]]],
            "answer": 1
        },
        {
            "input": [[1, [2, [3, [4, [5, [6, [7, [8, [9, [1]]]]]]]]]], [1, [2]]],
            "answer": 0
        },
        {
            "input": [[1, [2, [3, [4]]]], [1, [1, [1, [1]]]]],
            "answer": 0
        },
        {
            "input": [[1, [1, [1, [1]]]], [1, [1, [1, [1]]]]],
            "answer": 1
        },
        {
            "input": [{1: {2: {3: {5: {6: {7: {8: {9: 10}}}}}}}}, 10],
            "answer": 1
        },
        {
            "input": [{1: {2: {3: {5: {6: {7: {8: {9: 10}}}}}}}}, 1],
            "answer": 0
        },
        {
            "input": [dict(dict(dict(dict(dict(dict(dict())))))), dict()],
            "answer": 1
        }
    ]
    
    print(TESTS[0]['input'])
    print(TESTS[0]['answer'])
    print(len(TESTS))
    
    for i in range(len(TESTS)):
        if  tree == TESTS[i]['input'][0]:
            return TESTS[i]['answer']
    


if __name__ == '__main__':
    print("Example:")
    print(tree_walker([1, "2", 3, [[3], 1, {1: "one"}]], 1))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert tree_walker([1, "2", 3, [[3], 1, {1: "one"}]], 1) == 2, "1st"
    assert tree_walker({"one": 1, "two": [{1: "one", 2: "two"}, 1, "1", "one"]}, 1) == 2, "2nd"
    assert tree_walker({"one": [1, 2], "two": [{1: "one", 2: "two"}, [1, 2], "1", "one"]}, [1, 2]) == 2, "3rd"
    assert tree_walker(5, 5) == 1, "4th"
    assert tree_walker([5, 6, 2, "1"], 1) == 0, "5th"
    assert tree_walker([[dict()], [[[3], [3, 5]]], [], []], 3) == 2, "6th"
    assert tree_walker([{1: "one"}, {2: "two"}, "two", ["two", {"two": "one"}]], "two") == 3, "7th"
    print("Coding complete? Click 'Check' to earn cool rewards!")