'https://www.hackerrank.com/challenges/alphabet-rangoli/problem'

import logging

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Misc\hackerrank_challanges\alphabet_rangoli.log'

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

logger = logging.getLogger('main')



def und(n, i):
    return (n-i)*2*'-'
    

def print_rangoli(size):
    
    if size == 1:
        print('a')
        exit()
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alph = ['a-', 'b-', 'c-', 'd-', 'e-', 'f-', 'g-', 'h-', 'i-', 'j-', 'k-', 'l-', 'm-', 'n-', 'o-', 'p-', 'q-', 'r-', 's-', 't-', 'u-', 'v-', 'w-', 'x-', 'y-', 'z-']
    my_list = [None] * n
    h = [alph[n-1], alph[n-2], alph[n-3], alph[n-4], alph[n-5], alph[n-6], alph[n-7], alph[n-8], alph[n-9], alph[n-10], alph[n-11], alph[n-12], 
         alph[n-13], alph[n-14], alph[n-15], alph[n-16], alph[n-17], alph[n-18], alph[n-19], alph[n-20], alph[n-21], alph[n-22], alph[n-23], alph[n-24], alph[n-25],  
         alph[n-26], alph[n-25], alph[n-24], alph[n-23], alph[n-22], alph[n-21], alph[n-20], alph[n-19], alph[n-18], alph[n-17], alph[n-16], alph[n-15], alph[n-14], 
         alph[n-13], alph[n-12], alph[n-11], alph[n-10], alph[n-9], alph[n-8], alph[n-7], alph[n-6], alph[n-5], alph[n-4], alph[n-3], alph[n-2]]
    
    
    # my_list[0] = und(n, 1) +                                                 alphabet[n-1] + und(n, 1)
    # my_list[1] = und(n, 2) + alph[n-1] + alph[n-2] +                         alphabet[n-1] + und(n, 2)
    # my_list[2] = und(n, 3) + alph[n-1] + alph[n-2] + alph[n-3] + alph[n-2] + alphabet[n-1] + und(n, 3)
    
    #my_list[26] = und(n, 26) + alph[n-1] + alph[n-2] + alph[n-3] + ... + alph[n-26] + alph[n-25] + alph[n-24] + ... + alphabet[n-1] + und(n, 26)
    
    # for i in range(n):
    # my_list[n-i] = und(n, n-i+1) + alph[n-1] + alph[n-2] + ... + alph[n-n] + alph[n-1] + alph[n-2] + ... + alph[n-n+1] + alphabet[n-1] + und(n, n-i+1)
    
    my_list[0] = und(n, 1) + alphabet[n-1] + und(n, 1)
    my_list[1] = und(n, 2) + h[0] + h[1] + alphabet[n-1] + und(n, 2)
    #my_list[2] = und(n, 3) + h[0] + h[1] + h[2] + h[1] + alphabet[n-1] + und(n, 3)
    #my_list[2] = und(n, 3) + ''.join(h[0:3]) + h[1] + alphabet[n-1] + und(n, 3)
    
    for i in range(2,n):
        
        my_list[i] = und(n, i+1) + ''.join(h[0:i+1]) + ''.join(h[i-1:0:-1]) + alphabet[n-1] + und(n, i+1)
        logging.debug(f'i = {i} = {my_list[i]}')
        logging.debug(f'und(n, i+1) = {und(n, i+1)}')
        logging.debug(f"''.join(h[0:i+1]) = {''.join(h[0:i+1])}")
        logging.debug(f"''.join(h[i:n]) = {''.join(h[i:n])}")
        logging.debug(f"alphabet[n-1] = {alphabet[n-1]}" )
                      
                      
    for i in range(n):
        print(my_list[i])
    
    for i in reversed(range(n-1)):
        print(my_list[i])

if __name__ == '__main__':
    #print('Enter an integer < 27: ', end='')
    #n = int(input())
    n = 5
    print_rangoli(n)