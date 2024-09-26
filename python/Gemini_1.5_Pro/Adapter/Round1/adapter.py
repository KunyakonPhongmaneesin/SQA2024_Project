# Existing interface (Adaptee)
class EuropeanSocket:
    def voltage(self):
        return 230

    def live_pin(self):
        return 1

    def neutral_pin(self):
        return 2


# Target interface
class USAppliance:
    def __init__(self, adapter):
        self.adapter = adapter

    def power_on(self):
        if self.adapter.voltage() == 120 and \
           self.adapter.live_pin() == 1 and \
           self.adapter.neutral_pin() == 2:
            print("US Appliance powered on.")
        else:
            print("Incompatible power source!")


# Adapter (adapts EuropeanSocket to USAppliance)
class USAdapter:
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return 120  # Convert voltage

    def live_pin(self):
        return self.socket.live_pin()

    def neutral_pin(self):
        return self.socket.neutral_pin()


if __name__ == "__main__":
    european_socket = EuropeanSocket()
    us_adapter = USAdapter(european_socket)
    us_appliance = USAppliance(us_adapter)
    us_appliance.power_on()