import json
import os


class Validation():
    def is_int(input):
        try:
            int(input)
            return True
        except ValueError:
            return False


class File_check():
    def exist(file_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        path = 'json\\'+file_name+'.json'
        json_file_path = os.path.join(script_dir, path)

        if os.path.exists(json_file_path):
            return True
        else:
            return False


class Json_file_manager():
    def __init__(self, file_name):
        self.file_name = file_name
        script_dir = os.path.dirname(os.path.realpath(__file__))
        path = 'json\\' + file_name + '.json'
        json_file_path = os.path.join(script_dir, path)

        if os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as read_file:
                self.data = json.load(read_file)
        else:
            with open(json_file_path, 'w') as json_file:
                pass

    def __str__(self):
        print(self.data)
        return '\n'

    def rewrite_save(self, file_name='', data=''):
        if file_name == '':
            file_name = self.file_name
        if data == '':
            data = self.data
        script_dir = os.path.dirname(os.path.realpath(__file__))
        path = 'json\\'+file_name+'.json'
        json_file_path = os.path.join(script_dir, path)
        with open(json_file_path, 'w') as json_file:
            json.dump(self.serialize_list(data), json_file)

    @staticmethod
    def serialize_list(obj_list):
        return [obj.__json__() for obj in obj_list]
