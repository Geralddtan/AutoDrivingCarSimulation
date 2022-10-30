from VehicleManager import VehicleManager
from Field import Field
from Car import AutoDrivingCar

def test_valid_add_vehicle():
    field = Field(10,10)
    vm = VehicleManager(field, [])
    car1 = AutoDrivingCar("A", [0,0], "E", "FLR")
    car2 = AutoDrivingCar("B", [5,5], "N", "RFFFF")
    vm.add_vehicle(car1)
    vm.add_vehicle(car2)
    assert len(vm.get_vehicles()) == 2

def test_valid_check_vehicle_commands_remaining_true():
    field = Field(10,10)
    vm = VehicleManager(field, [])
    car1 = AutoDrivingCar("A", [0,0], "E", "FL")
    car2 = AutoDrivingCar("B", [5,5], "N", "RFF")
    for i in range(2):
        car1.move()
    vm.add_vehicle(car1)
    vm.add_vehicle(car2)
    assert vm.check_vehicles_commands_remaining() == True

def test_valid_check_vehicle_commands_remaining_false():
    field = Field(10,10)
    vm = VehicleManager(field, [])
    car1 = AutoDrivingCar("A", [0,0], "E", "FL")
    car2 = AutoDrivingCar("B", [5,5], "N", "RF")
    for i in range(2):
        car1.move()
        car2.move()
    vm.add_vehicle(car1)
    vm.add_vehicle(car2)
    assert vm.check_vehicles_commands_remaining() == False

def test_check_invalid_command_move_out_grid_bottom():
    field = Field(10,10)
    vm = VehicleManager(field, [])
    car1 = AutoDrivingCar("A", [0,0], "S", "F")
    vm.add_vehicle(car1)
    assert vm.check_valid_command(car1) == False

def test_check_invalid_command_move_out_grid_left():
    field = Field(10,10)
    vm = VehicleManager(field, [])
    car1 = AutoDrivingCar("A", [0,5], "W", "F")
    vm.add_vehicle(car1)
    assert vm.check_valid_command(car1) == False

def test_check_invalid_command_move_out_grid_right():
    field = Field(10,10)
    vm = VehicleManager(field, [])
    car1 = AutoDrivingCar("A", [9,5], "E", "F")
    vm.add_vehicle(car1)
    assert vm.check_valid_command(car1) == False

def test_check_invalid_command_move_out_grid_top():
    field = Field(10,10)
    vm = VehicleManager(field, [])
    car1 = AutoDrivingCar("A", [5,9], "N", "F") # On top side of grid
    vm.add_vehicle(car1)
    assert vm.check_valid_command(car1) == False

def test_check_valid_command_move_out_grid_bottom():
    field = Field(10,10)
    vm = VehicleManager(field, [])
    car1 = AutoDrivingCar("A", [0,0], "N", "F")
    vm.add_vehicle(car1)
    assert vm.check_valid_command(car1) == True

def test_check_valid_command_move_within_grid():
    field = Field(10,10)
    vm = VehicleManager(field, [])
    car1 = AutoDrivingCar("A", [5,5], "N", "F")
    vm.add_vehicle(car1)
    assert vm.check_valid_command(car1) == True