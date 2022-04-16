'https://py.checkio.org/en/mission/backspace-apply/'

'''
In a given string, replace character '#' with backspace. It means you need to remove the character before '#' (BS) and BS itself. 
The sequence of BSs shows how many chars should be removed before the sequence. 
If there is nothing to remove - only BS should be removed, so the final string has no BSs.
'''

import re
def backspace_apply(val: str) -> str:
    # if '#' not in val:
    #     return val
    
    #s = tuple()
    
    while True:
        #s = re.search('\w#|##|^#|\s#', val)
        s = re.search('.?#', val)
        if s == None:
            return val
        s = s.span()
        val = val[0:s[0]] + val[s[1]:]
        print(s)
        print(val)
        


# Best Solutions:
# https://py.checkio.org/mission/backspace-apply/publications/przemyslaw.daniel/python-3/28-liner-3-easy-examples/?ordering=most_voted&filtering=all

#1.
def backspace_apply_(text: str) -> str:
    result = []
    for char in text:
        if char == "#":
            result = result[:-1]
        else:
            result += [char]            
    return ''.join(result)

#2.
def backspace_apply_(text: str) -> str:
    """ Using regular re library """    
    
    import re
    while "#" in text:
        text = re.sub(r"[^#]#|^#", "", text)
    return text 


print("Example:")
print(backspace_apply("thna#m##e"))

assert backspace_apply("name") == "name"
assert backspace_apply("name#") == "nam"
assert backspace_apply("na##me") == "me"
assert backspace_apply("nam#e#") == "na"
assert backspace_apply("##name") == "name"
assert backspace_apply("name######") == ""
assert backspace_apply("nam######e") == "e"
assert backspace_apply("n###ame") == "ame"
assert backspace_apply("thna#m##e") == "the"
assert backspace_apply("oppo##r##t##u###nity") == "nity"
assert backspace_apply('if you #had o##n##e## shot#### o#r one opp#o##r###tunity') == 'if youh  r onetunity'

print("Not bad! Click 'Check' to earn cool rewards!")