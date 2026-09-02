import os
import json
import Task5


class Stats:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    path = 'json\\stats.json'
    json_file_path = os.path.join(script_dir, path)

    def __init__():
        Task5.Application()

    def load(self):
        if os.path.exists(Stats.json_file_path):
            print("Сохраненная база загружена")
            with open(Stats.json_file_path, "r") as read_file:
                self.stats = json.load(read_file)
        else:
            with open(Stats.json_file_path, "w") as file:
                json.dump('', file)

    def save(self):
        with open(Stats.json_file_path, "w") as file:
            json.dump(self.stats, file)

    def incr_stat():
        condition = False
        if condition is True:
            self.stats['stat'] += 1

    def display_stat():
        print('Table')
