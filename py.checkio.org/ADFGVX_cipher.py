'https://py.checkio.org/en/mission/adfgvx-cipher/'

'''
The ADFGVX Cipher was a field cipher used by the German Army on the Western Front during World War I. 
ADFGVX was in fact an extension of an earlier cipher called ADFGX. 
Invented by Colonel Fritz Nebel and introduced in March 1918, the cipher was a fractionating transposition 
cipher which combined a modified Polybius square with a single columnar transposition. 
The cipher is named after the six possible letters used in the ciphertext: A, D, F, G, V and X.
'''

def encode(message, secret_alphabet, keyword):
    return message


def decode(message, secret_alphabet, keyword):
    return message



# Best Solution:
# https://py.checkio.org/mission/adfgvx-cipher/publications/Sim0000/python-3/first/share/df908004320485452ac0c0621aff96b7/

MAGIC = 'ADFGVX'

def encode(message, secret_alphabet1, keyword):
    # remove duplicate character from keyword -> key
    # keyword = 'checkio' -> key = ['c','h','e','k','i','o']
    key = []
    for c in keyword:
        if c not in key: key.append(c)

    # make sort index -> k
    # keyword = 'cipher' -> k = [0, 4, 3, 2, 1, 2, 5]
    n = len(key)
    k = sorted(range(n), key=lambda i: key[i])

    # encode
    # message = 'I am going' ->
    # s = ['F','A','D','V','A','G','X','X','D','X','F','A','G','D','X','X']
    s = []
    for c in message.lower():
        if c.isalpha() or c.isdigit():
            row, col = divmod(secret_alphabet1.index(c), 6)
            s += [MAGIC[row], MAGIC[col]]

    # reorder
    # reorder index = [0, 6, 12, 4, 10, 3, 9, 15, 1, 7, 13, 2, 8, 14, 5, 11]
    return ''.join(s[j] for i in k for j in range(i, len(s), n))


def decode(message, secret_alphabet1, keyword):
    # remove duplicate character from keyword -> key
    # keyword = 'checkio' -> key = ['c', 'h', 'e', 'k', 'i', 'o']
    key = []
    for c in keyword:
        if c not in key: key.append(c)

    # make sort index -> k
    # keyword = 'cipher' -> k = [0, 4, 3, 2, 1, 2, 5]
    n = len(key)
    k = sorted(range(n), key=lambda i: key[i])

    # make reorder index
    # len(message) == 16 ->
    # x = [0, 6, 12, 4, 10, 3, 9, 15, 1, 7, 13, 2, 8, 14, 5, 11]
    m = len(message)
    x = [j for i in k for j in range(i, m, n)]

    # reorder
    # message = 'FXGAFVXXAXDDDXGA' ->
    # y = ['F','A','D','V','A','G','X','X','D','X','F','A','G','D','X','X']
    y = ['']*m
    for i, c in zip(x, message): y[i] = c

    # decode
    # y -> s = ['i','a','m','g','o','i','n','g']
    s = []
    for i in range(0, m, 2):
        row, col = y[i:i+2]
        s.append(secret_alphabet1[6 * MAGIC.index(row) + MAGIC.index(col)])
    return ''.join(s)



# Another Best Solution:
# https://py.checkio.org/mission/adfgvx-cipher/publications/Kouri/python-3/stepbystep/?ordering=most_voted&filtering=all

def encode(message, secret_alphabet, keyword):
    '''remove punctions and maj'''
    cleaned_string = list(filter(lambda char : char in 'abcdefghijklmnopqrstuvwxyz1234567890'
                                 , message.lower()))
    '''encode into the 'ADFGVX' alphabet'''
    transformed_string = "".join(['ADFGVX'[secret_alphabet.index(char)//len('ADFGVX')]+'ADFGVX'[secret_alphabet.index(char)%len('ADFGVX')]
                                  for char in cleaned_string])
    '''cleaning the keyword'''
    keyword = "".join(sorted({char:keyword.index(char) for char in keyword}.keys()
                    , key=lambda x : {char:keyword.index(char) for char in keyword}[x]))
    '''split the string according to keyword'''
    split_string = [transformed_string[index*len(keyword):(index+1)*len(keyword)]
                    for index in range(len(transformed_string)//len(keyword)+int(0<len(transformed_string)%len(keyword)))]
    '''associate letters of the keyword to splitted chars'''
    base_order_dic = {char:[elem[i] if i<len(elem) else "" for elem in split_string]
                      for i, char in enumerate(keyword)}
    '''rebuild the final string'''
    mixed_order = "".join(sum([base_order_dic[key] for key in sorted(base_order_dic.keys())], []))
    
    return mixed_order
    
def decode(message, secret_alphabet, keyword):
    '''build a grid with the alphabet'''
    alphabet_grid = [[secret_alphabet[i+j*len('ADFGVX')] for i in range(len('ADFGVX'))] for j in range(len('ADFGVX'))]
    '''cleaning the keyword'''
    keyword = "".join(sorted({char:keyword.index(char) for char in keyword}.keys()
                    , key=lambda x : {char:keyword.index(char) for char in keyword}[x]))
    '''split the string according to keyword'''
    blank_char = [0 if len(message)%len(keyword)-1<keyword.index(char) else 1 for i, char in enumerate(sorted(keyword))]
    indexes = [sum([len(message)//len(keyword)+i for i in blank_char[:j]]) for j in range(len(blank_char))]+[len(message)]
    split_string = [message[indexes[i]:indexes[i+1]]for i in range(len(indexes)-1)]
    '''associate letters of the keyword to splitted chars'''
    mixed_order = {char:split_string[i] if len(split_string[i])==len(message)//len(keyword)+1 else split_string[i]+" "  for i, char in enumerate(sorted(keyword))}
    '''rebuild the original order'''
    base_order_dic = [mixed_order[char] for char in keyword]
    rebuild_coded_char = "".join([elem[j] for j in range(len(base_order_dic[0])) for elem in base_order_dic]).replace(" ", "")
    '''Recompose word'''
    char_coord = [rebuild_coded_char[i:i+2] for i in range(0, len(rebuild_coded_char)-1, 2)]
    recomposed_message = "".join([alphabet_grid['ADFGVX'.index(i[0])]['ADFGVX'.index(i[1])] for i in char_coord])
    
    return recomposed_message





if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"