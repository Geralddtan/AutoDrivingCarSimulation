from abc import ABC, abstractmethod
from GridPoint import GridPoint
from exception import InvalidVehicleInitialisationException

class Vehicle(ABC):
    """
    An abstract class to represent Vehicles. Other vehicles such as cars should make use of the Vehicle Abstract Class 
    as it provides the base structure of vehicles


    Attributes:
    name : str
        Car Identifier
    current_position : GridPoint
        GridPoint of current position of vehicle
    current_direction : str
        Current direction vehicle is facing
    commands: str
        Commands associated to each vehicle
    has_finished_commands: bool
        Boolean to check if a vehicle has completed all of its commands
    left_rotation: dic
        Dictionary to store possible left rotation results based on current direction
    right_rotation: dic
        Dictionary to store possible right rotation results based on current direction
    movement:dic
        Dictionary to store movement results based on current direction

    Methods:
    get_name():
        Returns name of the vehicle

    get_current_position():
        Returns GridPoint of current position

    set_current_position(new_x, new_y):
        Sets current GridPoint position 
    
    get_current_direction():
        Returns current direction of vehicle

    set_current_direction(current_direction):
        Sets current direction of vehicle

    increment_current_command_index():
        Increase current command pointer

    get_has_finished_commands():
        Returns boolean stating if a vehicle has finished all of its commands

    get_current_command():
        Returns current command of vehicle

    get_left_rotation():
        Return left rotation results based on current direction

    get_right_rotation():
        Return right rotation results based on current direction
        
    get_current_position_direction
        Return vehicle position and direction

    get_movement():
        Return movement based on current direction

    """

    def __init__(self, name, current_position, current_direction, commands):

        if current_direction not in ["N", "S", "E", "W"]:
            raise InvalidVehicleInitialisationException("Invalid Vehicle Direction! It should be 'N, S, E, W")

        self.name = name
        self.current_position = GridPoint(current_position[0], current_position[1])
        self.current_direction = current_direction
        self.commands = commands
        self.current_command_index = 0 # Stores the index of the current command of the vehicle
        self.has_finished_commands = False
        self.left_rotation = {"N":"W","W":"S","S":"E","E":"N"} #Possible mappings for left rotation based on direction
        self.right_rotation = {"N":"E","E":"S","S":"W","W":"N"} #Possible mappings fir right rotation based on direction
        self.movement = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W':(-1, 0)} #Movement changes based on direction

    def get_name(self):
        return self.name

    def get_current_position(self) -> GridPoint:
        return self.current_position

    def set_current_position(self, new_x, new_y):
        self.current_position.set_x(new_x) #Sets new x coordinate from grid point
        self.current_position.set_y(new_y) #Sets new y coordinate from grid point

    def get_current_direction(self) -> str:
        return self.current_direction

    def set_current_direction(self, current_direction: str):
        self.current_direction = current_direction

    def increment_current_command_index(self):
        self.current_command_index += 1

        if self.current_command_index == len(self.commands): #When vehicle has reached the end of our commands
            self.has_finished_commands = True

    def get_has_finished_commands(self):
        return self.has_finished_commands

    def get_current_command(self):
        if self.current_command_index >= len(self.commands): #When vehicle have no more commands, raise Exception
            return None
        return self.commands[self.current_command_index]

    def get_left_rotation(self, current_direction):
        return self.left_rotation[current_direction]

    def get_right_rotation(self, current_direction):
        return self.right_rotation[current_direction]

    def get_movement(self, current_direction):
        return self.movement[current_direction]

    def get_current_position_direction(self): 
        curr_position = self.get_current_position()
        curr_direction = self.get_current_direction()
        return " ".join([str(curr_position.get_x()), str(curr_position.get_y()), curr_direction])

    @abstractmethod
    def move(self, current_command):
        pass
