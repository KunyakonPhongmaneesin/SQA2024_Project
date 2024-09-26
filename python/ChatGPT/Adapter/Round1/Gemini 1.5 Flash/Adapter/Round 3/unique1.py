class LegacyCalculator:
    def add(self, x, y):
        return x + y

class ModernCalculatorAdapter:
    def __init__(self, legacy_calculator):
        self.legacy_calculator = legacy_calculator

    def sum(self, numbers):
        result = 0
        for number in numbers:
            result += self.legacy_calculator.add(result, number)
        return result