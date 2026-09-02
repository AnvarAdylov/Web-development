import random
import sys
import math

   
def reverse_guess_number(answer, guess):
        if guess > answer:
            return 'less'
        elif guess == answer:
            return 'yes'
        else:
            return 'greater'

def recursive_guess_number(lowest,total, count, solution):
    attempt =  (total+lowest)/2
    attempt = math.floor(attempt)
    guess = reverse_guess_number(solution, attempt)
    if guess.lower() == 'greater':
        return recursive_guess_number(attempt,total, count+1,solution)
    elif guess.lower() == 'less':
        return recursive_guess_number(lowest,attempt, count+1,solution)
    elif guess.lower() == 'yes':
        return (count+1)


def recursive_random_guess_number(lowest,total, count,solution):
    attempt = random.randint(lowest,total)
    guess = reverse_guess_number(solution, attempt)
    if guess.lower() == 'greater':
        return recursive_guess_number(attempt,total, count+1,solution)
    elif guess.lower() == 'less':
        return recursive_guess_number(lowest,attempt, count+1,solution)
    elif guess.lower() == 'yes':
        return (count+1)
      
average_binary = []
average_random = []
for i in range (100):
    temp = random.randint(1,100)
    average_binary.append(recursive_guess_number(1,100,0,temp))
    average_random.append(recursive_random_guess_number(1,100,0,temp))
print(average_binary)
print(average_random)

