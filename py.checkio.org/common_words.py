'https://py.checkio.org/en/mission/common-words/'

'''
Let's continue examining words. You are given two strings with words separated by commas. 
Try to find what is common between these strings. The words in the same string don't repeat.

Your function should find all of the words that appear in both strings. 
The result must be represented as a string of words separated by commas in alphabetic order.

Input: Two arguments as strings.

Output: The common words as a string.
'''

# Method using lists
def checkio_1(line1: str, line2: str) -> str:
    common_words = list()
    
    for item in line1.split(','):
        if item in line2.split(','):
            common_words.append(item)
    
    common_words = sorted(common_words)     
    result = ','.join(common_words)
         
    return result

# Method using sets
def checkio(line1: str, line2: str) -> str:
    common_words = list()
    common_words = set(line1.split(',')).intersection(set(line2.split(',')))
    common_words = sorted(list(common_words))
    result = ','.join(common_words)
         
    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))
    print(checkio('one,two,three', 'four,five,one,two,six,three'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three', 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")