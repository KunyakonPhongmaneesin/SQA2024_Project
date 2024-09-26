import pytest
from bridge_pattern_example import TV, Speaker, RemoteControl, AdvancedRemoteControl

# ทดสอบตามโครงสร้าง AAA (Arrange, Act, Assert)

def test_tv_power():
    # Arrange (เตรียม)
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

def test_speaker_power():
    # Arrange
    speaker = Speaker()
    remote = RemoteControl(speaker)

    # Act
    remote.power()  # เปิดลำโพง
    is_enabled = speaker.is_enabled()

    # Assert
    assert is_enabled is True

def test_speaker_mute():
    # Arrange
    speaker = Speaker()
    advanced_remote = AdvancedRemoteControl(speaker)

    # Act
    advanced_remote.mute()  # ปิดเสียงลำโพง
    volume = speaker.get_volume()

    # Assert
    assert volume == 0

# ทดสอบการครอบคลุม 100% ของทุกเส้นทาง (Branch Coverage)
def test_branch_coverage_for_both_devices():
    # Arrange
    tv = TV()
    speaker = Speaker()
    remote_tv = RemoteControl(tv)
    advanced_remote_speaker = AdvancedRemoteControl(speaker)

    # Act & Assert (TV)
    remote_tv.power()
    assert tv.is_enabled() is True
    remote_tv.volume_down()
    assert tv.get_volume() == 50

    # Act & Assert (ลำโพง)
    advanced_remote_speaker.power()
    assert speaker.is_enabled() is True
    advanced_remote_speaker.mute()
    assert speaker.get_volume() == 0
