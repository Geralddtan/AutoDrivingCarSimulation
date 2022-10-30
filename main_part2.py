from Field import Field
from Car import AutoDrivingCar
from VehicleManager import VehicleManager
from exception import InvalidVehicleInitialisationException, CustomBaseException, InvalidInitiaisationException

class Main:
    """
    Reads input file and removes any empty line
    """
    def read_txt_file(self, file_path: str) -> list:
        user_input = []
        with open(file_path, "r") as file:
            line = file.readline()
            while line:
                line = line.strip('\n')
                if line:
                    user_input.append(line)
                line = file.readline()
        return user_input
            

if __name__ == "__main__":
    try:
        main = Main()
        file_path = input("Please Input your txt file name: ")
        user_input = main.read_txt_file(file_path)

        field_size = user_input[0].split(" ")
        field_width, field_height = int(field_size[0]), int(field_size[1])
        field = Field(field_width, field_height)
        car_manager = VehicleManager(field, [])

        if (len(user_input)-1)%3!=0: #Number of valid lines should be (multiples of 3) + 1
            raise InvalidInitiaisationException("Invalid Input! Please refer to valid input format")
        num_cars = int((len(user_input)-1)/3) 
        all_vehicles = []

        counter = 1
        for i in range(0, num_cars):
            # Increases counter by 3 for each loop to represent a vehicle's information
            vehicle_name = user_input[counter]
            counter += 1

            vehicle_orientation = user_input[counter].split(" ")
            vehicle_x = int(vehicle_orientation[0])
            vehicle_y = int(vehicle_orientation[1])

            if vehicle_x < 0 or vehicle_y < 0 or vehicle_x >= field_width or vehicle_y >= field_height: #If car is initialised outside of field width
                raise InvalidVehicleInitialisationException(f"Car Position {vehicle_x, vehicle_y} is outside Field Boundaries")

            vehicle_direction = vehicle_orientation[2]
            counter += 1

            vehicle_commands = user_input[counter]
            counter += 1

            car_manager.add_vehicle(AutoDrivingCar(vehicle_name, [vehicle_x, vehicle_y], vehicle_direction, vehicle_commands))

        car_manager.check_collision_all_vehicles()
    except CustomBaseException as e:
        print(str(e))
    except Exception as e:
        print("Something went wrong: ", e)

