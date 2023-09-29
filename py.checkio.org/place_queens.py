'https://py.checkio.org/en/mission/place-queens/'

'''
You should place eight chess Queens on an 8x8 chessboard so that no two Queens threaten each other. 
For this challenge, we have already placed one or more Queens on the board, so you will need to finish the placement.

1 
2
3
4
5
6
7
8
 a b c d e f g h
 
 
 THREATS = {
    'h2': ['a2', 'b2', 'b8', 'c2', 'c7', 'd2', 'd6', 'e2', 'e5', 'f2', 'f4', 'g1', 'g2', 'g3', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'g2': ['a2', 'a8', 'b2', 'b7', 'c2', 'c6', 'd2', 'd5', 'e2', 'e4', 'f1', 'f2', 'f3', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h1', 'h2', 'h3'],
    'a4': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b3', 'b4', 'b5', 'c2', 'c4', 'c6', 'd1', 'd4', 'd7', 'e4',
           'e8', 'f4', 'g4', 'h4'],
    'h8': ['a1', 'a8', 'b2', 'b8', 'c3', 'c8', 'd4', 'd8', 'e5', 'e8', 'f6', 'f8', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'd8': ['a5', 'a8', 'b6', 'b8', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e7', 'e8', 'f6', 'f8',
           'g5', 'g8', 'h4', 'h8'],
    'g1': ['a1', 'a7', 'b1', 'b6', 'c1', 'c5', 'd1', 'd4', 'e1', 'e3', 'f1', 'f2', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6',
           'g7', 'g8', 'h1', 'h2'],
    'a7': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b6', 'b7', 'b8', 'c5', 'c7', 'd4', 'd7', 'e3', 'e7', 'f2',
           'f7', 'g1', 'g7', 'h7'],
    'a3': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b2', 'b3', 'b4', 'c1', 'c3', 'c5', 'd3', 'd6', 'e3', 'e7',
           'f3', 'f8', 'g3', 'h3'],
    'c3': ['a1', 'a3', 'a5', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd2', 'd3', 'd4', 'e1',
           'e3', 'e5', 'f3', 'f6', 'g3', 'g7', 'h3', 'h8'],
    'h1': ['a1', 'a8', 'b1', 'b7', 'c1', 'c6', 'd1', 'd5', 'e1', 'e4', 'f1', 'f3', 'g1', 'g2', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'b4': ['a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c3', 'c4', 'c5', 'd2', 'd4', 'd6', 'e1',
           'e4', 'e7', 'f4', 'f8', 'g4', 'h4'],
    'b2': ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'd2', 'd4', 'e2', 'e5',
           'f2', 'f6', 'g2', 'g7', 'h2', 'h8'],
    'g8': ['a2', 'a8', 'b3', 'b8', 'c4', 'c8', 'd5', 'd8', 'e6', 'e8', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6',
           'g7', 'g8', 'h7', 'h8'],
    'g6': ['a6', 'b1', 'b6', 'c2', 'c6', 'd3', 'd6', 'e4', 'e6', 'e8', 'f5', 'f6', 'f7', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h5', 'h6', 'h7'],
    'h7': ['a7', 'b1', 'b7', 'c2', 'c7', 'd3', 'd7', 'e4', 'e7', 'f5', 'f7', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'e1': ['a1', 'a5', 'b1', 'b4', 'c1', 'c3', 'd1', 'd2', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2',
           'g1', 'g3', 'h1', 'h4'],
    'h4': ['a4', 'b4', 'c4', 'd4', 'd8', 'e1', 'e4', 'e7', 'f2', 'f4', 'f6', 'g3', 'g4', 'g5', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'g4': ['a4', 'b4', 'c4', 'c8', 'd1', 'd4', 'd7', 'e2', 'e4', 'e6', 'f3', 'f4', 'f5', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h3', 'h4', 'h5'],
    'd7': ['a4', 'a7', 'b5', 'b7', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e6', 'e7', 'e8',
           'f5', 'f7', 'g4', 'g7', 'h3', 'h7'],
    'h5': ['a5', 'b5', 'c5', 'd1', 'd5', 'e2', 'e5', 'e8', 'f3', 'f5', 'f7', 'g4', 'g5', 'g6', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'f5': ['a5', 'b1', 'b5', 'c2', 'c5', 'c8', 'd3', 'd5', 'd7', 'e4', 'e5', 'e6', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
           'f7', 'f8', 'g4', 'g5', 'g6', 'h3', 'h5', 'h7'],
    'f3': ['a3', 'a8', 'b3', 'b7', 'c3', 'c6', 'd1', 'd3', 'd5', 'e2', 'e3', 'e4', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
           'f7', 'f8', 'g2', 'g3', 'g4', 'h1', 'h3', 'h5'],
    'b8': ['a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c7', 'c8', 'd6', 'd8', 'e5', 'e8', 'f4', 'f8',
           'g3', 'g8', 'h2', 'h8'],
    'b7': ['a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c6', 'c7', 'c8', 'd5', 'd7', 'e4', 'e7',
           'f3', 'f7', 'g2', 'g7', 'h1', 'h7'],
    'b3': ['a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c2', 'c3', 'c4', 'd1', 'd3', 'd5', 'e3',
           'e6', 'f3', 'f7', 'g3', 'g8', 'h3'],
    'g3': ['a3', 'b3', 'b8', 'c3', 'c7', 'd3', 'd6', 'e1', 'e3', 'e5', 'f2', 'f3', 'f4', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h2', 'h3', 'h4'],
    'c4': ['a2', 'a4', 'a6', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd3', 'd4', 'd5', 'e2',
           'e4', 'e6', 'f1', 'f4', 'f7', 'g4', 'g8', 'h4'],
    'f7': ['a2', 'a7', 'b3', 'b7', 'c4', 'c7', 'd5', 'd7', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7',
           'f8', 'g6', 'g7', 'g8', 'h5', 'h7'],
    'f6': ['a1', 'a6', 'b2', 'b6', 'c3', 'c6', 'd4', 'd6', 'd8', 'e5', 'e6', 'e7', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
           'f7', 'f8', 'g5', 'g6', 'g7', 'h4', 'h6', 'h8'],
    'e8': ['a4', 'a8', 'b5', 'b8', 'c6', 'c8', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f7', 'f8',
           'g6', 'g8', 'h5', 'h8'],
    'c8': ['a6', 'a8', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd7', 'd8', 'e6', 'e8', 'f5', 'f8',
           'g4', 'g8', 'h3', 'h8'],
    'e5': ['a1', 'a5', 'b2', 'b5', 'b8', 'c3', 'c5', 'c7', 'd4', 'd5', 'd6', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',
           'e8', 'f4', 'f5', 'f6', 'g3', 'g5', 'g7', 'h2', 'h5', 'h8'],
    'e4': ['a4', 'a8', 'b1', 'b4', 'b7', 'c2', 'c4', 'c6', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',
           'e8', 'f3', 'f4', 'f5', 'g2', 'g4', 'g6', 'h1', 'h4', 'h7'],
    'c2': ['a2', 'a4', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'e2', 'e4',
           'f2', 'f5', 'g2', 'g6', 'h2', 'h7'],
    'c5': ['a3', 'a5', 'a7', 'b4', 'b5', 'b6', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd4', 'd5', 'd6', 'e3',
           'e5', 'e7', 'f2', 'f5', 'f8', 'g1', 'g5', 'h5'],
    'a1': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'c1', 'c3', 'd1', 'd4', 'e1', 'e5', 'f1', 'f6',
           'g1', 'g7', 'h1', 'h8'],
    'c6': ['a4', 'a6', 'a8', 'b5', 'b6', 'b7', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd5', 'd6', 'd7', 'e4',
           'e6', 'e8', 'f3', 'f6', 'g2', 'g6', 'h1', 'h6'],
    'd2': ['a2', 'a5', 'b2', 'b4', 'c1', 'c2', 'c3', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3',
           'f2', 'f4', 'g2', 'g5', 'h2', 'h6'],
    'f1': ['a1', 'a6', 'b1', 'b5', 'c1', 'c4', 'd1', 'd3', 'e1', 'e2', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
           'g1', 'g2', 'h1', 'h3'],
    'g7': ['a1', 'a7', 'b2', 'b7', 'c3', 'c7', 'd4', 'd7', 'e5', 'e7', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h6', 'h7', 'h8'],
    'f4': ['a4', 'b4', 'b8', 'c1', 'c4', 'c7', 'd2', 'd4', 'd6', 'e3', 'e4', 'e5', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
           'f7', 'f8', 'g3', 'g4', 'g5', 'h2', 'h4', 'h6'],
    'c7': ['a5', 'a7', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd6', 'd7', 'd8', 'e5', 'e7',
           'f4', 'f7', 'g3', 'g7', 'h2', 'h7'],
    'c1': ['a1', 'a3', 'b1', 'b2', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'e1', 'e3', 'f1', 'f4',
           'g1', 'g5', 'h1', 'h6'],
    'e2': ['a2', 'a6', 'b2', 'b5', 'c2', 'c4', 'd1', 'd2', 'd3', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1',
           'f2', 'f3', 'g2', 'g4', 'h2', 'h5'],
    'a2': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'c2', 'c4', 'd2', 'd5', 'e2', 'e6', 'f2',
           'f7', 'g2', 'g8', 'h2'],
    'd6': ['a3', 'a6', 'b4', 'b6', 'b8', 'c5', 'c6', 'c7', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e5', 'e6',
           'e7', 'f4', 'f6', 'f8', 'g3', 'g6', 'h2', 'h6'],
    'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b7', 'b8', 'c6', 'c8', 'd5', 'd8', 'e4', 'e8', 'f3', 'f8',
           'g2', 'g8', 'h1', 'h8'],
    'd3': ['a3', 'a6', 'b1', 'b3', 'b5', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e2', 'e3',
           'e4', 'f1', 'f3', 'f5', 'g3', 'g6', 'h3', 'h7'],
    'f8': ['a3', 'a8', 'b4', 'b8', 'c5', 'c8', 'd6', 'd8', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
           'g7', 'g8', 'h6', 'h8'],
    'd1': ['a1', 'a4', 'b1', 'b3', 'c1', 'c2', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'f1', 'f3',
           'g1', 'g4', 'h1', 'h5'],
    'a5': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b4', 'b5', 'b6', 'c3', 'c5', 'c7', 'd2', 'd5', 'd8', 'e1',
           'e5', 'f5', 'g5', 'h5'],
    'b1': ['a1', 'a2', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'd1', 'd3', 'e1', 'e4', 'f1', 'f5',
           'g1', 'g6', 'h1', 'h7'],
    'e6': ['a2', 'a6', 'b3', 'b6', 'c4', 'c6', 'c8', 'd5', 'd6', 'd7', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
           'f5', 'f6', 'f7', 'g4', 'g6', 'g8', 'h3', 'h6'],
    'a6': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b5', 'b6', 'b7', 'c4', 'c6', 'c8', 'd3', 'd6', 'e2', 'e6',
           'f1', 'f6', 'g6', 'h6'],
    'd4': ['a1', 'a4', 'a7', 'b2', 'b4', 'b6', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e3',
           'e4', 'e5', 'f2', 'f4', 'f6', 'g1', 'g4', 'g7', 'h4', 'h8'],
    'g5': ['a5', 'b5', 'c1', 'c5', 'd2', 'd5', 'd8', 'e3', 'e5', 'e7', 'f4', 'f5', 'f6', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h4', 'h5', 'h6'],
    'b5': ['a4', 'a5', 'a6', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c4', 'c5', 'c6', 'd3', 'd5', 'd7', 'e2',
           'e5', 'e8', 'f1', 'f5', 'g5', 'h5'],
    'b6': ['a5', 'a6', 'a7', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c5', 'c6', 'c7', 'd4', 'd6', 'd8', 'e3',
           'e6', 'f2', 'f6', 'g1', 'g6', 'h6'],
    'h3': ['a3', 'b3', 'c3', 'c8', 'd3', 'd7', 'e3', 'e6', 'f1', 'f3', 'f5', 'g2', 'g3', 'g4', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'h6': ['a6', 'b6', 'c1', 'c6', 'd2', 'd6', 'e3', 'e6', 'f4', 'f6', 'f8', 'g5', 'g6', 'g7', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'f2': ['a2', 'a7', 'b2', 'b6', 'c2', 'c5', 'd2', 'd4', 'e1', 'e2', 'e3', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7',
           'f8', 'g1', 'g2', 'g3', 'h2', 'h4'],
    'd5': ['a2', 'a5', 'a8', 'b3', 'b5', 'b7', 'c4', 'c5', 'c6', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e4',
           'e5', 'e6', 'f3', 'f5', 'f7', 'g2', 'g5', 'g8', 'h1', 'h5'],
    'e3': ['a3', 'a7', 'b3', 'b6', 'c1', 'c3', 'c5', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
           'f2', 'f3', 'f4', 'g1', 'g3', 'g5', 'h3', 'h6'],
    'e7': ['a3', 'a7', 'b4', 'b7', 'c5', 'c7', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f6',
           'f7', 'f8', 'g5', 'g7', 'h4', 'h7']}
 
'''
# My Solution (it's OK, but on the verification on site is failing the assert checker(place_queens, {"a1", "h8"}, False) !!!!!!! )

