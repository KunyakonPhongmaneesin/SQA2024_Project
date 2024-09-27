import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class ShapeTest {

    @Test
    void testDrawCircleWithRedColor() {
        // Arrange
        DrawingColor redColor = new RedColor();
        Shape circle = new Circle(redColor);

        // Act
        String result = circle.draw();

        // Assert
        assertEquals("Drawing Circle in Red", result);
    }

    @Test
    void testDrawSquareWithBlueColor() {
        // Arrange
        DrawingColor blueColor = new BlueColor();
        Shape square = new Square(blueColor);

        // Act
        String result = square.draw();

        // Assert
        assertEquals("Drawing Square in Blue", result);
    }
}
