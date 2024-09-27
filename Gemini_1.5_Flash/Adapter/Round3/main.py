def add_numbers(a, b):
    return a + b

class Shape:
    def draw(self):
        pass

class OldRectangle:
    def draw_old(self):
        print("Drawing an old rectangle")

class RectangleAdapter(Shape):
    def __init__(self, old_rectangle):
        self.old_rectangle = old_rectangle

    def draw(self):
        self.old_rectangle.draw_old()

old_rectangle = OldRectangle()
adapter = RectangleAdapter(old_rectangle)

shapes = [adapter]

for shape in shapes:
    shape.draw()