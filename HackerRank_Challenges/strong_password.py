'https://www.hackerrank.com/challenges/strong-password/problem'

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")
    counter1 = 0
    counter2 = 0
    counter = 0
    
    s_password = set(password)
    
    if s_password.intersection(numbers) == set():
        counter1 +=1
        
    if s_password.intersection(lower_case) == set():
        counter1 +=1
        
    if s_password.intersection(upper_case) == set():
        counter1 +=1
        
    if s_password.intersection(special_characters) == set():
        counter1 +=1
        
    if n < 6:
        counter2 = 6 - n
        
    if counter1 >= counter2:
        counter = counter1
    else:
        counter = counter2 
        
    return counter

n = 3
password = 'Ab1'
answer = minimumNumber(n, password)
print(answer)