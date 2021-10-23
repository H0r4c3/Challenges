'https://leetcode.com/problems/guess-number-higher-or-lower/'

'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.
'''
import logging
import sys

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\LeetCode_Challenges\guess_number_higher_or_lower.log'
  
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

logger = logging.getLogger('main')

start = 0

def guesss(pick):
        if pick < num:
            return -1
        elif pick > num:
            return 1
        else: 
            return 0
        
        
class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        Method NOK!!!
        This method has a problem with return, because return exits one level only!!!!!!!!
        '''
        global start
        
        if n == 1:
            return 1
        
        pick = (start+n)//2
        logging.info(f"Start")
        logging.debug(f'pick = {pick}')
        
        if guesss(pick)==-1:
            logging.debug(f'guesss(pick)={guesss(pick)}')
            start = pick
            logging.debug(f'start=pick -> {pick}')
            self.guessNumber(n)
        elif guesss(pick)==1:
            logging.debug(f'guesss(pick)={guesss(pick)}')
            n = pick
            logging.debug(f'n=pick -> {pick}')
            self.guessNumber(n)
        elif guesss(pick)==0:
            logging.debug(f'guesss(pick)={guesss(pick)}')
            logging.debug(f'return pick={pick}')
            print(pick)
            sys.exit
        else:
            print('Wrong result from guesss(pick)')
        
        logging.debug(f'bad finish: pick={pick}')
        return pick
    
    def guessNumber_OK():
        l = 1
        r = n
        
        while l <= r:
            
            # my guess
            mid = l + (r-l) // 2
            
            if guesss(mid) == -1:
                r = mid - 1
            elif guesss(mid) == 1:
                l = mid + 1                
            else:
                return mid

        return mid

n = 10
num = 6 # the number for guessing (the target)
 
my_obj = Solution()
pick = my_obj.guessNumber_OK()
print(pick)
        
        
    