'https://py.checkio.org/en/mission/multiplication-table/'

'''
We convert numbers to binary representation without leading zeroes. 
Then the first number is written vertically (up to down) and the second horizontally (left to right). 
With that, we fill a table with various binary operations for each crossing -- AND, OR, XOR, so we end up with three tables. 
In each table we convert rows to decimal and summarize it, then summarize the results of three tables.
'''

def checkio(first, second):
    result = 0
    for oper in ('&', '|', '^'):
        rows_sum = 0
        for i in bin(first)[2:]:
            rows = ''
            for j in bin(second)[2:]:
                rows += eval(f'str(int(i) {oper} int(j))')
            rows_sum += int(rows, 2)
        result += rows_sum
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18