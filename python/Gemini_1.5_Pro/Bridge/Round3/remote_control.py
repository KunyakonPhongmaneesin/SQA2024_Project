from abc import ABC, abstractmethod


class Device:
    """Implementation: Interface for devices controllable by the remote."""

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class TV(Device):
    """Concrete Implementation: A specific device (TV)."""

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("TV turned on.")

    def turn_off(self):
        self.is_on = False
        print("TV turned off.")


class RemoteControl:
    """Abstraction: The remote control interface."""

    def __init__(self, device):
        self.device = device
        self.command_history = []

    def turn_on(self):
        self.device.turn_on()
        self.command_history.append("Turn On")

    def turn_off(self):
        self.device.turn_off()
        self.command_history.append("Turn Off")

    def get_history(self):
        return self.command_history


if __name__ == "__main__":
    tv = TV()
    remote = RemoteControl(tv)

    remote.turn_on()
    remote.turn_off()
    remote.turn_on()

    print("Command History:", remote.get_history())