from itertools import product, combinations

COLS, ROWS = 'abcdefgh', '12345678'
DIAGS = []
WHOLE_BOARD = list(map(''.join, product(COLS, ROWS)))
D1 =[['a1'], ['a2', 'b1'], ['a3', 'b2', 'c1'], ['a4', 'b3', 'c2', 'd1'], ['a5', 'b4', 'c3', 'd2', 'e1'], ['a6', 'b5', 'c4', 'd3', 'e2', 'f1'], 
     ['a7', 'b6', 'c5', 'd4', 'e3', 'f2', 'g1'], ['a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'], ['h2', 'g3', 'f4', 'e5', 'd6', 'c7', 'b8'], 
     ['h3', 'g4', 'f5', 'e6', 'd7', 'c8'], ['h4', 'g5', 'f6', 'e7', 'd8'], ['h5', 'g6', 'f7', 'e8'], ['h6', 'g7', 'f8'], ['h7', 'g8'], ['h8']]

D2 = [['a8'], ['a7', 'b8'], ['a6', 'b7', 'c8'], ['a5', 'b6', 'c7', 'd8'], ['a4', 'b5', 'c6', 'd7', 'e8'], ['a3', 'b4', 'c5', 'd6', 'e7', 'f8'], 
      ['a2', 'b3', 'c4', 'd5', 'e6', 'f7', 'g8'], ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'], ['h7', 'g6', 'f5', 'e4', 'd3', 'c2', 'b1'], 
      ['h6', 'g5', 'f4', 'e3', 'd2', 'c1'], ['h5', 'g4', 'f3', 'e2', 'd1'], ['h4', 'g3', 'f2', 'e1'], ['h3', 'g2', 'f1'], ['h2', 'g1'], ['h1']]


