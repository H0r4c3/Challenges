'https://www.hackerrank.com/challenges/string-construction/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen'

import math
import os
import random
import re
import sys


def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    assert stringConstruction('abcd') == 4
    assert stringConstruction('abab') == 2
    print('Done!!!')