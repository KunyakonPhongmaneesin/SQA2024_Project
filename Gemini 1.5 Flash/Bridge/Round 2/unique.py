def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Test case
def test_factorial():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(0) == 1