import pytest
from Copilot_Bridge_R3 import ConcreteImplementorA, ConcreteImplementorB, RefinedAbstraction  

def test_refined_abstraction_with_concrete_implementor_a():
    # Arrange
    implementor_a = ConcreteImplementorA()
    abstraction = RefinedAbstraction(implementor_a)
    
    # Act
    result = abstraction.operation()
    
    # Assert
    assert result == "RefinedAbstraction: ConcreteImplementorA operation"

def test_refined_abstraction_with_concrete_implementor_b():
    # Arrange
    implementor_b = ConcreteImplementorB()
    abstraction = RefinedAbstraction(implementor_b)
    
    # Act
    result = abstraction.operation()
    
    # Assert
    assert result == "RefinedAbstraction: ConcreteImplementorB operation"
