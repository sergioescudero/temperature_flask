import unittest

from parser.parser import Parser


class TestParser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_read_file_properly(self):
        a_parser = Parser()
        data = a_parser.read_json_from_file("resources/weather.json")
        self.assertEqual(len(data), 30)

    def test_check_keys(self):
        a_parser = Parser()
        data = a_parser.read_json_from_file("resources/weather.json")
        keys = data[0].keys()
        self.assertEqual(len(keys), 3)
        self.assertEqual("Dy" in keys, True)
        self.assertIn("Dy", keys)
        self.assertEqual("MxT" in keys, True)
        self.assertIn("MxT", keys)
        self.assertEqual("MnT" in keys, True)
        self.assertIn("MnT", keys)


if __name__ == '__main__':
    unittest.main()
