// Concrete implementation for Red color
class RedColor implements DrawingColor {
    @Override
    public String drawShape(String shape) {
        return "Drawing " + shape + " in Red";
    }
}
