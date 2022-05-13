'https://py.checkio.org/en/mission/amsco-cipher/'

'''
The key is represented as a number that consist of unique digits from 1 to N. N is a length of the key. 
To encode message we should write a message in a matrix with N columns. 
The matrix is written row by row. In this process, one or two characters are alternately recorded in a field. 
One or two characters alternate in rows and in columns too (like a chessboard). 
The first element is single letter field (this is the arrangement for this mission). 
The last field can have single characters if there are not enough. 
Columns are then numbered with digits from the key in order. 
For example: using the key 312, the first column will be 3, the second is 1 and the third is 2. 
Lastly, you will write all characters in the columns as they were numbered in the most recent step. 
All white spaces and punctuation symbols are excluded while letters are in lowercase.
'''

def decode_amsco(message, key):
    
    
    return message


# Best Solution: 
# https://py.checkio.org/mission/amsco-cipher/publications/veky/python-3/i-forgot-about-this-one/?ordering=most_voted&filtering=all
from itertools import cycle, islice, zip_longest

def decode_amsco(message, key):
    key, lenm, it = str(key), len(message), iter(message)
    lens = {i: [start] for i, start in zip(key, cycle([1, 2]))}
    total = sum(sum(lens.values(), []))
    for column in map(lens.get, cycle(key)):
        nextlen = min(lenm - total, 3 - column[~0])
        if not nextlen: break
        column.append(nextlen)
        total += nextlen
    seg = {i: [''.join(islice(it, lh)) for lh in lens[i]] for i in sorted(key)}
    return ''.join(sum(zip_longest(*map(seg.get, key), fillvalue=''), ()))

    
    
    
# Solution: https://programtalk.com/vs2/python/6903/checkio/AMSCO%20cipher.py/

def decode_amsco(message, key):
    # create empty matrix
    matrix = [[] for i in range(len(str(key)))]
    i = 0
    while i < len(message):
        for j in range(len(str(key))):
            if ((j % 2 != 0 and len(matrix[j]) % 2 == 0)
                    or (j % 2 == 0 and len(matrix[j]) % 2 != 0)):
                if i + 2 <= len(message):
                    matrix[j].append('  ')
                    i += 2
                elif i + 1 <= len(message):
                    matrix[j].append(' ')
                    i += 1
            else:
                if i + 1 <= len(message):
                    matrix[j].append(' ')
                    i += 1
 
    # fill the empty matrix
    for i in range(1, len(str(key)) + 1):
        column = matrix[str(key).index(str(i))]
        for j in range(len(column)):
            column[j] = message[:len(column[j])]
            message = message[len(column[j]):]
 
    # re-order by rows
    OriginalMessage = ''
    for i in range(max(map(len, matrix))):
        OriginalMessage += ''.join([j[i] for j in matrix if i <= len(j) - 1])
 
    return OriginalMessage
 


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
    print('Done!!!')