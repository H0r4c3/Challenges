'https://py.checkio.org/en/mission/right-to-left/'

'''
You are given a sequence of strings. You should join these strings into a chunk of text where the initial strings are separated by commas. 
As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. 
All strings are given in lowercase.
'''

def left_join(phrases: tuple) -> str:
    """
    Join strings and replace "right" to "left"
    """
    phrases_list = list()
    for item in phrases:
        if 'right' not in item:
            phrases_list.append(item)
        else:
            new_left = item.replace('right', 'left')
            phrases_list.append(new_left)
    result = ','.join(phrases_list)
    
    return result


# Best Solution: 
# https://py.checkio.org/mission/right-to-left/publications/mr.floppy/python-3/first/?ordering=most_voted&filtering=all

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return (",".join(phrases)).replace("right","left")


if __name__ == "__main__":
    print("Example:")
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    ), "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"