// Concrete implementation for Circle
class Circle extends Shape {
    public Circle(DrawingColor color) {
        super(color);
    }

    @Override
    public String draw() {
        return color.drawShape("Circle");
    }
}
