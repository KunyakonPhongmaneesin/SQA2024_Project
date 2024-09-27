import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class StringManipulatorTest {

    @Test
    void testReverseString_Null() {
        // Arrange
        StringManipulator manipulator = new StringManipulator();
        String input = null;

        // Act
        String result = manipulator.reverseString(input);

        // Assert
        assertNull(result);
    }

    @Test
    void testReverseString_Empty() {
        // Arrange
        StringManipulator manipulator = new StringManipulator();
        String input = "";

        // Act
        String result = manipulator.reverseString(input);

        // Assert
        assertEquals("", result);
    }

    @Test
    void testReverseString_NonEmpty() {
        // Arrange
        StringManipulator manipulator = new StringManipulator();
        String input = "hello";

        // Act
        String result = manipulator.reverseString(input);

        // Assert
        assertEquals("olleh", result);
    }
}