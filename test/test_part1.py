from Field import Field
from Car import AutoDrivingCar
from VehicleManager import VehicleManager

def test_valid_case_1():
    car = AutoDrivingCar("A", [1, 2], "N", "FFRFFFRRLF")
    field = Field(10, 10)
    car_manager = VehicleManager(field, [car])
    
    assert car_manager.move_single_vehicle(car) == "4 3 S"

def test_valid_case_2_past_boundary():
    car = AutoDrivingCar("A", [4, 4], "N", "RRLRLRLRLRLRLRFFFFRFFFFRRRFFFFFRFFFFFFFFFF")
    field = Field(5, 5)
    car_manager = VehicleManager(field, [car])
    
    assert car_manager.move_single_vehicle(car) == "0 0 W"

def test_valid_case_3_past_boundary():
    car = AutoDrivingCar("A", [0, 0], "W", "FFFRFFFLFFFRRFFFRFF")
    field = Field(5, 5)
    car_manager = VehicleManager(field, [car])
    
    assert car_manager.move_single_vehicle(car) == "3 1 S"

def test_valid_case_4_no_movement():
    car = AutoDrivingCar("A", [0, 0], "W", "RLRLRLRLRLRLRLRLRLRL")
    field = Field(5, 5)
    car_manager = VehicleManager(field, [car])
    
    assert car_manager.move_single_vehicle(car) == "0 0 W"