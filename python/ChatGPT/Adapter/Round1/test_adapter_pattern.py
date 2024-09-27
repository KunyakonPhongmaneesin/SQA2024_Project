import pytest
from adapter_pattern import Car, Boat, BoatAdapter

# Test using the AAA pattern (Arrange, Act, Assert)

def test_car_drive():
    # Arrange
    car = Car()

    # Act
    result = car.drive()

    # Assert
    assert result == "Car is driving on the road"

def test_boat_adapter_drive():
    # Arrange
    boat = Boat()
    boat_adapter = BoatAdapter(boat)

    # Act
    result = boat_adapter.drive()

    # Assert
    assert result == "Boat is sailing on the water"

# 100% Branch Coverage Test:
def test_adapter_branch_coverage():
    # Arrange
    car = Car()
    boat = Boat()
    boat_adapter = BoatAdapter(boat)

    # Act & Assert
    assert car.drive() == "Car is driving on the road"
    assert boat_adapter.drive() == "Boat is sailing on the water"

