from Vehicle import Vehicle
from exception import InvalidCommandException

class AutoDrivingCar(Vehicle):
    """
        A class to represent an AutoDrivingCar.

        Methods

        turn_left():
            Performs left rotation on car

        turn_right():
            Performs right rotation on car
    
        move_forward():
            Moves car forward
        
        move(): 
            Performs command based on car current command
    """

    def __init__(self, name, current_position, current_direction, commands):
        super().__init__(name, current_position, current_direction, commands)

    def turn_left(self):
        current_direction = self.get_current_direction()
        new_direction = self.get_left_rotation(current_direction)
        self.set_current_direction(new_direction)

    def turn_right(self):
        current_direction = self.get_current_direction()
        new_direction = self.get_right_rotation(current_direction)
        self.set_current_direction(new_direction)

    def move_upwards(self):
        current_position = self.get_current_position()
        curr_x, curr_y, curr_z = current_position.get_x(), current_position.get_y(), current_position.get_z()
        new_x, new_y = curr_x, curr_y
        new_z = curr_z + 1
        self.set_current_position(new_x, new_y, new_z)

    def move_downwards(self):
        current_position = self.get_current_position()
        curr_x, curr_y, curr_z = current_position.get_x(), current_position.get_y(), current_position.get_z()
        new_x, new_y = curr_x, curr_y
        new_z = curr_z - 1
        self.set_current_position(new_x, new_y, new_z)

    def move_forward(self):
        current_direction = self.get_current_direction()
        current_position = self.get_current_position()

        to_move = self.get_movement(current_direction)
        new_x = current_position.get_x() + to_move[0]
        new_y = current_position.get_y() + to_move[1]
        new_z = current_position.get_z()
        self.set_current_position(new_x, new_y, new_z)

    def move(self):
        
        """ Moves AutoDrivingCar based on its current command """

        if self.get_has_finished_commands(): #If car has no more commands
            return False

        current_command = self.get_current_command()

        if current_command == "L": #Perform command based on turning left
            self.turn_left()
        elif current_command == "R": #Perform command based on turning right
            self.turn_right()
        elif current_command == "F": #Perform command to get new position based on current direction and position
            self.move_forward()
        elif current_command == "U":
            self.move_upwards()
        elif current_command == "D":
            self.move_downwards()
        else:
            raise InvalidCommandException(f"{current_command} is an invalid command. Valid commands are 'F', 'L', 'R', 'U', 'D'")

        #Incrementing index after we move the AutoDrivingCar
        self.increment_current_command_index()

        return True
    

