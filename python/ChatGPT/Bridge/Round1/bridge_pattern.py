# นามธรรม (Remote Control)
class RemoteControl:
    def __init__(self, device):
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


# นามธรรมที่ถูกขยาย (Advanced Remote Control)
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)


# ผู้ใช้ (Device)
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


# การใช้งานจริง (TV)
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
        self._volume = max(0, min(volume, 100))  # ให้ค่าเสียงอยู่ระหว่าง 0 ถึง 100


# การใช้งานจริง (Radio)
class Radio(Device):
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
        self._volume = max(0, min(volume, 100))  # ให้ค่าเสียงอยู่ระหว่าง 0 ถึง 100


# ตัวอย่างการใช้งาน
def main():
    tv = TV()
    remote = RemoteControl(tv)
    advanced_remote = AdvancedRemoteControl(tv)

    # ทดสอบรีโมตแบบธรรมดากับ TV
    remote.power()
    print(f"TV เปิดอยู่: {tv.is_enabled()}")
    remote.volume_up()
    print(f"เสียงของ TV หลังจากเพิ่ม: {tv.get_volume()}")

    # ทดสอบรีโมตแบบ Advanced กับ TV
    advanced_remote.mute()
    print(f"เสียงของ TV หลังจากปิดเสียง: {tv.get_volume()}")

    # ใช้กับวิทยุ
    radio = Radio()
    radio_remote = RemoteControl(radio)
    radio_remote.power()
    print(f"Radio เปิดอยู่: {radio.is_enabled()}")
    radio_remote.volume_down()
    print(f"เสียงของ Radio หลังจากลดเสียง: {radio.get_volume()}")

if __name__ == "__main__":
    main()
