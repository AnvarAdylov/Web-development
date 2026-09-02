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
        print("To compete with ai enter - versus")
        command = check(input('> '))
        if command.lower() == 'my turn':
            while True:
                print("pick difficulty:(easy,hard)")
                difficulty = check(input('> '))
                if difficulty.lower() == 'easy':recursive_random_guess_number(1,100,0); break
                elif difficulty.lower() == 'hard':recursive_guess_number(1,100,0); break
        elif command.lower() == 'your turn':
            try_guessing()
        elif command.lower() == 'versus':
            sequential_play()

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
        return (count+1)
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
        return attempt, count+1
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
            return reverse_guess_number(answer, count+1)
        elif guess < answer:
            print('greater')
            return reverse_guess_number(answer, count+1)
        elif guess == answer:
            print('yes')
            print("Got it in %i steps!" % (count+1))
            return (count+1)

def round_easy(player_score,ai_score):
    print("Computer guessing:")
    ai_attempt = recursive_random_guess_number(1,100, 0)
    print("Player guessing:")
    player_attempt = try_guessing()
    if player_attempt > ai_attempt:
        return player_score, ai_score+1
    elif player_attempt < ai_attempt:
        return player_score+1, ai_score
    elif player_attempt == ai_attempt:
        return player_score, ai_score 
    
def round_hard(player_score,ai_score):
    print("Computer guessing:")
    ai_attempt = recursive_guess_number(1,100, 0)
    print("Player guessing:")
    player_attempt = try_guessing()
    if player_attempt > ai_attempt:
        return player_score, ai_score+1
    elif player_attempt < ai_attempt:
        return player_score+1, ai_score
    elif player_attempt == ai_attempt:
        return player_score, ai_score 
  
def sequential_play():
    print("How many rounds you would like to play?")
    amount_rounds = check(input('> '))
    mode = False
    if amount_rounds == '':
        amount_rounds = 3
    else:
        amount_rounds = int(amount_rounds)
    while True:    
        print("pick difficulty:(easy,hard)")
        difficulty = check(input('> '))
        if difficulty.lower() == 'easy':mode = False; break
        elif difficulty.lower() == 'hard':mode = True; break
    player_total_score = 0
    ai_total_score = 0
    for i in range (amount_rounds):
        print('_________________________________________')
        print("Round %i" %i)
        print('_________________________________________')
        if mode:
            player_total_score, ai_total_score = round_hard(player_total_score,ai_total_score)
        else:    
            player_total_score, ai_total_score = round_easy(player_total_score,ai_total_score)
    print("Player got %i wins" %player_total_score)
    print("Opponent got %i wins" %ai_total_score)
    if player_total_score > ai_total_score:
        print("Player won")
    elif player_total_score < ai_total_score:
        print("Player lost")
    elif player_total_score == ai_total_score:
        print("Draw")

def try_guessing():
    sol = random.randint(1,100)
    return reverse_guess_number(sol,0)




game()