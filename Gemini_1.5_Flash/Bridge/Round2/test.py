import pytest
from main import Circle, Square, RedColor, BlueColor

# Arrange, Act, Assert (AAA) structure with result output

def test_circle_with_red_color(capfd):
    # Arrange
    color = RedColor()
    circle = Circle(color, 5)

    # Act
    result = circle.draw()

    # Capture output
    out, err = capfd.readouterr()

    # Assert
    assert result == "Drawing a red circle with radius 5"
    
    # Show result
    print(f"Test Result: {result}")

def test_square_with_blue_color(capfd):
    # Arrange
    color = BlueColor()
    square = Square(color, 10)

    # Act
    result = square.draw()

    # Capture output
    out, err = capfd.readouterr()

    # Assert
    assert result == "Drawing a blue square with side length 10"
    
    # Show result
    print(f"Test Result: {result}")

def test_circle_with_blue_color(capfd):
    # Arrange
    color = BlueColor()
    circle = Circle(color, 7)

    # Act
    result = circle.draw()

    # Capture output
    out, err = capfd.readouterr()

    # Assert
    assert result == "Drawing a blue circle with radius 7"
    
    # Show result
    print(f"Test Result: {result}")

def test_square_with_red_color(capfd):
    # Arrange
    color = RedColor()
    square = Square(color, 8)

    # Act
    result = square.draw()

    # Capture output
    out, err = capfd.readouterr()

    # Assert
    assert result == "Drawing a red square with side length 8"
    
    # Show result
    print(f"Test Result: {result}")
