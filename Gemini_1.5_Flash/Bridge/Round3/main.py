from abc import ABC, abstractmethod

# Abstract Base Class
class CodeGenerator(ABC):
    @abstractmethod
    def generate_code(self, requirements):
        pass

# Code generator class for Pytest
class PytestCodeGenerator(CodeGenerator):
    def generate_code(self, requirements):
        # Generate Pytest code based on the requirements
        pytest_code = """
import pytest
from main import calculate_factorial, is_palindrome

def test_calculate_factorial():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    assert calculate_factorial(5) == 120

def test_is_palindrome():
    assert is_palindrome('') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('python') == False
"""
        return pytest_code

# Main execution
def main():
    requirements = {
        "functions": [
            {"name": "calculate_factorial", "params": [0, 1, 5]},
            {"name": "is_palindrome", "params": ["", "racecar", "python"]}
        ]
    }

    code_generator = PytestCodeGenerator()
    pytest_code = code_generator.generate_code(requirements)

    # Save the generated Pytest code to a file
    with open("test_code.py", "w") as f:
        f.write(pytest_code)

    # Print to indicate that the file has been created
    print("Pytest code has been generated and saved to test_code.py")
    print("You can run 'pytest test_code.py' to execute the tests.")

# Functions to test
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def is_palindrome(word):
    """Checks if a given word is a palindrome."""
    return word == word[::-1]

if __name__ == "__main__":
    main()
