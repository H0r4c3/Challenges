'https://practice.geeksforgeeks.org/contest/interview-series-amazon-2/problems/'
'https://www.geeksforgeeks.org/palindrome-pair-in-an-array-of-words-or-strings/'

'''
Given a list of words, find if any of the two words can be joined to form a palindrome.

Input  : list[] = {"geekf", "geeks", "or", 
                            "keeg", "abc", "bc"}
Output : Yes
There is a pair "geekf" and "keeg"

Input : list[] =  {"abc", "xyxcba", "geekst", "or",
                                      "keeg", "bc"}
Output : Yes
There is a pair "abc" and "xyxcba"

'''

# 1. Solution
def isPalindrome(st):
 
    length = len(st)
 
    # Compare each character from starting with its corresponding character from last
    for i in range(length // 2):
        if (st[i] != st[length - i - 1]):
            return False
 
    return True
 
# Function to check if a palindrome pair exists
def checkPalindromePair(vect):
 
    # Consider each pair one by one
    for i in range(len(vect) - 1):
        for j in range(i + 1, len(vect)):
             
            # Concatenate both strings
            check_str = vect[i] + vect[j]
 
            # Check if the concatenated
            # string is palindrome
            if (isPalindrome(check_str)):
                return True
 
            # Check for other combination of the two strings
            check_str = vect[j] + vect[i]
            if (isPalindrome(check_str)):
                return True
    return False

   
# Driver code
if __name__ == "__main__":
   
    vect = ["geekf", "geeks", "or",
            "keeg", "abc", "bc"]
     
    if checkPalindromePair(vect):
        print("Yes")
    else:
        print ("No")
        
        

# 2. Solution
'''
Efficient method 
It can be done efficiently by using the Trie data structure. The idea is to maintain a Trie of the reverse of all words.
1) Create an empty Trie.
2) Do following for every word:-
    a) Insert reverse of current word.
    b) Also store up to which index it is 
       a palindrome.
3) Traverse list of words again and do following 
   for every word.
    a) If it is available in Trie then return true
    b) If it is partially available
         Check the remaining word is palindrome or not 
         If yes then return true that means a pair
         forms a palindrome.
         Note: Position upto which the word is palindrome
               is stored because of these type of cases.
'''
def function(wordlist):
  #storing word in reverse format along with their indices.
   
    hashmap_reverse = {word[::-1]: index for index, word in enumerate(wordlist)}
    ans = []
    #enumerating over all words and for each character of them
    for index, word in enumerate(wordlist):
        for i in range(len(word)):
          #extracting left and right of them
            left, right = word[:i+1], word[i+1:]
            #checking if left exists and is palindrome and also right is present in map
            #this is to make sure the best edge case described holds.
             
            if not len(left) == 0 and left == left[::-1] and right in hashmap_reverse and hashmap_reverse[right] != index:
                ans.append([hashmap_reverse[right], index])
               
            #normal case.
            if right == right[::-1] and left in hashmap_reverse and hashmap_reverse[left] != index:
                ans.append([index, hashmap_reverse[left]])
    if len(ans)>0:
        return True
    return False
   
   
words = ["geekf", "geeks", "or","keeg", "abc", "bc"]
print(function(words))