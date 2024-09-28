import pytest
# Test_Copilot_Adapter_R2.py

from Copilot_Adapter_R2 import Adaptee  # ตรวจสอบให้แน่ใจว่า Adaptee อยู่ใน main.py

def test_adapter():
    # Arrange
    adaptee = Adaptee()
    # Act & Assert (เพิ่มโค้ดที่เหลือของการทดสอบที่นี่)

def test_adaptee():
    # Arrange
    adaptee = Adaptee()
    # Act & Assert (เพิ่มโค้ดที่เหลือของการทดสอบที่นี่)


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