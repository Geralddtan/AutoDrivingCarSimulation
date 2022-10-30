from Field import Field
from Car import AutoDrivingCar
from VehicleManager import VehicleManager

def test_valid_case_1_multiple_vehicles(capfd):
    car_a = AutoDrivingCar("A", [1, 2], "W", "RFFRLRFFFRRRLLLLLL")
    car_b = AutoDrivingCar("B", [7, 8], "W", "FFLFFFFRFLLLLLL")
    car_c = AutoDrivingCar("C", [4, 4], "N", "RRRRLLLLRRRRLLL")
    field = Field(10, 10)
    car_manager = VehicleManager(field, [car_a, car_b, car_c])
    
    car_manager.check_collision_all_vehicles()

    out, err = capfd.readouterr()
    assert out == "A B C\n4 4\n9\n" #Checking with output

def test_valid_case_2_multiple_collisions(capfd): 
    car_a = AutoDrivingCar("A", [1, 2], "N", "R")
    car_b = AutoDrivingCar("B", [2, 1], "W", "FRFRF")
    car_c = AutoDrivingCar("C", [3, 3], "N", "FRF")
    car_d = AutoDrivingCar("D", [4, 4], "N", "R")
    field = Field(10, 10)
    car_manager = VehicleManager(field, [car_a, car_b, car_c, car_d])
    
    car_manager.check_collision_all_vehicles()

    out, err = capfd.readouterr()
    assert out == "A B\n1 2\n3\nC D\n4 4\n3\n" #Checking with output

def test_valid_case_3_single_collision(capfd):
    car_a = AutoDrivingCar("A", [1, 2], "N", "FFRFFFFRRL")
    car_b = AutoDrivingCar("B", [7, 8], "W", "FFLFFFFFFF")
    field = Field(10, 10)
    car_manager = VehicleManager(field, [car_a, car_b])
    
    car_manager.check_collision_all_vehicles()

    out, err = capfd.readouterr()
    assert out == "A B\n5 4\n7\n" #Checking with output

def test_valid_case_4_no_collision(capfd):
    car_a = AutoDrivingCar("A", [1, 2], "E", "FRFRFRFRFRFR")
    car_b = AutoDrivingCar("B", [2, 1], "W", "FRFRFRFRFRFR")
    field = Field(10, 10)
    car_manager = VehicleManager(field, [car_a, car_b])
    
    car_manager.check_collision_all_vehicles()

    out, err = capfd.readouterr()
    assert out == "no collision\n" #Checking with output
