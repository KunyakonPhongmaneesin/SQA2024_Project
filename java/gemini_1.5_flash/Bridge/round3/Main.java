import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DateValidatorTest {

    @Test
    void testIsValidDate_YearOutOfRange_TooLow() {
        // Arrange
        DateValidator validator = new DateValidator();
        int year = 1899;
        int month = 12;
        int day = 31;

        // Act
        boolean result = validator.isValidDate(year, month, day);

        // Assert
        assertFalse(result);
    }

    @Test
    void testIsValidDate_YearOutOfRange_TooHigh() {
        // Arrange
        DateValidator validator = new DateValidator();
        int year = 2101;
        int month = 12;
        int day = 31;

        // Act
        boolean result = validator.isValidDate(year, month, day);

        // Assert
        assertFalse(result);
    }

    @Test
    void testIsValidDate_MonthOutOfRange_TooLow() {
        // Arrange
        DateValidator validator = new DateValidator();
        int year = 2000;
        int month = 0;
        int day = 31;

        // Act
        boolean result = validator.isValidDate(year, month, day);

        // Assert
        assertFalse(result);
    }

    @Test
    void testIsValidDate_MonthOutOfRange_TooHigh() {
        // Arrange
        DateValidator validator = new DateValidator();
        int year = 2000;
        int month = 13;
        int day = 31;

        // Act
        boolean result = validator.isValidDate(year, month, day);

        // Assert
        assertFalse(result);
    }

    @Test
    void testIsValidDate_DayOutOfRange_TooLow() {
        // Arrange
        DateValidator validator = new DateValidator();
        int year = 2000;
        int month = 12;
        int day = 0;

        // Act
        boolean result = validator.isValidDate(year, month, day);

        // Assert
        assertFalse(result);
    }

    @Test
    void testIsValidDate_DayOutOfRange_TooHigh() {
        // Arrange
        DateValidator validator = new DateValidator();
        int year = 2000;
        int month = 12;
        int day = 32;

        // Act
        boolean result = validator.isValidDate(year, month, day);

        // Assert
        assertFalse(result);
    }

    @Test
    void testIsValidDate_February_TooManyDays() {
        // Arrange
        DateValidator validator = new DateValidator();
        int year = 2000;
        int month = 2;
        int day = 30;

        // Act
        boolean result = validator.isValidDate(year, month, day);

        // Assert
        assertFalse(result);
    }

    @Test
    void testIsValidDate_ShortMonth_TooManyDays() {
        // Arrange
        DateValidator validator = new DateValidator();
        int year = 2000;
        int month = 4;
        int day = 31;

        // Act
        boolean result = validator.isValidDate(year, month, day);

        // Assert
        assertFalse(result);
    }

    @Test
    void testIsValidDate_ValidDate() {
        // Arrange
        DateValidator validator = new DateValidator();
        int year = 2000;
        int month = 12;
        int day = 31;

        // Act
        boolean result = validator.isValidDate(year, month, day);

        // Assert
        assertTrue(result);
    }
}