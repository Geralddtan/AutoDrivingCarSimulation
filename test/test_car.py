import pytest
from Car import AutoDrivingCar

def test_valid_move_F():
    # Test if car move() function for "F" is accurate 
    car = AutoDrivingCar("a", [0, 0], "E", "F")
    car.move()
    curr_pos = car.get_current_position()
    curr_dir = car.get_current_direction()
    curr_command = car.get_current_command()

    assert curr_pos.get_x() == 1
    assert curr_pos.get_y() == 0
    assert curr_dir == "E"
    assert curr_command == None

def test_valid_move_L():
    # Test if car move() function for "F" is accurate 
    car = AutoDrivingCar("a", [0, 0], "E", "L")
    car.move()
    curr_pos = car.get_current_position()
    curr_dir = car.get_current_direction()
    curr_command = car.get_current_command()

    assert curr_pos.get_x() == 0
    assert curr_pos.get_y() == 0
    assert curr_dir == "N"
    assert curr_command == None

def test_valid_move_R():
    # Test if car move() function for "F" is accurate 
    car = AutoDrivingCar("a", [0, 0], "E", "R")
    car.move()
    curr_pos = car.get_current_position()
    curr_dir = car.get_current_direction()
    curr_command = car.get_current_command()
    assert curr_pos.get_x() == 0
    assert curr_pos.get_y() == 0
    assert curr_dir == "S"
    assert curr_command == None

