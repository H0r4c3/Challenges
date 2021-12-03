'https://py.checkio.org/en/mission/remove-accents/'

'''
Assuming you are developing a user based system like facebook, you will want to provide the functionality to 
search for other members regardless of the presence of accents in a username. 

Without using a 3rd party collation library, you will need to remove the accents from the username before the comparison.

é - letter with an accent; e - letter without an accent; ̀ and ́ - the stand alone accents;
'''

# Method 1

import unidecode

def checkio(in_string):
    out_string = unidecode.unidecode(in_string)
    
    return out_string




# Method 2

import unicodedata

def checkio_2(in_string):
    # The character category "Mn" stands for Nonspacing_Mark, which is similar to unicodedata.combining
    out_list = [c for c in unicodedata.normalize('NFD', in_string) if unicodedata.category(c) != 'Mn']
    
    return ''.join(out_list)



    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    assert checkio(u"café") == u"cafe"
    assert checkio(u"ăŞŢşţâ") == u"aSTsta"
    print('Done')

