'https://py.checkio.org/en/mission/long-repeat-inside/'

'''
You should find a repeating sequence inside the substring. 
I have an example for you: in a string "abababc" - "ab" is a sequence that repeats more than once, so the answer will be "ababab"
'''

# My Solution
def repeat_inside(line):
    """
        first the longest repeating substring
    """
    print(f'line = {line}')
    
    # create a list with all possible substrings
    all_substrings = [line[i:j] for i in range(len(line)) for j in range(i+1, len(line) + 1)]
    print(f'all_substrings = {all_substrings}')
    
    # create a dictionary having keys = the substrings and values = the repetitions
    subs_dict = {item:line.count(item) for item in all_substrings if line.count(item) > 1}
    print(f'subs_dict = {subs_dict}')
    if subs_dict == {}:
        return ''
    
    # create a new dictionary checking if the multiplied substring is in 'line'
    for key, value in subs_dict.items():
        for i in range(value, 0, -1):
            if key*i in line:
                subs_dict[key] = i
                print('break')
                break
                
    print(subs_dict)
    print(subs_dict.items())

    # create a list of tuples of substrings and repetitions
    # sort the list after the length of (string*repetitions)
    sorted_subs = sorted(subs_dict.items(), key=lambda x : len(x[1]*x[0]), reverse=True)
    print(f'sorted_subs = {sorted_subs}')
    
    # result = the first item in the sorted list multiplied with repetitions
    print(f'result = {sorted_subs[0][0]*sorted_subs[0][1]}')
    return sorted_subs[0][0]*sorted_subs[0][1]



# BEST Solution
# https://py.checkio.org/mission/long-repeat-inside/publications/Moff/python-3/first/share/9810391444f3214c8dc6e8c2693456a8/
def repeat_inside_(line):
    result = ''
    for i in range(len(line)):
        for j in range(len(line) - i):
            s = line[i : i + j + 1]
            for k in range(2, len(line) // len(s) + 1):
                ls = s * k
                if ls in line and len(ls) > len(result):
                    result = ls
    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    assert repeat_inside("rghtyjdfrtdfdf56r") == 'dfdf'
    print('"Run" is good. How is "Check"?')