import pytest

def test_adapter():
    # Arrange
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    # Act
    result = client_code(adapter)

    # Assert
    assert result == "Specific request"

def test_adaptee():
    # Arrange
    adaptee = Adaptee()

    # Act
    result = adaptee.specific_request()

    # Assert
    assert result == "Specific request"