'https://py.checkio.org/en/mission/cryptarithmetic-puzzle/'

'''
This is a mission to create a solver for the cryptarithmetic puzzle. 
In this puzzle, each letter must be assigned a one-digit number to complete the calculation.

You are given a list of words. The last word is the sum. You have to return a dictionary with the alphabets as keys and the one-digit numbers as values.

NOTE:

Each letter should represent a different digit.
The leading digit of a multi-digit number must not be zero.
All tests always have one answer.

Additional Tips
Pre-check Constraints: For example, the sum of the digits for SEND + MORE must match the number of digits in MONEY.
Performance: Use Python's multiprocessing module to parallelize testing of permutations if the problem is large.
Libraries: Consider using constraint-solving libraries like z3 for more complex puzzles.
'''

# Solution nr. 1 - all possibilities (Brute Force):

from itertools import combinations, permutations

def generate_grouped_permutations(start, end, group_size):
    numbers = list(range(start, end + 1))
    all_grouped_permutations = []

    for perm in permutations(numbers, group_size):
        all_grouped_permutations.append(perm)

    return all_grouped_permutations


def conversion(word, solution):
    number = ''
    for letter in word:
        number += str(solution[letter])
    number = int(number)
    
    return number


def possible_solution(words, all_letters, all_comb_numbers, idx):
    solution = dict(zip(all_letters, all_comb_numbers[idx]))
    numbers = [conversion(words[i], solution) for i in range(len(words))]
    
    return solution, numbers

def cryptarithm_solver_(words: str) -> dict[str, int]:
    all_letters = sorted({letter for word in words for letter in word})
    all_numbers = list(range(10))
    all_comb_numbers = list(combinations(all_numbers, len(all_letters)))
    for item in all_comb_numbers:
        permutation_numbers = list(permutations(item))
        all_comb_numbers.extend(permutation_numbers)

    print(all_letters)
    print(all_numbers)
    print(all_comb_numbers)
    
    for idx in range(len(all_comb_numbers)):
        solution, numbers = possible_solution(words, all_letters, all_comb_numbers, idx)
        #print(solution)
        #print(numbers)
        if sum(numbers[:-1]) == numbers[-1]:
            print(solution)
            return solution
        

# 2. ChatGPT:

from itertools import permutations

def cryptarithm_solver_(words: str) -> dict[str, int]:
    sum_word = words[-1]
    unique_letters = set(''.join(words))
    
    if len(unique_letters) > 10:
        raise ValueError("More than 10 unique letters is not supported.")
    
    for perm in permutations(range(10), len(unique_letters)):
        letter_to_digit = dict(zip(unique_letters, perm))
        
        def word_to_number(word):
            return int(''.join(str(letter_to_digit[letter]) for letter in word))
        
        if sum(word_to_number(word) for word in words[:-1]) == word_to_number(sum_word):
            return letter_to_digit
    
    return None

# 3. ChatGPT: OK OK OK

from itertools import permutations

def cryptarithm_solver(words: str) -> dict[str, int]:
    # Parse the equation
    left = words[0:-1]
    right = words[-1]
    all_letters = set("".join(left) + right)
    
    # Generate all possible digit mappings
    if len(all_letters) > 10:
        print("Too many unique letters for a valid cryptarithmetic puzzle!")
        return
    
    # Solve using permutations of digits
    for perm in permutations(range(10), len(all_letters)):
        letter_to_digit = dict(zip(all_letters, perm))
        
        # Check for leading zeros
        if any(letter_to_digit[word[0]] == 0 for word in words + [right]):
            continue
        
        # Convert words to numbers
        word_values = [sum(letter_to_digit[c] * 10**i for i, c in enumerate(word[::-1])) for word in words]
        right_value = sum(letter_to_digit[c] * 10**i for i, c in enumerate(right[::-1]))
        
        #print(word_values[:-1])
        #print(right_value)
        #print()
        
        # Check if the equation holds
        if sum(word_values[:-1]) == right_value:
            # Print the solution
            solution = {letter: letter_to_digit[letter] for letter in sorted(all_letters)}
            print("Solution found!")
            print(f"Mapping: {solution}")
            for word, value in zip(words + [right], word_values + [right_value]):
                print(f"{word} = {value}")
            
            solution = dict(sorted(solution.items(), key=lambda item: item[1]))
            print(f"Solution: {solution}")
                
            return solution
    
    print("No solution found!")
            
            
