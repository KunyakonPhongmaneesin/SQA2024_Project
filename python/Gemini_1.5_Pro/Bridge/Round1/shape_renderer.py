from abc import ABC, abstractmethod

# Abstraction
class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass


# Concrete Implementations of Shape
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.draw_circle(self.radius)


class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.draw_square(self.side)


# Implementation
class Renderer(ABC):
    @abstractmethod
    def draw_circle(self, radius):
        pass

    @abstractmethod
    def draw_square(self, side):
        pass


# Concrete Implementations of Renderer
class VectorRenderer(Renderer):
    def draw_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using vectors.")

    def draw_square(self, side):
        print(f"Drawing a square with side {side} using vectors.")


class RasterRenderer(Renderer):
    def draw_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using raster graphics.")

    def draw_square(self, side):
        print(f"Drawing a square with side {side} using raster graphics.")


if __name__ == "__main__":
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle = Circle(vector_renderer, 5)
    circle.draw()

    square = Square(raster_renderer, 10)
    square.draw()