def col_row_diagonals_to_eliminate(coord):
    col = coord[0]
    row = coord[1]
    
    diag1 = [item for item in D1 if coord in item]
    diag2 = [item for item in D2 if coord in item]
    
    elements_from_diags = {item for sublist in diag1 for item in sublist} | {item for sublist in diag2 for item in sublist}
    
    return col, row, elements_from_diags


def eliminate_columns_and_rows(cols, rows):
    cols_all, rows_all = list(COLS), list(ROWS)
    
    cols_ok = [item for item in cols_all if item not in cols]
    rows_ok = [item for item in rows_all if item not in rows]
    
    return cols_ok, rows_ok


def eliminate_diagonals(placed):
    cols, rows, all_elements_from_diags = list(), list(), set()
    
    for coord in placed:
        col, row, elements_from_diags = col_row_diagonals_to_eliminate(coord)
        #print(col, row, elements_from_diags)
        cols.append(col)
        rows.append(row)
        all_elements_from_diags = all_elements_from_diags.union(elements_from_diags)
    
    cols_ok, rows_ok = eliminate_columns_and_rows(cols, rows)
    #print(f'Remaining cols and rows: cols_list = {cols_ok}, rows_list = {rows_ok}')
    
    # after eliminating the columns and the rows
    remaining_board = list(map(''.join, product(cols_ok, rows_ok)))
    #print(f'Remaining board after eliminating cols and rows = {remaining_board}')
    
    # eliminating the elements in diagonals
    #print(f'All elements from diags for eliminating = {sorted(all_elements_from_diags)}')
    remaining_board = [item for item in remaining_board if item not in all_elements_from_diags]
    #print(f'Remaining board after eliminating diagonals = {remaining_board}')
    
    return remaining_board
    

