import pytest
from main import add_numbers

def test_add_numbers():
    # Arrange
    a = 2
    b = 3
    expected_result = 5

    # Act
    actual_result = add_numbers(a, b)

    # Assert
    assert actual_result == expected_result