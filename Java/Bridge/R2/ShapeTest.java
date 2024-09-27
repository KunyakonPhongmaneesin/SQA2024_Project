package Java.Bridge.R2;

// ShapeTest.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ShapeTest {

    @Test
    public void testRedCircle() {
        // Arrange
        Color red = new RedColor();
        Shape redCircle = new Circle(red);

        // Act & Assert
        assertDoesNotThrow(() -> redCircle.applyColor());
    }

    @Test
    public void testBlueSquare() {
        // Arrange
        Color blue = new BlueColor();
        Shape blueSquare = new Square(blue);

        // Act & Assert
        assertDoesNotThrow(() -> blueSquare.applyColor());
    }
}
