import pytest 
from bridge_pattern_unique import TV, Radio, RemoteControl, AdvancedRemoteControl

# ทดสอบตามโครงสร้าง AAA (Arrange, Act, Assert)

def test_tv_power():
    # Arrange (จัดเตรียม)
    tv = TV()
    remote = RemoteControl(tv)

    # Act (กระทำ)
    remote.power()  # เปิด TV
    is_enabled = tv.is_enabled()

    # Assert (ตรวจสอบ)
    assert is_enabled is True

def test_tv_volume_up():
    # Arrange
    tv = TV()
    remote = RemoteControl(tv)

    # Act
    remote.volume_up()  # เพิ่มเสียง 10 หน่วย
    volume = tv.get_volume()

    # Assert
    assert volume == 60

def test_tv_mute():
    # Arrange
    tv = TV()
    advanced_remote = AdvancedRemoteControl(tv)

    # Act
    advanced_remote.mute()  # ปิดเสียง TV
    volume = tv.get_volume()

    # Assert
    assert volume == 0

def test_radio_power():
    # Arrange
    radio = Radio()
    remote = RemoteControl(radio)

    # Act
    remote.power()  # เปิดวิทยุ
    is_enabled = radio.is_enabled()

    # Assert
    assert is_enabled is True

def test_radio_volume_down():
    # Arrange
    radio = Radio()
    remote = RemoteControl(radio)

    # Act
    remote.volume_down()  # ลดเสียงลง 10 หน่วย
    volume = radio.get_volume()

    # Assert
    assert volume == 20

# ทดสอบครอบคลุมทุกเส้นทาง (100% Branch Coverage)
def test_advanced_remote_mute_on_radio():
    # Arrange
    radio = Radio()
    advanced_remote = AdvancedRemoteControl(radio)

    # Act
    advanced_remote.mute()  # ปิดเสียงวิทยุ
    volume = radio.get_volume()

    # Assert
    assert volume == 0
