'https://www.hackerrank.com/challenges/two-characters/problem'
'https://www.thepoorcoder.com/hackerrank-two-characters-solution/'

'''
Given a string, remove characters until the string is made up of any two alternating characters. 
When you choose a character to remove, all instances of that character must be removed. 
Determine the longest string possible that contains just two alternating letters.
'''


import re
from itertools import combinations

import logging

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\Challenges\HackerRank_Challenges\two_characters.log'
  
#Create and configure logger
#logging.basicConfig(filename=path, format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

logger = logging.getLogger('main')

def alternate(s):
    m = 0
    
    for i in (combinations(set(s),2)):
        logger.debug(f'for i {i} in combinations(set(s),2) {combinations(set(s),2)}')
        j = "".join(i)
        logger.debug(f'j = {j}')
        t = re.sub("[^%s]"%j, "",s)
        logger.debug(f't = re.sub("[^%s]"%j, "",s) = {t}')
        
        if len(t)>m and not re.search(r"(\w)\1", t) :
            m = len(t)
            logger.debug(f'm = {m}')
            
    return m

s1 = 'aabbccdd'
s3 = 'beabeefeab'
s4 = 'asvkugfiugsalddlasguifgukvsa'
s = 'asdcbsdcagfsdbgdfanfghbsfdab'

print(alternate(s))