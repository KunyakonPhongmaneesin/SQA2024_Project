import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    @Test
    void testAddPositiveNumbers() {
        // Arrange
        Calculator calculator = new Calculator();
        int a = 2;
        int b = 3;

        // Act
        int result = calculator.add(a, b);

        // Assert
        assertEquals(5, result);
    }

    @Test
    void testAddNegativeNumbers() {
        // Arrange
        Calculator calculator = new Calculator();
        int a = -2;
        int b = 3;

        // Act
        int result = calculator.add(a, b);

        // Assert
        assertEquals(0, result);
    }

    @Test
    void testAddZero() {
        // Arrange
        Calculator calculator = new Calculator();
        int a = 0;
        int b = 3;

        // Act
        int result = calculator.add(a, b);

        // Assert
        assertEquals(0, result);
    }
}