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
    """
    Main code to run part 1
    - Reads in input txt file
    - Initialises Vehicle, Field, VehicleManager
    - Moves the Vehicle to get the final position
    """
    try: 
        main = Main()
        file_path = input("Please Input your txt file name: ")
        user_input = main.read_txt_file(file_path) #Process input txt file

        if len(user_input) != 3:
            raise InvalidInitiaisationException("Invalid Input! Please refer to valid input format")

        #Obtains field and vehicle information from user input
        field_size = user_input[0].split(" ")
        vehicle_orientation = user_input[1].split(" ")
        vehicle_x = int(vehicle_orientation[0])
        vehicle_y = int(vehicle_orientation[1])
        vehicle_z = int(vehicle_orientation[2])
        vehicle_direction = vehicle_orientation[3]
        vehicle_commands = user_input[2]

        field_width, field_height, field_z = int(field_size[0]), int(field_size[1]), int(field_size[2])
        field = Field(field_width, field_height, field_z)

        # Checkif vehicle initialised outside of field boundary
        if vehicle_x < 0 or vehicle_y < 0 or vehicle_x >= field_width or vehicle_y >= field_height or vehicle_z < 0 or vehicle_z >= field_z: #If car is initialised outside of field width
            raise InvalidVehicleInitialisationException(f"Car Position {vehicle_x, vehicle_y, vehicle_z} is outside Field Boundaries")

        car = AutoDrivingCar("A", [vehicle_x, vehicle_y, vehicle_z], vehicle_direction, vehicle_commands)
        car_manager = VehicleManager(field, [car])

        # Main Code to get output
        print(car_manager.move_single_vehicle(car))
    except CustomBaseException as e:
        print(str(e))
    # except Exception as e:
    #     print("Something went wrong: ", e)
