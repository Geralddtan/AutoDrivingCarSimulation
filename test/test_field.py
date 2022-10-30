from Field import Field

def test_valid_get_width():
    # Test if Field retrieves width properly
    field = Field(10,10)
    assert field.get_width() == 9

def test_valid_get_height():
    # Test if Field retrieves width properly
    field = Field(10,10)
    assert field.get_height() == 9