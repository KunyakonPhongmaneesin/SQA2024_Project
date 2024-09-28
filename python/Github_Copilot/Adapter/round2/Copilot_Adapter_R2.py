class Target:
    def request(self) -> str:
        pass

class Adaptee:
    def specific_request(self) -> str:
        return "Specific request"

class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        return self.adaptee.specific_request()

def client_code(target: Target) -> str:
    return target.request()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(client_code(adapter))  # Output: Specific request