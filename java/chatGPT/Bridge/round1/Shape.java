// Abstraction for Shapes
abstract class Shape {
    protected DrawingColor color;

    protected Shape(DrawingColor color) {
        this.color = color;
    }

    public abstract String draw();
}
