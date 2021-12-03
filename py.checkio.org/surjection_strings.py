'https://py.checkio.org/en/mission/isometric-strings/'

'''
You need to check that the 2 given strings are isometric. This means that a character from one string can become a match for characters from another string.

One character from one string can correspond only to one character from another string. 
Two or more characters of one string can correspond to one character of another string, but not vice versa.
'''

def isometric_strings(a, b):
    my_zip = list(zip(a, b))
    my_set = set(my_zip)
    
    if len(set(a)) == len(my_set):
        return True
    else:
        return False


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False