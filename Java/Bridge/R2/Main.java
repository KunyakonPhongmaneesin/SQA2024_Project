package Java.Bridge.R2;

// Main.java
public class Main {
    public static void main(String[] args) {
        Shape redCircle = new Circle(new RedColor());
        redCircle.applyColor();

        Shape blueSquare = new Square(new BlueColor());
        blueSquare.applyColor();
    }
}
