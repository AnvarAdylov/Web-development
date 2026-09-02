import json
import os
import sys


def add(movie_title, movie_reviews_list):
    temp_dictionary = {'name': movie_title, 'ratings': {}}
    movie_reviews_list.append(temp_dictionary)


def average_rating(movie_name, reviews):
    temp_ratings = reviews[find_movie(movie_name, reviews)]['ratings']
    sum = 0
    for reviewer, rating in temp_ratings.items():
        sum = sum + rating
    if (len(temp_ratings) == 0):
        return 'No ratings in the database'
    else:
        return sum/len(temp_ratings)


def calculate_average(ratings):
    if not ratings:
        return 0
    return sum(ratings.values()) / len(ratings)


def check_if_valid(user_input):
    try:
        float_value = float(user_input)
        if float_value >= 0 and float_value <= 10:
            return float_value
        else:
            print('Недопустимая оценка! Введите оценку в пределах 10 баллов')
    except ValueError:
        print('Недопустимая оценка!')
        return None


def command_list(command, movie_reviews_list):
    if command.lower() == 'add':
        print("Введите имя фильма, который вы хотите добавить в базу:")
        new_movie = input('> ')

        if duplicate(new_movie, movie_reviews_list):
            print("Этот фильм уже есть в базе!")
        else:
            add(new_movie, movie_reviews_list)
    elif command.lower() == 'delete':
        print("Введите имя фильма, который вы хотите удалить:")
        deleted_movie = input('> ')

        if duplicate(deleted_movie, movie_reviews_list):
            print("Вы уверены, что хотите удалить фильм " +
                  deleted_movie + " включая все его оценки?")
            temp = input('> ')

            if (temp.lower() == 'yes' or
                    temp.lower() == 'ok' or temp.lower() == 'да'):
                delete_movie(deleted_movie, movie_reviews_list)
                print("Контакт удален успешно")
        else:
            print("Данного фильма нет в базе!")
    elif command.lower() == 'list':
        list_movies(movie_reviews_list)
    elif command.lower() == 'sort':
        sorted_movies = sorted(movie_reviews_list, key=lambda x:
                               calculate_average(x.get('ratings',
                                                       {})),
                               reverse=True)
        list_movies(sorted_movies)
    elif command.lower() == 'rate':
        print("Введите имя фильма, который вы хотите оценить:")
        rated_movie = input('> ')
        if duplicate(rated_movie, movie_reviews_list):
            print("Введите ваше имя:")
            reviewer = input('> ')
            rate(reviewer, rated_movie, movie_reviews_list)
            rigged_reviews(rated_movie, reviewer, movie_reviews_list)
        else:
            print("Этот фильм отсутствует в базе! Хотите ли вы добавить его?")
            temp_command = input('> ')
            if (temp_command.lower() == 'yes' or
                    temp_command.lower() == 'ok' or
                    temp_command.lower() == 'да'):
                print('Вы можете добавить фильм использую команду - add')
            else:
                print('Добавьте фильм перед тем как оценивать!')

    elif command.lower() == 'find':
        print("Введите имя фильма, оценки которого вы хотите посмотреть:")
        searched_movie = input('> ')

        if duplicate(searched_movie, movie_reviews_list):
            find_and_print(searched_movie, movie_reviews_list)
        else:
            print("Данного фильма нет в базе!")
    elif command.lower() == 'exit':
        save_movies(movie_reviews_list)
        sys.exit()
    else:
        print("Неизвестная команда!")


def delete_movie(movie_deleted, movie_review_list):
    movie_review_list.pop(find_movie(movie_deleted, movie_review_list))


def duplicate(search_name, movie_database):
    if find_movie(search_name, movie_database) is not None:
        return True
    else:
        return False


def find(search_name, movie_name, movie_review_list):
    temp_dict = movie_review_list[movie_name]['ratings']
    for i in range(len(movie_review_list)):
        if temp_dict[i]['name'].lower() == search_name.lower():
            return i
    return None


def find_and_print(search_movie, reviews_list):
    temp_index = find_movie(search_movie, reviews_list)
    temp_dict = reviews_list[temp_index]['ratings']
    print("Name:                            | Rating:")
    for reviewer, rating in temp_dict.items():
        print(reviewer.ljust(33) + '|   ', end='')
        print(rating)
    if len(temp_dict) == 0:
        print('No reviews were made')
    else:
        print("Average rating of the movie: %.2f" %
              average_rating(reviews_list[temp_index]['name'], reviews_list))


def find_movie(search_movie, movie_review_list):
    for i in range(len(movie_review_list)):
        if movie_review_list[i]['name'].lower() == search_movie.lower():
            return i
    return None


def list_movies(movie_list):
    print("Movie:                            | Average rating:")
    for i in range(len(movie_list)):
        print(movie_list[i]['name'].ljust(34) + '|  ', end='')
        temp_ratings = movie_list[i]['ratings']
        print(average_rating(movie_list[i]['name'], movie_list))


def main_programm(contacts):
    command = input('> ')
    command_list(command, contacts)


def movie_reviews_json():
    if os.path.exists(json_file_path):
        print("Сохраненная база загружена")
        with open(json_file_path, "r") as read_file:
            movies = json.load(read_file)
#        print(movies)
    else:
        print("База оценок кинофильмов отсутсвует!")
        print("Не желаете добавить новые оценки фильмов?")
        print("Используйте комманду - 'add'")
        movies = []
    programm_menu()
    while True:
        main_programm(movies)


def programm_menu():
    print("║             Добро пожаловать в программу           ║")
    print("║                 для оценки фильмов                 ║")
    print()
    print("║ Список доступных комманд:                          ║")
    print("║ list  - вывести список фильмов и их средние оценки ║")
#    print("║ menu - вывести меню снова                       ║")
    print("║ add   - добавить фильм в базу                      ║")
    print("║ rate  - оценить фильм                              ║")
    print("║ sort  - вывести отсортированный список фильмов     ║")
    print("║ find  - показать все оценки фильма                 ║")
    print("║ delete - удалить фильм из базы                     ║")
    print("║ exit   - выход                                     ║")


def rate(reviewer_name, movie_name, movie_review_list):
    print("Введите оценку которую вы хотите дать данному фильму:")
    while True:
        movie_rating = input('> ')
        movie_rating = check_if_valid(movie_rating)
        if movie_rating is not None:
            movie_index = find_movie(movie_name, movie_review_list)
            movie_ratings = movie_review_list[movie_index]['ratings']

            if reviewer_name in movie_ratings:
                movie_ratings[reviewer_name] = movie_rating
                break
            else:
                movie_ratings[reviewer_name] = movie_rating
                break


def rigged_reviews(movie_name, reviewer_name, movie_review_list):
    movie_index = find_movie(movie_name, movie_review_list)
    movie_ratings = movie_review_list[movie_index]['ratings']

    if reviewer_name in movie_ratings and movie_ratings[reviewer_name] == 0:
        del movie_ratings[reviewer_name]


def save_movies(movies_list):
    with open(json_file_path, "w") as file:
        json.dump(movies_list, file)


# Constants
script_dir = os.path.dirname(os.path.realpath(__file__))
path = 'json\\contacts.json'
json_file_path = os.path.join(script_dir, path)
#


movie_reviews_json()
