'https://py.checkio.org/en/mission/hacker-language/'

'''
Your friends and you have decided to feel like the true hackers and create a special "hacker language" for correspondence in the net. 
The original messages will be written in English and then encrypted according to these rules:
- all letters and whitespaces will be converted into their ASCII codes and than into the binary numbers. 
Except the whitespaces - their binary form should be '1000000' not '100000'.
- numbers, dates (in the 'dd.mm.yyyy' format), time (in the 'hh:mm' format) and special signs ('.', ':', '!', '?', '@', '$', '%') won't be converted.
For the realization of this system you should create the HackerLanguage class with the following methods:

write (text) - adds new (text) to the current text message.
delete (N) - deletes from the current text message the last N symbols.
send() - returns the encrypted message which will be send.
read (text) - gets the encrypted (text) as the argument and returns the normal readable English text.
'''

class HackerLanguage:
    pass




# Best Solution:
# https://py.checkio.org/mission/hacker-language/publications/Tinus_Trotyl/python-3/first/share/2ee38ac04577a2419e4df0d5dc820cbf/

class HackerLanguage:
    
    def __init__(self):
        self.message = ''
        
    def write(self, addition):
        self.message = self.message + addition
    
    def delete(self,cut_off):
        self.message = self.message[: -cut_off]
    
    def send(self):
        code = ''
        for ch in self.message:
            if ch == ' ':                    code += '1000000'
            elif ch in '0123456789.,:!?$%@': code += ch
            else:                            code += bin(ord(ch) + 0x80)[3:]                
        return code
    
    def read(self, code):
        message = ''
        while code:
            if code[:7] == '1000000':              message, code = message + ' ', code[7:]
            elif all(c in '01' for c in code[:7]): message, code = message + chr(int(code[:7], 2)), code[7:]
            else:                                  message, code = message + code[:1], code[1:]
        return message




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")