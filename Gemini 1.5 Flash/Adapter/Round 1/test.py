import ast
import inspect

def generate_pytest_code(function_code):
    """Generates Pytest code for a given Python function.

    Args:
        function_code: The Python code of the function to test.

    Returns:
        The generated Pytest code.
    """

    # Parse the function code into an AST
    tree = ast.parse(function_code)

    # Extract function name and parameters
    function_name = tree.body[0].name
    parameters = [arg.arg for arg in tree.body[0].args.args]

    # Generate test cases based on branch coverage
    test_cases = []
    for branch in get_branches(tree):
        test_case = generate_test_case(function_name, parameters, branch)
        test_cases.append(test_case)

    # Generate Pytest code
    pytest_code = f"""
import pytest

def test_{function_name}():
    {''.join(test_cases)}
"""

    return pytest_code

def get_branches(tree):
    """Gets all branches in a given AST.

    Args:
        tree: The AST to analyze.

    Returns:
        A list of branches, where each branch is a tuple of (condition, true_value, false_value).
    """

    branches = []
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            condition = ast.dump(node.test)
            true_value = ast.dump(node.body[0])
            false_value = ast.dump(node.orelse[0]) if node.orelse else None
            branches.append((condition, true_value, false_value))
    return branches

def generate_test_case(function_name, parameters, branch):
    """Generates a test case for a given branch.

    Args:
        function_name: The name of the function to test.
        parameters: A list of parameters for the function.
        branch: A tuple of (condition, true_value, false_value) representing the branch.

    Returns:
        The generated test case code.
    """

    # Create a test case based on the branch condition and expected outcomes
    condition, true_value, false_value = branch
    test_case = f"""
    {function_name}({', '.join(parameters)}) == {true_value} if {condition} else {false_value}
    """
    return test_case

# Example usage:
function_code = """
def my_function(x, y):
    if x > y:
        return x
    else:
        return y
"""

pytest_code = generate_pytest_code(function_code)
print(pytest_code)