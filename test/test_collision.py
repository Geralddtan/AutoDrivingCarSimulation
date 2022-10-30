from Collision import Collision
from Car import AutoDrivingCar

def test_valid_get_width(capfd):
    car_a = AutoDrivingCar("A", [1, 2], "N", "R")
    car_b = AutoDrivingCar("B", [2, 1], "W", "FRFRF")
    collision = Collision([car_a, car_b], [1, 2], 3)
    collision.get_collision_details()   

    out, err = capfd.readouterr()
    assert out == "A B\n1 2\n3\n" #Checking with output
