import random
import json
import os
import sys


def main_game_loop():
    if os.path.exists(json_file_path):
        print("список слов обнаружен")
        with open(json_file_path, "r", encoding="utf-8") as read_file:
            words = json.load(read_file)
#        print(words)
    else:
        words = []
    while True:
        if len(words) == 0:
            sys.exit()
#        print(len(words))
        index = random.randint(0, len(words)-1)
        secret_word = words[index]
        words.pop(index)
        secret_word_boolean = generate_word_check(secret_word)
        used_letters_list = []
        game_state(secret_word, secret_word_boolean, 0, used_letters_list)


def win_condition(secret_word_boolean):
    return all(secret_word_boolean)


def check_if_there(letter, secret_word, secret_word_boolean):
    for i in range(len(secret_word)):
        if letter.lower() == secret_word[i]:
            secret_word_boolean[i] = True
    return secret_word_boolean


def generate_word_check(string):
    return [False] * len(string)


def game_state(secret_word, secret_word_boolean,
               turns_taken, used_letters_list):
    interface(secret_word, secret_word_boolean, turns_taken)
    print('Использованные буквы:')
    print(used_letters_list)
    guess = input_handler()
    print(guess)
    if guess not in used_letters_list:
        turns_taken = turns_taken+1
        secret_word_boolean = check_if_there(guess,
                                             secret_word, secret_word_boolean)
        used_letters_list = used_letters(used_letters_list, guess)

        if win_condition(secret_word_boolean) is True:
            print('Вы угадали слово!')
            interface(secret_word, secret_word_boolean, turns_taken)
            print('Вы угадали слово за %i ходов' % turns_taken)
#            sys.exit()
            return
        game_state(secret_word, secret_word_boolean,
                   turns_taken, used_letters_list)
    elif guess in used_letters_list:
        print('Эта буква уже была использована!')
        game_state(secret_word, secret_word_boolean,
                   turns_taken, used_letters_list)
    return


def interface(secret_word, secret_word_boolean, turns_taken):
    print("Слово из %i букв:" % len(secret_word))
    for i in range(len(secret_word)):
        if secret_word_boolean[i] is True:
            print(secret_word[i], end='')
        else:
            print('_', end='')
    print()
    print('Ходов сделано: %i' % turns_taken)


def used_letters(used_letters_list, letter):
    used_letters_list.append(letter)
    return used_letters_list


def input_handler():
    print('Введите букву:')
    while True:
        input_letter = input('> ')
        if input_letter.lower() == 'cancel':
            sys.exit()
        elif input_letter.lower() in allowed_inputs:
            return input_letter
        else:
            print('Напишите букву, или комманду (cancel) чтобы выйти!')


allowed_inputs = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
                  'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                  'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
script_dir = os.path.dirname(os.path.realpath(__file__))
path = 'json\\words.json'
json_file_path = os.path.join(script_dir, path)


main_game_loop()
