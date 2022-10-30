from GridPoint import GridPoint

def test_valid_get_x():
    # Test if grid point retrieves x value properly
    point = GridPoint(10,11)
    assert point.get_x() == 10

def test_valid_get_y():
    # Test if grid point retrieves y value properly
    point = GridPoint(11,10)
    assert point.get_y() == 10

def test_valid_set_x():
    # Test if grid point retrieves x value properly
    point = GridPoint(10,11)
    point.set_x(5)
    assert point.get_x() == 5

def test_valid_set_y():
    # Test if grid point retrieves y value properly
    point = GridPoint(11,10)
    point.set_y(5)
    assert point.get_y() == 5

def test_valid_get_location_tuple():
    # Test if grid point retrieves x value properly
    point = GridPoint(10,11)
    assert point.get_location_tuple() == (10,11)
