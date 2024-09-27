# test_main.py
import pytest
from main import NewSystemAdapter, LegacySystem


def test_calculate_area_positive():
    # Arrange
    legacy_system = LegacySystem()
    adapter = NewSystemAdapter(legacy_system)
    length = 5
    width = 3
    expected_area = 15

    # Act
    actual_area = adapter.calculate_area(length, width)

    # Assert
    assert actual_area == expected_area


def test_calculate_area_negative_length():
    # Arrange
    legacy_system = LegacySystem()
    adapter = NewSystemAdapter(legacy_system)
    length = -1
    width = 3
    expected_area = 0

    # Act
    actual_area = adapter.calculate_area(length, width)

    # Assert
    assert actual_area == expected_area


def test_calculate_area_negative_width():
    # Arrange
    legacy_system = LegacySystem()
    adapter = NewSystemAdapter(legacy_system)
    length = 5
    width = -2
    expected_area = 0

    # Act
    actual_area = adapter.calculate_area(length, width)

    # Assert
    assert actual_area == expected_area
