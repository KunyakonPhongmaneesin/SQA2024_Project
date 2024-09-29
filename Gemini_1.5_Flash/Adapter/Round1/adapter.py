# adapter.py

class LegacySystem:
    def specific_request(self) -> str:
        return "Legacy system response"


class TargetInterface:
    def request(self) -> str:
        raise NotImplementedError("You should implement this method!")


class Adapter(TargetInterface):
    def __init__(self, legacy_system: LegacySystem):
        self._legacy_system = legacy_system

    def request(self) -> str:
        # Adapting the legacy system's response to the target interface
        return self._legacy_system.specific_request()


def main():
    legacy_system = LegacySystem()
    adapter = Adapter(legacy_system)
    print(adapter.request())  # This would print: "Legacy system response"


if __name__ == "__main__":
    main()
