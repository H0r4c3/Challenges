'https://py.checkio.org/en/mission/binary-count/'

'''
You are given a number (a positive integer). You should convert it to the binary format and count how many unities (1) are in the number spelling. 
For example: 5 = 0b101 contains two unities, so the answer is 2.

Input: A number as a positive integer.

Output: The quantity of unities in the binary form as an integer.
'''

def checkio(number: int) -> int:
    # Binary representation is done by the addition of prefix "0b"
    binary = bin(number).lstrip("0b")
    print(f'Binary form of {number} is {binary}')
    return binary.count('1')


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    print("Done!")