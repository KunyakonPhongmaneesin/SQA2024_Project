# Python

from abc import ABC, abstractmethod

# Step 1: Define the implementer interface
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float) -> str:
        pass

# Step 2: Implement concrete classes for the implementer
class VectorRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"Drawing a circle of radius {radius} with VectorRenderer"

class RasterRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"Drawing a circle of radius {radius} with RasterRenderer"

# Step 3: Define the abstraction class
class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def draw(self) -> str:
        pass

    def resize(self, factor: float):
        pass

# Step 4: Implement refined abstractions
class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> str:
        return self.renderer.render_circle(self.radius)

    def resize(self, factor: float):
        self.radius *= factor

# Example usage
if __name__ == "__main__":
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle = Circle(vector_renderer, 5)
    print(circle.draw())
    circle.resize(2)
    print(circle.draw())

    circle = Circle(raster_renderer, 5)
    print(circle.draw())
    circle.resize(2)
    print(circle.draw())