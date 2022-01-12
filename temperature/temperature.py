from parser.parser import Parser


class Temperature:
    def all(self):
        return self.data

    def get_day(self, day):
        return next((filter(lambda x: x['Dy'] == day, self.data)), None)


class TemperatureFromFile(Temperature):
    def __init__(self, path):
        self.path = path
        parser = Parser()
        self.data = parser.read_json_from_file(self.path)


class TemperatureFromJson(Temperature):
    def __init__(self, data):
        self.data = data
