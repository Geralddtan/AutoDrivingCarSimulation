class Collision:
    def __init__(self, vehicles, position, time_point):
        self.vehicles = vehicles
        self.position = position
        self.time_point = time_point

    def get_vehicles_involved(self):
        return self.vehicles

    def get_position(self):
        return self.position

    def get_time_point(self):
        return self.time_point

    def get_collision_details(self):
        vehicles_involved_name = [veh.get_name() for veh in self.get_vehicles_involved()]
        print(" ".join(vehicles_involved_name))
        print(" ".join([str(i) for i in self.get_position()]))
        print(self.get_time_point())
        