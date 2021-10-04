import sys
import unittest
from route import Route
from services import Services


class TestCases(unittest.TestCase):
    def test_valid_station(self):
        Route.register_routes()
        lines = ['TRAIN_A ENGINE NDL NDL KRN GHY SLM NJP NGP BLR', 'TRAIN_B ENGINE NJP GHY AGA PNE MAO BPL PTA']
        trains = Services.process_file(lines)
        for train in trains:
            value = Services.get_bogie_at('HYB', train)
            self.assertEqual(type([]), type(value))

    def test_invalid_station(self):
        Route.register_routes()
        lines = ['TRAIN_A ENGINE NDL NDL KRN GHY SLM NJP NGP BLR', 'TRAIN_B ENGINE NJP GHY AGA PNE MAO BPL PTA']
        trains = Services.process_file(lines)
        for train in trains:
            # passing mock value
            msg = Services.get_bogie_at('PPP', train)
            self.assertEqual('E01', msg)


if __name__ == '__main__':
    unittest.main()
