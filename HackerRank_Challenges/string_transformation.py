'Skill Certification Test nr. 2 - Python (Basics)'

'String Transformation'

'''
There is a sentence that consists of space-separated strings of upper and lower case English letters.
Transform each string according to the given algorithm and return the new sentence.

Each string should be modified as follows:
- The first character of the string remains unchanged
- For each subsequent character, say x, consider a letter preceding it, say y:
    - If y precedes x in the alphabet, transform x to uppercase
    - If x precedes y in the alphabet, transform x to lowercase
    - If x and y are equal, the letter remains unchanged
'''

def transformSentence(sentence):
    new_sentence = []
    
    sentence_list = sentence.split()
    
    for string in sentence_list:
        st = string[0]
        if len(string)==1:
            new_sentence.append(st)
        else:
            for i in range(1, len(string)):
                if string[i].lower()==string[i-1].lower():
                    st = st + string[i]
                elif string[i].lower() > string[i-1].lower():
                    st = st + string[i].upper()
                else:
                    st = st + string[i].lower()
                    
            new_sentence.append(st)
        
    result = ' '.join(new_sentence)
    
    return result

sentence = 'coOL dog'
result = transformSentence(sentence)
print(result)




sentence = ''
result = transformSentence(sentence)
print(result)