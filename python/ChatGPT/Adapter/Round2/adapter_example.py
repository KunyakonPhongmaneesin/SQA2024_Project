# Legacy Printer class
class Printer:
    def print_text(self, text: str) -> str:
        return f"Printing: {text}"

# New Logger class
class Logger:
    def log_message(self, message: str) -> str:
        return f"Logging: {message}"

# Adapter class to adapt Logger to Printer's interface
class LoggerAdapter(Printer):
    def __init__(self, logger: Logger):
        self.logger = logger

    def print_text(self, text: str) -> str:
        # Adapting log_message to the print_text method
        return self.logger.log_message(text)

# Example usage
def main():
    printer = Printer()
    logger = Logger()
    logger_adapter = LoggerAdapter(logger)

    # Both objects can now use the 'print_text' method
    print(printer.print_text("Hello from Printer"))
    print(logger_adapter.print_text("Hello from Logger via Adapter"))

if __name__ == "__main__":
    main()
