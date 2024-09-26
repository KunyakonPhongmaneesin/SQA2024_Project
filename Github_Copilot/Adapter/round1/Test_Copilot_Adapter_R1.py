# Python

import pytest
from main import Target, Adaptee, Adapter, client_code

# Arrange-Act-Assert (AAA) structure

def test_adapter():
    # Arrange
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    
    # Act
    result = client_code(adapter)
    
    # Assert
    assert result == "Adaptee's specific request"

def test_adaptee_directly():
    # Arrange
    adaptee = Adaptee()
    
    # Act
    result = adaptee.specific_request()
    
    # Assert
    assert result == "Adaptee's specific request"

# Ensure 100% branch coverage
def test_adapter_with_mock():
    # Arrange
    class MockAdaptee:
        def specific_request(self) -> str:
            return "Mocked request"
    
    mock_adaptee = MockAdaptee()
    adapter = Adapter(mock_adaptee)
    
    # Act
    result = client_code(adapter)
    
    # Assert
    assert result == "Mocked request"