def calculate_all_combinations(placed, remaining_board):
    print(f'placed = {placed}')
    placed_queens = len(placed)
    print(f'placed_queens = {placed_queens}')
    q = 8 - placed_queens # how many more queens must be placed
    print(f'q = {q}')
    
    # calculate combinations of remaining queens from remaining_board
    # if len(remaining_board) > q:
    #     remaining_board_combinations = list(combinations(remaining_board, 4))
    #     return remaining_board_combinations
    # elif len(remaining_board) == q:
    #     remaining_board_combinations = placed | remaining_board
    #     return remaining_board_combinations
    # else:
    #     print('No remaining_board_combinations')
    #     return []
    
    remaining_board_combinations = list(combinations(remaining_board, q))
    return remaining_board_combinations

def verify_all_8_queens(new_placed):
    elements_for_all_queens = list()

    for coord in new_placed:
        col, row, elements_from_diags = col_row_diagonals_to_eliminate(coord)
        print(f'row = {row}, col = {col}')
        print(f'elements_from_diags = {elements_from_diags}')
        elements_from_row = {item for item in WHOLE_BOARD if item[1] == row}
        print(f'elements_from_row = {elements_from_row}')
        elements_from_col = {item for item in WHOLE_BOARD if item[0] == col}
        print(f'elements_from_col = {elements_from_col}')
        all_elements = elements_from_row | elements_from_col | elements_from_diags
        all_elements.discard(coord)
        elements_for_all_queens.append(tuple(sorted(all_elements)))
        print(elements_for_all_queens)
        
    for coord in new_placed:
        for queen in elements_for_all_queens:
            if coord in queen:
                verification = False
                print(verification)
                return elements_for_all_queens, verification
    
    verification = True                 
    return elements_for_all_queens, verification

