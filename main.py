import os

import route
from station import Station
from train import Train
from services import Services
from route import Route_for_A, Route_for_B
import sys


def register_routes():
    Route_for_A.create_route()
    Route_for_B.create_route()


def main():
    register_routes()
    input_file = '/home/ayushi/myprojects/train/input.txt'
    value = Services.check_valid_file(input_file)
    if not value:
        print("Invalid File")
    trains = Services.read_file(input_file)
    new_stations = Services.print_path_till_hyb(trains)
    if new_stations != 'Invalid Station':
        merged = Services.get_merged_bogies(new_stations)
        print('DEPARTURE TRAIN_AB', *merged, sep=' ')
    else:
        print('Error : Invalid Station')


if __name__ == "__main__":
    main()
