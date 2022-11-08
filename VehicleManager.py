from Collision import Collision

class VehicleManager:
    """
    An abstract class to represent Vehicle Managers. Vehicle Managers control vehicles that are present on a single field.

    Attributes:
    field : Field
        Field that a vehicle manager is controlling

    vehicles: List[Vehicle]
        List of Vehicles that the vehicle manager is controlling

    Methods:
    add_vehicle(vehicle):
        Adds additional vehicle to the vehicle manager

    get_vehicles(vehicle):
        Return all vehicles assigned to the vehicle manager

    check_vehicles_commands_remaining():
        Returns a boolean to check if any vehicles still have commands remaining

    check_valid_command(vehicle):
        Checks if a particular vehicles' next command is valid (Does not move out of boundary)

    move_single_vehicle(vehicle):
        Moves a single vehicle using all its commands

    check_collision_all_vehicles():
        Checks to see if any collision occurs while vehicles carry out all their commands

    """
    def __init__(self, field, vehicles = []):
        self.field = field
        self.vehicles = vehicles

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def get_vehicles(self):
        return self.vehicles

    def check_vehicles_commands_remaining(self): #Check to see if any vehicles still have commands remaining
        for vehicle in self.get_vehicles():
            if not vehicle.get_has_finished_commands():
                return True
        return False #Only if all vehicles have finished all commands would we return true

    def check_valid_command(self, vehicle):
        veh_curr_pos = vehicle.get_current_position()
        veh_curr_dir = vehicle.get_current_direction()
        veh_curr_com = vehicle.get_current_command()
        if veh_curr_com == None: # Case where the vehicle no longer has any commands
            return False

        field_width = self.field.get_width()
        field_height = self.field.get_height()
        field_z = self.field.get_z()
        x, y, z = veh_curr_pos.get_x(), veh_curr_pos.get_y(), veh_curr_pos.get_z()

        if (veh_curr_com == "F") and ((x == 0) or (x == field_width) or (y == 0) or (y == field_height)): 
            #Check command is moving forward and if vehicle is on the field boundary
            if (y == 0) and (veh_curr_dir == "S"): #On bottom boundary and moving South
                return False
            elif (y == field_height) and (veh_curr_dir == "N"): #On top boundary and moving north 
                return False
            elif (x == 0) and (veh_curr_dir == "W"): #On left boundary and moving West
                return False
            elif (x == field_width) and (veh_curr_dir == "E"): #On right boundary and moving East
                return False
            else:
                return True #All else are valid movements
        elif (veh_curr_com == "U" and z == field_z) or (veh_curr_com == "D" and z == 0):
            return False
        else:
            return True
        

    def move_single_vehicle(self, vehicle):
        while vehicle.get_has_finished_commands() == False: #Check to see if vehicle has finished all its commands
            if self.check_valid_command(vehicle): #If movement is valid, perform movement
                vehicle.move()
            else:
                vehicle.increment_current_command_index() #Invalid move, so we skip the move

        return vehicle.get_current_position_direction()

    def check_collision_all_vehicles(self):
        """
        This method carries out commands for each vehicle at every time step and cross checks to see if any vehicle is already on 
        the grid point which the vehicle is trying to move towards. If more than one car is on the grid point, a collision occurs.
        
        """
        counter = 1
        while self.check_vehicles_commands_remaining(): #Check to see if any vehicles still have remaining commands
            current_locations = {}
            collision_flag = -1 #Flag to check for any collision
            for vehicle in self.get_vehicles():
                if self.check_valid_command(vehicle): #Check to see if move is valid. If not valid, dont move the vehicle
                    vehicle.move()
                else:
                    vehicle.increment_current_command_index() #Increment vehicle counter if move is not valid

                location = vehicle.get_current_position().get_location_tuple() #Get vehicle current location
                if location in current_locations: #If another vehicle is already on the location
                    current_locations[location].append(vehicle) #Store all vehicles involved in the collision
                    collision_flag = 1
                else:
                    current_locations[location] = [vehicle]  #If no collision, store current location of vehicle

            if collision_flag == 1:
                for position, vehicles_involved in current_locations.items(): 
                    if len(vehicles_involved) > 1: #Check all current locations for possible collisions
                        collision = Collision(vehicles_involved, position, counter)
                        collision.get_collision_details()
                return

            counter += 1
        
        print("no collision") #If no collision occurs after all vehicles moved
        return
