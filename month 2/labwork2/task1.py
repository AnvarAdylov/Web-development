import random
def recursive_guess_number(lowest,total, count):
    print("is it %i"% int((total+lowest)/2))
    guess = input("> ")
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
    guess = input("> ")
    if guess.lower() == 'greater':
        return recursive_guess_number(attempt,total, count+1)
    elif guess.lower() == 'less':
        return recursive_guess_number(lowest,attempt, count+1)
    elif guess.lower() == 'yes':
        print("Got it in %i steps!" % (count+1))
        #return attempt, count+1
    else:
        return recursive_guess_number(lowest,total, count)

#print(recursive_guess_number(0,100,0))
recursive_guess_number(0,100,0)
#print(recursive_random_guess_number(0,100, 0))
recursive_random_guess_number(0,100, 0)