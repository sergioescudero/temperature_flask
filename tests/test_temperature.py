import unittest

from parser.parser import Parser


class TestTemperature(unittest.TestCase):

    def setUp(self):
        a_parser = Parser()
        self.data = a_parser.read_json_from_file("resources/weather.json")

    def tearDown(self):
        pass

    def test_max_and_min_of_max_temperatures(self):
        max_of_max = max(self.data, key=lambda x: x['MxT'])
        min_of_max = min(self.data, key=lambda x: x['MxT'])
        self.assertEqual(min_of_max.get('MxT'), 61)
        self.assertEqual(max_of_max.get('MxT'), 97)


if __name__ == '__main__':
    unittest.main()
