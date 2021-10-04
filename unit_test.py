import unittest

from route import Route
from services import Services


class TestCases(unittest.TestCase):
    def test_valid_file(self):
        input_file = '/home/ayushi/myprojects/train/input.txt'
        self.assertEqual(Services.check_valid_file(input_file), True)

    def test_valid_station(self):
        Route.register_routes()
        input_file = '/home/ayushi/myprojects/train/input.txt'
        trains = Services.read_file(input_file)
        for train in trains:
            value = Services.get_bogie_at('HYB', train)
            self.assertEqual(type([]), type(value))

    def test_invalid_station(self):
        Route.register_routes()
        input_file = '/home/ayushi/myprojects/train/input.txt'
        trains = Services.read_file(input_file)
        for train in trains:
            msg = Services.get_bogie_at('PPP', train)
            self.assertEqual('E01', msg)


if __name__ == '__main__':
    unittest.main()
