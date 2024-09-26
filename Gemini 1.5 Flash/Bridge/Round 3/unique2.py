def is_palindrome(word):
    """Checks if a given word is a palindrome."""
    return word == word[::-1]

# Test case
def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False