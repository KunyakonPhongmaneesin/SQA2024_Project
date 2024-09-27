from abc import ABC, abstractmethod

# Abstraction
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# Concrete Abstraction
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        return f"Drawing a {self.color.apply_color()} circle with radius {self.radius}"

# Another Concrete Abstraction
class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def draw(self):
        return f"Drawing a {self.color.apply_color()} square with side length {self.side_length}"

# Implementor Interface
class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass

# Concrete Implementor A
class RedColor(Color):
    def apply_color(self):
        return "red"

# Concrete Implementor B
class BlueColor(Color):
    def apply_color(self):
        return "blue"

# Main execution (optional)
if __name__ == "__main__":
    red_circle = Circle(RedColor(), 5)
    blue_square = Square(BlueColor(), 10)
    print(red_circle.draw())  # Output: Drawing a red circle with radius 5
    print(blue_square.draw())  # Output: Drawing a blue square with side length 10
