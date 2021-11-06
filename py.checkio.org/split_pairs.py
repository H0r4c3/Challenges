'https://py.checkio.org/en/mission/split-pairs/'

'''
Split the string into pairs of two characters. If the string contains an odd number of characters, then the 
missing second character of the final pair should be replaced with an underscore ('_').
'''

def split_pairs(a):
    if a == '':
        return []
    
    my_list = [a[i:i+2] for i in range(0, len(a), 2)]
    
    last_string = my_list[-1]
    if len(last_string) == 1:
        new_str = last_string + '_'
        my_list[-1] = new_str
        
        
    return my_list


if __name__ == '__main__':
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []