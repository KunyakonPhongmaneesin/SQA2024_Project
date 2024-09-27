import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class StringUtilitiesTest {

    @Test
    void testCapitalize_Null() {
        // Arrange
        StringUtilities utilities = new StringUtilities();
        String input = null;

        // Act
        String result = utilities.capitalize(input);

        // Assert
        assertNull(result);
    }

    @Test
    void testCapitalize_Empty() {
        // Arrange
        StringUtilities utilities = new StringUtilities();
        String input = "";

        // Act
        String result = utilities.capitalize(input);

        // Assert
        assertEquals("", result);
    }

    @Test
    void testCapitalize_NonEmpty() {
        // Arrange
        StringUtilities utilities = new StringUtilities();
        String input = "hello";

        // Act
        String result = utilities.capitalize(input);

        // Assert
        assertEquals("Hello", result);
    }
}