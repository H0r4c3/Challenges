'https://py.checkio.org/en/mission/parse-array/'

'''
In this task you you already have the solution. 
The problem is that it has a bug and you must try to find and fix it. " import ", " exec " and " eval " don't work for this task.

You are given a string that contains a list with integers or nested lists. 
The integers could have single plus or minus sign before them. 
If the input string does not contain an array, then raise ValueError . 
For an incorrectly formatted string -- raise ValueError . 
Elements of the array are separated by commas.

Input: A string.

Output: The list with nested lists or integers.
'''
WHITESPACE_STR = ' \t\n\r'

def parse_array_(s, _w=WHITESPACE_STR, _sep=","):
    print(eval(s))
    return(eval(s))

def parse_array(s):
    print(eval(s))
    return(eval(s))
    
    


# Best Solution:
# https://py.checkio.org/mission/parse-array/publications/Sim0000/python-3/first/share/e87a3c6d1608a8ce3673a6f4585be966/

WHITESPACE_STR = ' \t\n\r'


def parse_array(s, _w=WHITESPACE_STR, _sep=","):
    array = None
    stack = []
    accumulator = ""
    closed_flag = False
    sep_flag = False
    whitespace_flag = False
    started_flag = False
    for ch in s:
        if ch in _w:
            whitespace_flag = True
            continue
        if ch == "[":
            if started_flag and not stack:
                raise ValueError("Wrong string.")
            if closed_flag or accumulator:
                raise ValueError
            in_array = []
            if stack:
                stack[-1](in_array)
            else:
                array = in_array
                started_flag = True
            stack.append(in_array.append)
        elif not started_flag:
            raise ValueError("Wrong string.")
        elif ch == "]":

            if not stack:
                raise ValueError("Wrong string.")
            if accumulator:
                stack[-1](int(accumulator))
                accumulator = ""
            stack.pop()
            closed_flag = True
            sep_flag = False
            whitespace_flag = False
        elif ch in _sep:
            if accumulator:
                stack[-1](int(accumulator))
                accumulator = ""
            elif closed_flag:
                pass
            else:
                raise ValueError("Wrong string.")
            sep_flag = True
            closed_flag = False
            whitespace_flag = False
        else:
            if whitespace_flag and accumulator or closed_flag:
                raise ValueError
            accumulator += ch
        whitespace_flag = False
    if not array is None and not stack and not sep_flag:
                        ###############################
        return array
    else:
        raise ValueError("Wrong string")



    try:
        parse_array("[asd]")
        assert False, "Only integers"
    except ValueError:
        pass

    try:
        parse_array("[2, 3]]")
        assert False, "Excess bracket"
    except ValueError:
        pass

    try:
        parse_array("[++2, 1]")
        assert False, "Two plus"
    except ValueError:
        pass

    try:
        parse_array("[10, 11, , 12]")
        assert False, "Two separators"
    except ValueError:
        pass

    try:
        parse_array(" 13 ")
        assert False, "Where is a list?"
    except ValueError:
        pass

    try:
        parse_array("[[2]")
        assert False, "Excess opened bracket"
    except ValueError:
        pass

    try:
        parse_array("[3 4]")
        assert False, "Check for spurious spaces within a number"
    except ValueError:
        pass

    try:
        parse_array("[10, 11,, 12]")
        assert False, "Check for double separators without a space in between"
    except ValueError:
        pass

    try:
        parse_array("[[]3]")
        assert False, "Check for missing separators after []"
    except ValueError:
        pass

    try:
        parse_array("[2[]]")
        assert False, " Check for missing separators before []"
    except ValueError:
        pass

    try:
        parse_array("[3],")
        assert False, "Excess separator"
    except ValueError:
        pass

    try:
        parse_array("[1,2]3")
        assert False, "Excess number"
    except ValueError:
        pass

    try:
        parse_array("[1], [2,3]")
        assert False, "Here should be only one array."
    except ValueError:
        pass


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert parse_array("[1, 2, 3]") == [1, 2, 3], "Simple"
    assert parse_array("[[1], 2, 3]") == [[1], 2, 3], "Nested"
    assert parse_array("[-3, [-2, 0], 10]") == [-3, [-2, 0], 10], "Negative integers"
    assert parse_array("[100]") == [100], "One number"
    assert parse_array("[2,     3]") == [2, 3], "Whitespaces"
    assert parse_array("[[10, [11]], [[[1], 2], 3], 5]") == [[10, [11]], [[[1], 2], 3], 5], "Deep nested"
    assert parse_array("   [3, 4]   ") == [3, 4], "Skip whitespaces"
    assert parse_array("[[], 0]") == [[], 0], "Empty arrays"
    assert parse_array("[[0,], 0]") == [[0], 0], "Comma - closed bracket"
    print('Done!!!')

    