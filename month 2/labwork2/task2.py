import random
import sys

def is_allowed_input(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Ошибка неверный тип данных попробуйте еще раз")
        return False

def check(input):
    if input.lower() == 'exit':
        sys.exit()
    else:
        return input

def game():
    while True:
        menu_caption = '< Main menu >'
        print(menu_caption.center(50))
        print("To let ai guess your number enter - my turn")
        print("To guess number chooen by ai enter - your turn")
        command = check(input('> '))
        if command.lower() == 'my turn':
            recursive_guess_number(1,100,0)
            #recursive_random_guess_number(1,100,0)
        elif command.lower() == 'your turn':
            try_guessing()

def recursive_guess_number(lowest,total, count):
    print("is it %i"% int((total+lowest)/2))
    guess = check(input('> '))
    if guess.lower() == 'greater':
        return recursive_guess_number(int((total+lowest)/2),total, count+1)
    elif guess.lower() == 'less':
        return recursive_guess_number(lowest,int((total+lowest)/2), count+1)
    elif guess.lower() == 'yes':
        print("Got it in %i steps!" % (count+1))
        #return int((total+lowest)/2), count+1
    else:
        return recursive_guess_number(lowest,total, count)

def recursive_random_guess_number(lowest,total, count):
    attempt = random.randint(lowest,total)
    print("is it %i"% attempt)
    guess = check(input('> '))
    if guess.lower() == 'greater':
        return recursive_guess_number(attempt,total, count+1)
    elif guess.lower() == 'less':
        return recursive_guess_number(lowest,attempt, count+1)
    elif guess.lower() == 'yes':
        print("Got it in %i steps!" % (count+1))
        #return attempt, count+1
    else:
        return recursive_guess_number(lowest,total, count)
      
def reverse_guess_number(answer, count):
        print("Make your guess:")
        while True:
            guess = check(input('> ')))
            if is_allowed_input(guess):
                guess = int(guess)
                break    
        if guess > answer:
            print('less')
            reverse_guess_number(answer, count+1)
        elif guess < answer:
            print('greater')
            reverse_guess_number(answer, count+1)
        elif guess == answer:
            print('yes')
            print("Got it in %i steps!" % (count+1))
            #return (count+1)

def try_guessing():
    sol = random.randint(1,100)
    reverse_guess_number(sol,0)





game()