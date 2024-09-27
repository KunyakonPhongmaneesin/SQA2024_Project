# test_adapter.py

import pytest
from adapter import LegacySystem, Adapter


def test_adapter_request():
    # Arrange
    legacy_system = LegacySystem()
    adapter = Adapter(legacy_system)

    # Act
    result = adapter.request()

    # Assert
    assert result == "Legacy system response"
