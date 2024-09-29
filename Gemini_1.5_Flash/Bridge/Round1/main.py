class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print(f"Drawing a circle in {self.color} color")

class Square(Shape):
    def draw(self):
        print(f"Drawing a square in {self.color} color")

# สร้างออบเจ็กต์ของ Circle และ Square
circle = Circle("red")
square = Square("blue")

# เรียกใช้ฟังก์ชัน draw
circle.draw()  # จะแสดงผล: Drawing a circle in red color
square.draw()  # จะแสดงผล: Drawing a square in blue color
