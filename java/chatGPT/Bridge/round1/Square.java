// Concrete implementation for Square
class Square extends Shape {
    public Square(DrawingColor color) {
        super(color);
    }

    @Override
    public String draw() {
        return color.drawShape("Square");
    }
}
