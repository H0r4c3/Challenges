'https://py.checkio.org/en/mission/ryerson-letter-grade/'

'''
Given the grade percentage for the course, calculate and return the letter grade that would appear in the Ryerson’s grade transcript, 
as defined on the page Ryerson Grade Scales . The letter grade should be returned as a string that consists of the uppercase letter 
followed by the possible modifier "+" or "-" .

Input: Int. Grade percentage.

Output: Str. The letter grade.
'''

# feel free to change table structure in any way

TABLE = '''
A+ 90-150%
A 85-89%
A- 80-84%
B+ 77-79%
B 73-76%
B- 70-72%
C+ 67-69%
C 63-66%
C- 60-62%
D+ 57-59%
D 53-56%
D- 50-52%
F 0-49%
'''

def ryerson_letter_grade(pct: int) -> str:
    table_list = TABLE.split()
    
    # Convert the 'TABLE' to a dictionary converting the list 'table_list'
    table_dict = {table_list[i] : range(int(table_list[i+1][:-1].split('-')[0]), int((table_list[i+1][:-1].split('-')[1]))+1) for i in range(0, len(table_list), 2)}
    
    print(table_list)
    print(table_dict)

    for g, p in table_dict.items():
        if pct in p:
            return g
        

# Best Solution: 
# https://py.checkio.org/mission/ryerson-letter-grade/publications/veky/python-3/no-thanks/?ordering=most_voted&filtering=all

def ryerson_letter_grade_(pct: int) -> str:
    for line in filter(None, TABLE.splitlines()):
        grade, range = line.rstrip('%').split()
        down, up = map(int, range.split('-'))
        if down <= pct <= up: return grade
    return 'A+' if pct >= 90 else 'F'


if __name__ == '__main__':
    print("Example:")
    print(ryerson_letter_grade(45))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert ryerson_letter_grade(45) == "F"
    assert ryerson_letter_grade(62) == "C-"
    print("Coding complete? Click 'Check' to earn cool rewards!")