def verify_placed_queens_(placed):
    elements_for_placed_queens = list()

    for coord in placed:
        col, row, elements_from_diags = col_row_diagonals_to_eliminate(coord)
        print(f'row = {row}, col = {col}')
        print(f'elements_from_diags = {elements_from_diags}')
        elements_from_row = {item for item in WHOLE_BOARD if item[1] == row}
        print(f'elements_from_row = {elements_from_row}')
        elements_from_col = {item for item in WHOLE_BOARD if item[0] == col}
        print(f'elements_from_col = {elements_from_col}')
        all_elements = elements_from_row | elements_from_col | elements_from_diags
        all_elements.discard(coord)
        elements_for_placed_queens.append(tuple(sorted(all_elements)))
        
    for coord in placed:
        for queen in elements_for_placed_queens:
            if coord in queen:
                verification = False
                print(verification)
                return elements_for_placed_queens, verification
    
    verification = True                 
    return elements_for_placed_queens, verification


def verify_placed_queens(placed):
    # create a dictionary having as keys all placed queens and as values the column, row, diag1, diag2
    placed_dictionary = {}
    for queen in placed:
        c = queen[0]
        r = queen[1]
        diag1 = [item for item in D1 if queen in item]
        diag1 = [item for subitem in diag1 for item in subitem]
        diag2 = [item for item in D2 if queen in item]
        diag2 = [item for subitem in diag2 for item in subitem]
        placed_dictionary[queen] = [c, r, diag1, diag2]
    
    print(f'placed_dictionary = {placed_dictionary}')
    
    values = list(placed_dictionary.values())
    values = [item for subitem in values for item in subitem]
    print(f'values = {values}')
    
    dup = [item for item in values if values.count(item) > 1]
    print(f'dup = {dup}')
    
    if len(dup) >= 1:
        verification_placed = False
    else:
        verification_placed = True
        
    return verification_placed

    
    
def place_queens_(placed):
    print(f'placed = {placed}')
    verification_placed = verify_placed_queens(placed)
    print(f'verification_placed = {verification_placed}')
    if not verification_placed:
        return set()
    
    remaining_board = eliminate_diagonals(placed)
    print(f'Remaining board after eliminating diagonals = {remaining_board}')

    if len(remaining_board) == 1:
        new_placed = placed | set(remaining_board)
        elements_for_all_queens, verification = verify_all_8_queens(new_placed)
        return new_placed if verification else set()
    
    remaining_board_combinations = calculate_all_combinations(placed, remaining_board)
    print(f'remaining_board_combinations = {remaining_board_combinations}')
    
    if remaining_board_combinations == []:
        return set()
    
    for i in range(len(remaining_board_combinations) - 1):
        new_placed = placed | set(remaining_board_combinations[i])
        print(f'new_placed = {new_placed}')
        elements_for_all_queens, verification = verify_all_8_queens(new_placed)
        print(f'elements_for_all_queens = {elements_for_all_queens}')
        print(f'verification = {verification}')
        if verification:
            print(f'FINAL new_placed = {new_placed}')
            return new_placed
        
    return set()
    


# Best Solution: https://py.checkio.org/mission/place-queens/publications/StefanPochmann/python-3/permutations/?ordering=most_voted&filtering=all

from itertools import permutations

def place_queens(placed):
    print(f'permutations("abcdefgh") = {list(permutations("abcdefgh"))}')
    for p in permutations('abcdefgh'):
        full = {c+r for c, r in zip(p, '12345678')}
        #print(f'full = {full}')
        if placed <= full and len({ord(c) + ord(r) * m for c, r in full for m in (1, -1)}) == 16:
            print(f'full OK = {full}')
            return full
    return set()





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import combinations
    COLS = "abcdefgh"
    ROWS = "12345678"

    THREATS = {c + r: set(
        [c + ROWS[k] for k in range(8)] +
        [COLS[k] + r for k in range(8)] +
        [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8] +
        [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
               for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}

    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example" # a5", "f3", "g1", "h7
    assert checker(place_queens, {"b2", "c4", "d6", "e8", "a7", "g5"}, False), "2nd Example"
    assert checker(place_queens, {"a5", "b7", "c1", "e2", "f8", "g6", "h3"}, True)
    assert checker(place_queens, {"a1", "h8"}, False)

    print('Done!')