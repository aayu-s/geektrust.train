import os
from settings import PROJECT_ROOT
import unittest

from route import Route_for_A, Route_for_B
from services import Services


class TestCases(unittest.TestCase):
    def test_valid_file(self):
        input_file = '/home/ayushi/myprojects/train/input.txt'
        self.assertEqual(Services.check_valid_file(input_file), True)

    def test_invalid_file(self):
        input_file = '/home/ayushi/myprojects/train/input.txt'
        self.assertEqual(Services.check_valid_file(input_file), False)

    def test_valid_station(self):
        input_file = '/home/ayushi/myprojects/train/input.txt'
        trains = Services.read_file(input_file)
        new_stations = Services.print_path_till_hyb(trains)
        self.assertEqual(type([]), type(new_stations))

    def test_invalid_station(self):
        input_file = '/home/ayushi/myprojects/train/input.txt'
        trains = Services.read_file(input_file)
        msg = Services.print_path_till_hyb(trains)
        self.assertEqual('Invalid Station', msg)


if __name__ == '__main__':
    unittest.main()
