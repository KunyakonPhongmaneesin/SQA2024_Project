class Renderer:
    def render_circle(self, radius):
        raise NotImplementedError("This method should be implemented by subclasses")

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} with VectorRenderer"

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} with RasterRenderer"

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        raise NotImplementedError("This method should be implemented by subclasses")

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        return self.renderer.render_circle(self.radius)

# Example main code
if __name__ == "__main__":
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle1 = Circle(vector_renderer, 5)
    circle2 = Circle(raster_renderer, 10)

    print(circle1.draw())
    print(circle2.draw())