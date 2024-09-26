import pytest
from adapter_example import Printer, Logger, LoggerAdapter

# Test using the AAA pattern (Arrange, Act, Assert)

def test_printer_print_text():
    # Arrange
    printer = Printer()

    # Act
    result = printer.print_text("Hello from Printer")

    # Assert
    assert result == "Printing: Hello from Printer"

def test_logger_adapter_print_text():
    # Arrange
    logger = Logger()
    logger_adapter = LoggerAdapter(logger)

    # Act
    result = logger_adapter.print_text("Hello from Logger via Adapter")

    # Assert
    assert result == "Logging: Hello from Logger via Adapter"

# 100% Branch Coverage Test:
def test_adapter_branch_coverage():
    # Arrange
    printer = Printer()
    logger = Logger()
    logger_adapter = LoggerAdapter(logger)

    # Act & Assert
    assert printer.print_text("Branch Coverage Test for Printer") == "Printing: Branch Coverage Test for Printer"
    assert logger_adapter.print_text("Branch Coverage Test for Logger Adapter") == "Logging: Branch Coverage Test for Logger Adapter"
