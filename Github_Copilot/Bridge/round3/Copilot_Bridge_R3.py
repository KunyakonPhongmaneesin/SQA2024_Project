# Implementor Interface
class Implementor:
    def operation_impl(self):
        pass

# Concrete Implementor A
class ConcreteImplementorA(Implementor):
    def operation_impl(self):
        return "ConcreteImplementorA operation"

# Concrete Implementor B
class ConcreteImplementorB(Implementor):
    def operation_impl(self):
        return "ConcreteImplementorB operation"

# Abstraction
class Abstraction:
    def __init__(self, implementor: Implementor):
        self._implementor = implementor

    def operation(self):
        return self._implementor.operation_impl()

# Refined Abstraction
class RefinedAbstraction(Abstraction):
    def operation(self):
        return f"RefinedAbstraction: {self._implementor.operation_impl()}"

# Example usage
if __name__ == "__main__":
    implementor_a = ConcreteImplementorA()
    implementor_b = ConcreteImplementorB()

    abstraction_a = RefinedAbstraction(implementor_a)
    abstraction_b = RefinedAbstraction(implementor_b)

    print(abstraction_a.operation())  # Output: RefinedAbstraction: ConcreteImplementorA operation
    print(abstraction_b.operation())  # Output: RefinedAbstraction: ConcreteImplementorB operation