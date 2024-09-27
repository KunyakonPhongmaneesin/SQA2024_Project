import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CelsiusToFahrenheitAdapterTest {

    @Test
    void testGetTemperature() {
        // Arrange
        double celsius = 25;
        CelsiusTemperature celsiusTemperature = new CelsiusTemperature(celsius);
        CelsiusToFahrenheitAdapter adapter = new CelsiusToFahrenheitAdapter(celsiusTemperature);

        // Act
        double fahrenheit = adapter.getTemperature();

        // Assert
        assertEquals(77.0, fahrenheit, 0.01);
    }
}