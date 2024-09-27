
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
