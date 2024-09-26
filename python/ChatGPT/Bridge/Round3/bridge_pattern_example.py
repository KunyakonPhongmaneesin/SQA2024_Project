# ผู้ใช้ (Device Interface)
class Device:
    def is_enabled(self):
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def get_volume(self):
        raise NotImplementedError

    def set_volume(self, volume):
        raise NotImplementedError


# การใช้งานจริง 1 (TV)
class TV(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 50

    def is_enabled(self):
        return self._enabled

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def get_volume(self):
        return self._volume

    def set_volume(self, volume):
        self._volume = max(0, min(volume, 100))  # ให้เสียงอยู่ระหว่าง 0 ถึง 100


# การใช้งานจริง 2 (Speaker)
class Speaker(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 30

    def is_enabled(self):
        return self._enabled

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def get_volume(self):
        return self._volume

    def set_volume(self, volume):
        self._volume = max(0, min(volume, 100))  # ให้เสียงอยู่ระหว่าง 0 ถึง 100


# นามธรรม (RemoteControl)
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)


# นามธรรมที่ถูกขยาย (AdvancedRemoteControl)
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)


# ตัวอย่างการใช้งาน
def main():
    tv = TV()
    speaker = Speaker()

    # การควบคุม TV ด้วยรีโมทพื้นฐาน
    basic_remote = RemoteControl(tv)
    basic_remote.power()
    print(f"สถานะการเปิด TV: {tv.is_enabled()}")
    basic_remote.volume_up()
    print(f"เสียง TV: {tv.get_volume()}")

    # การควบคุมลำโพงด้วยรีโมทขั้นสูง
    advanced_remote = AdvancedRemoteControl(speaker)
    advanced_remote.power()
    print(f"สถานะการเปิดลำโพง: {speaker.is_enabled()}")
    advanced_remote.mute()
    print(f"เสียงลำโพงหลังจากปิดเสียง: {speaker.get_volume()}")

if __name__ == "__main__":
    main()
