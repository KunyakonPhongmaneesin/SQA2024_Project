// AdapterTest.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AdapterTest {

    @Test
    public void testExecute() {
        // Arrange
        Adaptee adaptee = new Adaptee();
        Target target = new Adapter(adaptee);

        // Act
        target.execute();

        // Assert
        // Since the method prints to the console, we can't assert the output directly.
        // Instead, we can ensure no exceptions are thrown.
        assertDoesNotThrow(() -> target.execute());
    }
}