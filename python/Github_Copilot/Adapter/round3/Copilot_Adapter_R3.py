# Python

from abc import ABC, abstractmethod

# Step 1: Define the implementer interface
class Implementer(ABC):
    @abstractmethod
    def operation_impl(self) -> str:
        pass

# Step 2: Implement concrete classes for the implementer
class ConcreteImplementerA(Implementer):
    def operation_impl(self) -> str:
        return "ConcreteImplementerA operation"

class ConcreteImplementerB(Implementer):
    def operation_impl(self) -> str:
        return "ConcreteImplementerB operation"

# Step 3: Define the abstraction class
class Abstraction:
    def __init__(self, implementer: Implementer):
        self.implementer = implementer

    def operation(self) -> str:
        return self.implementer.operation_impl()

# Step 4: Implement refined abstractions
class RefinedAbstractionA(Abstraction):
    def operation(self) -> str:
        return f"RefinedAbstractionA: {self.implementer.operation_impl()}"

class RefinedAbstractionB(Abstraction):
    def operation(self) -> str:
        return f"RefinedAbstractionB: {self.implementer.operation_impl()}"

# Example usage
if __name__ == "__main__":
    implementer_a = ConcreteImplementerA()
    abstraction_a = RefinedAbstractionA(implementer_a)
    print(abstraction_a.operation())

    implementer_b = ConcreteImplementerB()
    abstraction_b = RefinedAbstractionB(implementer_b)
    print(abstraction_b.operation())