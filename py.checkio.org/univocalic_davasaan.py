'https://py.checkio.org/en/mission/univocalic-davasaan/'

'''
You have to write a function named davasaan (division with all vowels a) which calculates integer division by 10.
The vowels " eiou " are disallowed as are the slash " / ", asterisk " * ", and period " . " characters.

We have one more rule for this univocalic challenge. 
This is a code golf mission and your main goal is to make your code as short as possible: 300 characters is the maximum allowable.

Input: A non-negative number as an integer.

Output: The integer division ( //10 ) of the input as an integer.
'''

# https://py.checkio.org/mission/univocalic-davasaan/publications/Ylliw/python-3/64-chars-with-explanations/share/0778667b405846339485bba195e0d0c6/

davasaan=d=lambda n:[n>9,(a:=n>>4)and a+d(n-(a<<3)-(a<<1))][a>0]

# recursively with the greatest power of n (let's call it a) so that 10*a is less than n
# a=n>>4 = n//16 is that greatest power, so we know that 10a is less than n
# Therefore new_n=n-10a is less than n and if we know that davasaan(n)=a+davassan(new_n)
# 
# It's now time to make this work, so let's define d=davassan (less char usage in recursion)
# new_n=n-10a=n-8a-2a=n-(a<<3)-(a<<1)
# and a is n>>4 (n//16)
# so main recursion element is d(n-(n>>4<<3)-(n>>4<<1))
# Let's now add the corner cases:
# We can do the recursion only if n>=16, so n>>4 and <recursion> ensure n>=16 only as and does not evaluate 2nd element if 1st is False
# Finally is n is less than 16, so 15 or less, we need to return 1 if n>=10 and 0 if n<10
# n>9 is the shortest condition and +(n>9) ensure it's considered as int and not boolean
# I finally used a two element list (n<=16, n>15) with a condition (n>15) to choose as 'or' is not acceptable.
#
# Last trick added (Python 3.8.1): assign n>>4 to p (a:n>>4) to reduce number of chars as it's used 4 times.
# Brackets around a:=n>>4 is mandatory as otherwise it's evaluating the 'and' part before assignment.
#
# Finally and thanks to Phil15 comments, I remove the unnecessary + sign to convert n>9 to int and the parenthesis left around one 'a' occurence



# this assertion should be stripped after self-testing!!!!!
if __name__ == '__main__':
    assert davasaan(0) == 0, "First"
    assert davasaan(7) == 0, "Second"
    assert davasaan(81) == 8, "Third"
    assert davasaan(199) == 19, "Fourth"
    assert davasaan(4500) == 450, "Fifth"
    assert davasaan(9999) == 999, "Sixth"
    print('Click on "Check" to get your code inspected and for real tests.')