# 4. ChatGPT:

from itertools import permutations
from z3 import Solver, Int, Distinct

def cryptarithm_solver_(words: str) -> dict[str, int]:
    # Parse the equation
    left = words[0 : -1]
    right = words[-1]
    all_letters = set("".join(left) + right)
    
    # Generate all possible digit mappings
    if len(all_letters) > 10:
        print("Too many unique letters for a valid cryptarithmetic puzzle!")
        return
    
    # Create a Z3 solver instance
    solver = Solver()
    
    # Create variables for each unique letter
    letter_vars = {letter: Int(letter) for letter in all_letters}
    
    # Add constraints: each letter must be a digit (0–9)
    for letter in letter_vars:
        solver.add(letter_vars[letter] >= 0, letter_vars[letter] <= 9)
    
    # Add the constraint that all digits must be distinct
    solver.add(Distinct(*letter_vars.values()))
    
    # Add the constraint that no word has a leading zero
    for word in words + [right]:
        solver.add(letter_vars[word[0]] != 0)
    
    # Convert words to their numerical representation
    def word_to_number(word):
        return sum(letter_vars[c] * 10**i for i, c in enumerate(word[::-1]))
    
    # Add the main equation as a constraint
    left_sum = sum(word_to_number(word) for word in words)
    right_number = word_to_number(right)
    solver.add(left_sum == right_number)
    
    # Solve the puzzle
    if solver.check() == "sat":
        model = solver.model()
        solution = {str(var): model[letter_vars[var]].as_long() for var in all_letters}
        print("Solution found!")
        print(f"Mapping: {solution}")
        for word in words + [right]:
            number = sum(solution[c] * 10**i for i, c in enumerate(word[::-1]))
            print(f"{word} = {number}")
    else:
        print("No solution found!")

    
# BEST SOLUTION: 
# https://py.checkio.org/mission/cryptarithmetic-puzzle/publications/przemyslaw.daniel/python-3/12-liner-slow/?ordering=most_voted&filtering=all

from itertools import permutations


def cryptarithm_solver_(words: str) -> dict[str, int]:
    letters = list(set("".join(words)))
    for digits in permutations("0123456789", r=len(letters)):
        result = dict(zip(letters, digits))
        numbers = [''.join(result[letter] for letter in word) for word in words]
        if any(number[0] == "0" for number in numbers):
            continue
        if sum(map(int, numbers[:-1])) == int(numbers[-1]):
            return {letter: int(digit) for letter, digit in result.items()}
        
        
        

print("Example:")
#print(cryptarithm_solver(["SEND", "MORE", "MONEY"]))

# These "asserts" are used for self-checking
assert cryptarithm_solver(["SEND", "MORE", "MONEY"]) == {
    "O": 0,
    "M": 1,
    "Y": 2,
    "E": 5,
    "N": 6,
    "D": 7,
    "R": 8,
    "S": 9,
}
assert cryptarithm_solver(["BLACK", "GREEN", "ORANGE"]) == {
    "C": 0,
    "O": 1,
    "A": 2,
    "R": 3,
    "E": 4,
    "G": 5,
    "N": 6,
    "B": 7,
    "K": 8,
    "L": 9,
}
assert cryptarithm_solver(["POTATO", "TOMATO", "PUMPKIN"]) == {
    "U": 0,
    "P": 1,
    "N": 2,
    "M": 3,
    "A": 4,
    "O": 6,
    "I": 7,
    "T": 8,
    "K": 9,
}
assert cryptarithm_solver(["KYOTO", "OSAKA", "TOKYO"]) == {
    "A": 0,
    "Y": 1,
    "S": 2,
    "O": 3,
    "K": 4,
    "T": 7,
}

print("The mission is done! Click 'Check Solution' to earn rewards!")