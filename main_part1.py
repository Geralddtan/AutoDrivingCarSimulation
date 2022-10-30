from Field import Field
from Car import AutoDrivingCar
from VehicleManager import VehicleManager
from exception import CustomBaseException, InvalidVehicleInitialisationException, InvalidInitiaisationException

class Main:
    """
    Reads input file and removes line break at end of line
    """
    def read_txt_file(self, file_path: str) -> list:
        user_input = []
        with open(file_path, "r") as file:
            line = file.readline()
            while line:
                user_input.append(line.strip('\n'))
                line = file.readline()
        return user_input            

if __name__ == "__main__":
    try: 
        main = Main()
        file_path = input("Please Input your txt file name: ")
        user_input = main.read_txt_file(file_path)

        if len(user_input) != 3:
            raise InvalidInitiaisationException("Invalid Input! Please refer to valid input format")

        field_size = user_input[0].split(" ")
        vehicle_orientation = user_input[1].split(" ")
        vehicle_x = int(vehicle_orientation[0])
        vehicle_y = int(vehicle_orientation[1])
        vehicle_direction = vehicle_orientation[2]
        vehicle_commands = user_input[2]

        field_width, field_height = int(field_size[0]), int(field_size[1])
        field = Field(field_width, field_height)

        if vehicle_x < 0 or vehicle_y < 0 or vehicle_x >= field_width or vehicle_y >= field_height: #If car is initialised outside of field width
            raise InvalidVehicleInitialisationException(f"Car Position {vehicle_x, vehicle_y} is outside Field Boundaries")

        car = AutoDrivingCar("A", [vehicle_x, vehicle_y], vehicle_direction, vehicle_commands)
        car_manager = VehicleManager(field, [car])

        print(car_manager.move_single_vehicle(car))
    except CustomBaseException as e:
        print(str(e))
    except Exception as e:
        print("Something went wrong: ", e)
