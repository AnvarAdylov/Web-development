import json
import os


def filter_by_job(job_name, dictionary_list):
    filtered_list = []
    for item in dictionary_list:
        if item['position'] == job_name:
            filtered_list.append(item)
    if len(filtered_list) == 0:
        raise Exception(ValueError)
    return filtered_list


def main_body():
    try:
        list_of_workers = open_input_file()
    except:
        print('Не найден файл списка')
    output(list_of_workers)
    print('Введите должность сотрудника: ')
    job_name = input('> ')
    try:
#        filter_by_job(job_name, list_of_workers)
        output_stuff = filter_by_job(job_name, list_of_workers)
        output(output_stuff)
        save_filtered(output_stuff)
    except:
#    except ValueError:
        print('Nothing was found!')


def output(dictionary_list):
    print('Список сотрудников:')
    print('Номер | ФИО              | Должность  | Год')
    print('------|-----------------------|--------------|-----')
    for item in dictionary_list:
        print('  %i  | %s  %s         | %s  | %i' %
              (item['id'], item['name'], item['lastname'],
               item['position'], item['begin_year']))


def open_input_file():
    if os.path.exists(json_file_path):
        print("Input.json обнаружен")
        with open(json_file_path, "r", encoding="utf-8") as read_file:
            dictionary_list = json.load(read_file)
#        print(dictionary_list)
        return dictionary_list
    else:
        raise Exception('Input.json не найден!')


def save_filtered(dictionary_list):
    with open(json_save_path, "w") as file:
        json.dump(dictionary_list, file)


script_dir = os.path.dirname(os.path.realpath(__file__))
path_input = 'json\\input.json'
path_output = 'json\\out.json'
json_file_path = os.path.join(script_dir, path_input)
json_save_path = os.path.join(script_dir, path_output)

main_body()
