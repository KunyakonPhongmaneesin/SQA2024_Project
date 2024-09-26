# main.py
def my_function(x, y):
    if x > y:
        return x
    else:
        return y

# test_main.py
import pytest
from main import my_function

def test_my_function():
    # Arrange
    x = 5
    y = 3

    # Act
    result = my_function(x, y)

    # Assert
    assert result == 5