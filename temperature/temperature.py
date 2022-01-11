from parser.parser import Parser


class Temperature:

    def __init__(self, path):
        self.path = path

    def all(self):
        parser = Parser()
        return parser.read_json_from_file(self.path)

    def get_day(self, day):
        parser = Parser()
        data = parser.read_json_from_file(self.path)
        element = next((filter(lambda x: x['Dy'] == day, data)), None)
        return element
