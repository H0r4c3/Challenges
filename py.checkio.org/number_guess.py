'https://py.checkio.org/en/mission/number-guess/'

'''
You are given an unknown number within the range of 1 to 100, inclusive. 
Your task is to guess what the number is by performing a series of guesses .

Your solution will need to guess the number by submitting an integer divisor ranging from 2 to 10, and the number you guessed . 
At each attempt you will get information as a list of tuples. 
Each tuple contains the remainder result along with your previous divisor.
'''

def checkio(attempts):
    print(f'attempts = {attempts}')
    divisors = set(range(2, 11))
    numbers = set(range(1, 101))
    
    #number = divisor * quotient + remainder
    
    for remainder, divisor in attempts:
        print(f'rem = {remainder}, divisor = {divisor}')
        divisors.discard(divisor)
        print(f'divisors = {divisors}')
        for number in range(1, 101):
            if number % divisor != remainder:
                numbers.discard(number)
                #print(f'numbers = {numbers}')
                if len(numbers) == 1:
                    return [min(divisors), list(numbers)[0]]
                       
    print(f'Result [divisor, number] = {[min(divisors), min(numbers)]}')
    return [min(divisors), min(numbers)]



# Best Solution: https://py.checkio.org/mission/number-guess/publications/Moff/python-3/first/share/29aa71795fe9a22b3a975f3f1cee6d89/

def checkio_(attempts):
    print(attempts)
    unused_divisors = set(range(2, 11))
    nums = set(range(1, 101))
    for rem, divisor in attempts:
        unused_divisors.discard(divisor)
        for i in range(1, 101):
            if i % divisor != rem:
                nums.discard(i)
    return min(unused_divisors), min(nums)


# Best Solution: https://py.checkio.org/mission/number-guess/publications/artakase/python-3/first/?ordering=most_voted&filtering=all

def checkio_(attempts):
    if len(attempts) == 1:
        return [10, 100]
    elif len(attempts) == 2:
        rem_10 = attempts[1][0]
        return [9, 90 + rem_10]
    else:
        rem_10, rem_9 = attempts[1][0], attempts[2][0]
        return [2, ((rem_9 - rem_10) % 10) * 9 + rem_9]


if __name__ == "__main__":
    # This part is using only for self-checking and not necessary for auto-testing
    MAX_ATTEMPT = 8

    def initial_referee(data):
        data["attempt_count"] = 0
        data["guess"] = 0
        return data

    def check_solution(func, goal, initial):
        prev_steps = [initial]
        for attempt in range(MAX_ATTEMPT):
            divisor, guess = func(prev_steps[:])
            if guess == goal:
                return True
            if divisor <= 1 or divisor > 10:
                print("You gave wrong divisor range.")
                return False
            if guess < 1 or guess > 100:
                print("You gave wrong guess number range.")
                return False
            prev_steps.append((goal % divisor, divisor))
        print("Too many attempts.")
        return False

    assert check_solution(checkio, 47, (2, 5)), "1st example"
    assert check_solution(checkio, 94, (3, 7)), "2nd example"
    assert check_solution(checkio, 52, (0, 2)), "3rd example"
    
    print('Done!')