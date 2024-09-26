# Python

from abc import ABC, abstractmethod

# Step 1: Define the interface
class Target(ABC):
    @abstractmethod
    def request(self) -> str:
        pass

# Step 2: Implement the concrete class
class Adaptee:
    def specific_request(self) -> str:
        return "Adaptee's specific request"

# Step 3: Implement the adapter class
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        return self.adaptee.specific_request()

# Step 4: Client code
def client_code(target: Target) -> str:
    return target.request()

# Example usage
if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(client_code(adapter))