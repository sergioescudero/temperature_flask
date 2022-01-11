import json
import os


class Parser:

    def __init__(self):
        pass

    def read_json_from_file(self, path):
        with open(self.__get_absolute_path(path), "r") as json_file:
            data = json.load(json_file)
            return data

    def __get_absolute_path(self, relative_path):
        parent_dir = self.__get_parent_dir()
        return os.path.join(parent_dir, relative_path)

    def __get_parent_dir(self):
        return os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
