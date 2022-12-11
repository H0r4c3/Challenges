'https://py.checkio.org/en/mission/bulls-and-cows/'

'''
The host thinks up a 4-digits sequence. The digits must all be different. Then, in turn, you try to guess the sequence. 
If the matching digits are on their right positions, they are called "bulls", when they are on different positions, they are "cows". 
The host tells you how many "bulls" and "cows" you've guessed. You should attempt to solve the code in eight turns (it is however, possible in seven turns).

On each step, your function receives a list with information from the previous steps. Each element of the list contains your guess and 
the result in the following format "XXXX YBZC" , where:

XXXX is a guess
Y is a quantity of "bulls"
Z is a quantity of "cows"
'''

def checkio(data):
    #your function
    return "0123"


# Best Solution:
# https://github.com/hrvach/CheckiO/blob/master/Bulls%20and%20Cows.py

import string
from functools import reduce

response = ((3,1), (2,2), (3,0), (2,0), (1,0), (0,0), (2,1), (1,1))

def checkio(a):
  if not len(a)>2: return ['1357', '2491', '6890'][len(a)]
  
  def count(goal, res):
    bulls = cows = 0
    for u, g in zip(res, goal):
        if u == g:
            bulls += 1
        elif u in goal:
            cows += 1
    return bulls, cows

  candidates = {str(i).zfill(4) for i in range(9999)} 
  results = dict(list(map(str.split, a)))

  bulls = {i[:4]: (int(i[5]), int(i[7])) for i in a}  

  
  conditions = [set([x for x in candidates if count(x, key)==val]) for key,val in bulls.items()]
 
  conditions = reduce(set.intersection, conditions)

  bla = dict()  
  for c in conditions:            
      bla[c]=sum([len([x for x in conditions if count(x, key)==val]) for key,val in bulls.items()])
  
  return min(bla, key=bla.get)



if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, goal):
        recent = []
        for step in range(8):
            user_result = func(recent)
            bulls = cows = 0
            for u, g in zip(user_result, goal):
                if u == g:
                    bulls += 1
                elif u in goal:
                    cows += 1
            recent.append("{0} {1}B{2}C".format(user_result, bulls, cows))
            if bulls == 4:
                print("{0} Win with {1} steps.".format(goal, step + 1))
                return True
        print("{0} Fail.".format(goal))
        return False

    assert check_solution(checkio, "1234"), "1234"
    assert check_solution(checkio, "6130"), "6130"
    assert check_solution(checkio, "0317"), "0317"
    assert check_solution(checkio, "9876"), "9876"
    print('Done!!!')