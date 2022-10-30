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

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_location_tuple(self): 
        ''' Get a tuple representing the (x, y) location of the point '''
        return (self.get_x(), self.get_y())
