class GridPoint:
    """
    A class to represent a GridPoint.

    ...

    Attributes:
    x : int
        x coordinate of point
    y : int
        y coordinate of point

    Methods:
    get_x():
        Get x coordinate of point

    get_y():
        Get y coordinate of point

    set_x():
        Set x coordinate of point

    set_y():
        Set y coordinate of point 

    get_location_tuple():
        Get a tuple representing the (x, y) location of the point
    
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def get_location_tuple(self): 
        ''' Get a tuple representing the (x, y) location of the point '''
        return (self.get_x(), self.get_y(), self.get_z())
