from exception import FieldSizeException

class Field:
    """
    A class to represent a Field.


    Attributes:
    width : int
        Width of Field
    height : int
        Height of Field

    Methods:
    get_width():
        Get width of field

    get_height():
        Get height of field
    
    """
    def __init__(self, width, height):
        if width <= 0 or height <= 0: #Checking Field Size
            raise FieldSizeException("Field width and height must be at least size 1")

        self.width = width-1 #-1 to make the grid 0-based
        self.height = height-1 #-1 to make the grid 0-based

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height
