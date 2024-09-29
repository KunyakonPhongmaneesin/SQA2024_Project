import pytest
from main import Shape, Circle, Square

def test_circle_drawing():
    # Arrange
    circle = Circle("red")

    # Act
    circle.draw()

    # Assert
    assert "Drawing a circle in red color" in str(circle.draw())

def test_square_drawing():
    # Arrange
    square = Square("blue")

    # Act
    square.draw()

    # Assert
    assert "Drawing a square in blue color" in str(square.draw())