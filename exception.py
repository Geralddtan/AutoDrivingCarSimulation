class CustomBaseException(Exception):
    """
    Base Execption Object
    """

    def __init__(self, message):
        super().__init__(f"Exception Raised: {message}")
        self.message = message

class InvalidVehicleInitialisationException(CustomBaseException):
    """
    Exception Class when car location or direction is invalid
    """

    def __init__(self, message):
        super().__init__(message)

class FieldSizeException(CustomBaseException):
    """
    Exception class when Field size is <= 0 in any dimension
    """

    def __init__(self, message):
        super().__init__(message)
 
class InvalidCommandException(CustomBaseException):
    """
    Exception class when a command is invalid (Any command except "F", "L", "R") 
    """

    def __init__(self, message):
        super().__init__(message)

class InvalidInitiaisationException(CustomBaseException):
    """
    Exception class when user input for initialisation is invalid
    """

    def __init__(self, message):
        super().__init__(message)