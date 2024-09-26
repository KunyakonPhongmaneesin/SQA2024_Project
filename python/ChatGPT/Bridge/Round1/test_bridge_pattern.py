import pytest
from bridge_pattern import TV, Radio, RemoteControl, AdvancedRemoteControl

# Test using the AAA (Arrange, Act, Assert) pattern

def test_tv_power():
    # Arrange
    tv = TV()
    remote = RemoteControl(tv)

    # Act
    remote.power()  # Turns the TV on
    is_enabled = tv.is_enabled()

    # Assert
    assert is_enabled is True

def test_tv_volume_up():
    # Arrange
    tv = TV()
    remote = RemoteControl(tv)

    # Act
    remote.volume_up()  # Increases the volume by 10
    volume = tv.get_volume()

    # Assert
    assert volume == 60

def test_tv_mute():
    # Arrange
    tv = TV()
    advanced_remote = AdvancedRemoteControl(tv)

    # Act
    advanced_remote.mute()  # Mutes the TV
    volume = tv.get_volume()

    # Assert
    assert volume == 0

def test_radio_power():
    # Arrange
    radio = Radio()
    remote = RemoteControl(radio)

    # Act
    remote.power()  # Turns the radio on
    is_enabled = radio.is_enabled()

    # Assert
    assert is_enabled is True

def test_radio_volume_down():
    # Arrange
    radio = Radio()
    remote = RemoteControl(radio)

    # Act
    remote.volume_down()  # Decreases the volume by 10
    volume = radio.get_volume()

    # Assert
    assert volume == 20

# 100% Branch Coverage Test
def test_advanced_remote_mute_on_radio():
    # Arrange
    radio = Radio()
    advanced_remote = AdvancedRemoteControl(radio)

    # Act
    advanced_remote.mute()  # Mute the radio
    volume = radio.get_volume()

    # Assert
    assert volume == 0
