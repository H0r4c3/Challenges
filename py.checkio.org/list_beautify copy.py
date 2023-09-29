'https://py.checkio.org/en/mission/list-beautify/share/9642245bc745c13b705758200ef54255/'

'''
Your function should return something from both views and improved: 
a single string (multiline if more than one inner list), where numbers in columns should be right-aligned.
'''

def convert_list_to_string(my_list):
    #print(my_list)
    # add comma and space after every converted element to string, except the last one
    my_list_with_commas = [str(item) + ', ' for item in my_list[:-1]]
    
    # append the last element from list
    my_list_with_commas.append(str(my_list[-1]))
    #print(my_list_with_commas)
    
    my_str_with_commas = '[' + ''.join(my_list_with_commas) + ']'
    #print(my_str_with_commas)
    
    return my_str_with_commas


def complete_with_spaces(my_list):
    my_list1 = sorted(my_list, key=len)
    len_max = len(my_list1[-1])
    my_list_new = [' ' * (len_max - len(item)) + item for item in my_list]
        
    return my_list_new
    

def alignment(data):
    aligned_lists = list()
    
    print(f'data = {data}')
    
    my_zip = zip(*data)
    #print(list(my_zip))
    
    # convert to string
    my_zip_str = [list(map(str, my_tuple)) for my_tuple in my_zip ]
    print(list(my_zip_str))
    
    aligned_lists = [complete_with_spaces(item) for item in my_zip_str]
    print(aligned_lists)
    
    aligned_lists = zip(*aligned_lists)
    print(list(aligned_lists))
    
    return list(aligned_lists)
    
    

def list_beautify(data: list[list[int]]) -> str:
    alignment(data)
    
    # if the list has only ONE list
    if len(data) == 1:
        result = '[' + convert_list_to_string(data[0]) + ']'
        print(result)
        return result
    else:
        result_list = ([convert_list_to_string(item) + ',\n ' for item in data[:-1]])
        
        # append the last list
        result_list.append(convert_list_to_string(data[-1]))
        print(result_list)
        
        # convert to string
        result = '[' + ''.join(result_list) + ']'
        print(result)
     
    return result


print("Example:")
#print(list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]))

# These "asserts" are used for self-checking

#assert list_beautify([[1, 10, 100, -1000]]) == "[[1, 10, 100, -1000]]"

#assert list_beautify([[10, 2, 1000, 2]]) == "[[10, 2, 1000, 2]]"

assert (
    list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]])
    == "[[ 1,   2,   10,  150],\n [10,   2, 1000,    2],\n [ 1, 120,    1, 1000]]"
)
assert list_beautify([[1, 10, 100, -1000]]) == "[[1, 10, 100, -1000]]"
assert (
    list_beautify([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1]]"
)
assert (
    list_beautify([[1, 1, -1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, -1, 1, 1],\n [1, 1,  1, 1, 1],\n [1, 1,  1, 1, 1]]"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")