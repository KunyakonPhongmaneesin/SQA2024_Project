import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class RefinedAbstractionTest {

    @Test
    public void testOperationWithImplementerA() {
        // Arrange
        Implementer implementerA = new ConcreteImplementerA();
        Abstraction abstraction = new RefinedAbstraction(implementerA);

        // Act & Assert
        assertDoesNotThrow(() -> abstraction.operation());
    }

    @Test
    public void testOperationWithImplementerB() {
        // Arrange
        Implementer implementerB = new ConcreteImplementerB();
        Abstraction abstraction = new RefinedAbstraction(implementerB);

        // Act & Assert
        assertDoesNotThrow(() -> abstraction.operation());
    }
}