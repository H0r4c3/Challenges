'https://py.checkio.org/en/mission/loading-cargo/'

'''
You have been given a list of integer weights. 
You should help Stephen distribute these weights into two sets, such that the difference between the total weight of each set is as low as possible.

Input data: A list of the weights as a list of integers.

Output data: The number representing the lowest possible weight difference as a positive integer.
'''
from itertools import pairwise

# My Solution (NOK, should be modified!!!)
def checkio_(data):
    left, right = list(), list()
    data.sort()
    print(f'START data = {data}')
    
    # data = eliminate_duplicates(data)
    # print(f'data after eliminate pairs of duplicates = {data}')
    # if not data: return 0
    
    def calc(data):
        if sum(left) <= sum(right):
            if data:
                left.append(data.pop())
            if sum(left) <= sum(right):
                if data:
                    left.append(data.pop())
            else:
                if data:
                    right.append(data.pop())
        else:
            if data:
                right.append(data.pop())
            if sum(left) >= sum(right):
                if data:
                    right.append(data.pop())
            else:
                if data:
                    left.append(data.pop())
                
        
        print(f'left = {left}')
        print(f'right = {right}')
        
        # new data, after deletions    
        print(f'New data, after deletions = {data}')
        
        print(sum(left), sum(right))
        return sum(left), sum(right)
    
    while data:
        s_left, s_right = calc(data)
    
    print(abs(s_left - s_right))
    return abs(s_left - s_right)



# My Solution (NOK, should be modified!!!)
def checkio_(data):
    left, right = list(), list()
    data.sort()
    print(data)
    
    def calc(data):
        data_pairs = list(pairwise(data))
        print(data_pairs)
    
        differences = [item[1] - item[0] for item in data_pairs]
        print(differences)
        
        diff_enum = enumerate(differences)
        
        diff_enum_sort = sorted([(count, values) for count, values in diff_enum], key=lambda x : x[1])
        print(diff_enum_sort)
        
        ix = diff_enum_sort[0][0]
        
        s_left = sum(left)
        s_right = sum(right)
        
        if s_left <= s_right:
            left.append(data_pairs[ix][0])
            if s_left <= s_right:
                left.append(data_pairs[ix][0])
            else:
                right.append(data_pairs[ix][1])
        else:
            right.append(data_pairs[ix][1])
            if s_left <= s_right:
                left.append(data_pairs[ix][0])
            else:
                right.append(data_pairs[ix][0])
        
        data.remove(data_pairs[ix][0])
        data.remove(data_pairs[ix][1])
        print(data)
        
        s_left = sum(left)
        s_right = sum(right)  
        print(left)
        print(s_left)
        print(right)
        print(s_right)
        
        return s_left, s_right
    
    s_left, s_right = calc(data)
    s_left, s_right = calc(data)

    print(abs(s_left - s_right))
    return abs(s_left - s_right)



import itertools

def checkio_(data):
# split in 2 parts (all the 2 parts) and calculate the 2 sums (all)
    diff = list()

    def binary_splits(seq):
        for result_indices in itertools.product((0,1), repeat=len(seq)):
            result = ([], [])
            for seq_index, result_index in enumerate(result_indices):
                result[result_index].append(seq[seq_index])
            #skip results where one of the sides is empty
            if not result[0] or not result[1]: continue
            #convert from list to tuple so we can hash it later
            yield map(tuple, result)

    def binary_splits_no_dupes(seq):
        seen = set()
        for item in binary_splits(seq):
            key = tuple(sorted(item))
            if key in seen: continue
            yield key
            seen.add(key)

    for left, right in binary_splits_no_dupes(data):
        print(left, right)
        diff.append((abs(sum(left) - sum(right))))   
        
    print(diff)
    return min(diff)



# My SOLUTION (Brute Force)
from itertools import combinations

def checkio(data):
    diff = list()
    
    def split_list(my_list):
        all_comb = list()
        pairs = list()
        
        for i in range(1, len(my_list)):
            all_comb = all_comb + list(combinations(my_list, i))
        
        for item in all_comb:
            left = item
            right = my_list[:]
            for i in left:
                right.remove(i)
            pairs.append([left, right])
            
        return pairs

    pairs = split_list(data)

    for item in pairs:
        print(item)
        print((abs(sum(item[0]) - sum(item[1]))))
        diff.append((abs(sum(item[0]) - sum(item[1]))))
    
    if diff == []:
        return 0
    
    print(diff)
    print(min(diff))
    return min(diff)
    



# Best Solution
# https://py.checkio.org/mission/loading-cargo/publications/PythonLearner/python-3/first/share/affcad738034b32f96db1447f4f6c6c9/

def checkio_(data):
    def get_difference(n):
        mask = bin(n)[2:].zfill(len(data))
        return abs(sum(item if flag == '1' else -item for item, flag in zip(data, mask)))
    return min(map(get_difference, range(2**len(data)+1)))


# Another Best Solution: 
# https://py.checkio.org/mission/loading-cargo/publications/takapt0226/python-3/first/?ordering=most_voted&filtering=all

def checkio(data):
    dp = {0}
    for i in data:
        ndp = set()
        for diff in dp:
            ndp.add(abs(i - diff))
            ndp.add(abs(i + diff))
        dp = ndp
    return min(dp)




#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example: 30,30,42 - 12,32,49"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
    assert checkio([9,9,7,6,5]) == 0, "7,6,5 - 9,9"
    assert checkio([33,5,10,19,35,16,10]) == 0, "33,16,10,5 - 35,19,10"
    print('Done!!!')