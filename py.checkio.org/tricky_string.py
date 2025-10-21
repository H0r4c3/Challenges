'https://py.checkio.org/en/mission/tricky-string/share/bd1f7136e7b118a9827fd551b7ece737/'

'''
You are given a string. Somewhere in that text a word "CheckIO" has hidden. 
Your task is to find a place where word is hiding and make the minimum number of replacements to get it. 
Let's proceed with an example: for a string "xheckIO" you should replace only one symbol ("x" to "C") to get a desired word, 
on the other hand we can try to find it in more complex string: "CheckzzVSCheckIz", right answer here will be a string "CheckzzVSCheckIO" 
(only one replacement has made "z" to "O").

Every string contains at least one of seven characters of the word "CheckIO" and there are enough symbols around it to obtain the necessary word.
If there are several ways to complete the task, just put the word in the first suitable place for that.
'''

#1. Solution
def tricky_string_(word):
    target = "CheckIO"
    candidates = []

    # Iterate through the positions where "CheckIO" might start
    for i in range(len(word) - len(target) + 1):
        candidate = word[:i] + target + word[i + len(target):]
        replacements = sum(c1 != c2 for c1, c2 in zip(word, candidate))
        candidates.append((replacements, candidate))

    # Find the candidate with the minimum number of replacements
    min_replacements, result = min(candidates, key=lambda x: x[0])

    return result

#2. Solution

import re

def tricky_string(text):
    word = 'CheckIO'
    pattern = re.compile(r'(?i)([checkio]+)', re.IGNORECASE)
    match = pattern.search(text)
    print(match)
    if match:
        start, end = match.span()
        print(match.span())
        result = text[:start] + word + text[end:]
        print(result)
        return result
    else:
        return word
    
#3. Solution 
# https://py.checkio.org/mission/tricky-string/publications/Kolia951/python-3/regex-solves-charades/?ordering=most_voted&filtering=all#comment-125126

import re

def tricky_string(text: str) -> str:
    # masks for every symbol in the "CheckIO"
    masks = [
        "[Cc].{6}", ".{1}[Hh].{5}", ".{2}[Ee].{4}", ".{3}[Cc].{3}",
        ".{4}[Kk].{2}", ".{5}[Ii].{1}", ".{6}[Oo]"
    ]
    matchings = []
    # apply masks and check the difference
    for item in masks:
        res = re.findall(item, text)
        # verify every found substring against "CheckIO"
        for substring in res:
            gaps = zip("CheckIO", substring)
            # count number of different symbols
            gaps_count = sum([1 for i,j in gaps if i != j])
            # add all of them into the list
            elem = (gaps_count, text.find(substring))
            matchings.append(elem)
    # find an element with the min differense with "CheckIO"
    position = min(matchings)[1]
    # create a final string
    final_result = text[:position] + "CheckIO" + text[position + 7:]
    return final_result
    

print("Example:")
#print(tricky_string("Checkio"))

# These "asserts" are used for self-checking
assert tricky_string("checkIO") == "CheckIO"
assert tricky_string("zcheckzz") == "zCheckIO"
assert tricky_string("SoManyChoicesHere") == "SoManyCheckIOHere"

print("The mission is done! Click 'Check Solution' to earn rewards!")