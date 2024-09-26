
from remote_control import Device, TV, RemoteControl

class MockDevice(Device):
    def __init__(self):
        self.on_count = 0
        self.off_count = 0

    def turn_on(self):
        self.on_count += 1

    def turn_off(self):
        self.off_count += 1

def test_remote_control_commands():
    # Arrange
    mock_device = MockDevice()
    remote = RemoteControl(mock_device)

    # Act
    remote.turn_on()
    remote.turn_off()
    remote.turn_on()

    # Assert
    assert mock_device.on_count == 2
    assert mock_device.off_count == 1
    assert remote.get_history() == ["Turn On", "Turn Off", "Turn On"]

def test_remote_with_tv():
    # Arrange
    tv = TV()
    remote = RemoteControl(tv)

    # Act
    remote.turn_on()

    # Assert
    assert tv.is_on is True 

def test_remote_history():
    # Arrange
    device = TV()
    remote = RemoteControl(device)

    # Act
    remote.turn_on()
    remote.turn_off()

    # Assert
    assert remote.get_history() == ["Turn On", "Turn Off"]