// Concrete implementation for Blue color
class BlueColor implements DrawingColor {
    @Override
    public String drawShape(String shape) {
        return "Drawing " + shape + " in Blue";
    }
}
