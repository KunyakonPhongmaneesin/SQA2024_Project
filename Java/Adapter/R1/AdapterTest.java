import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import org.junit.jupiter.api.Test;

public class AdapterTest {

    @Test
    public void testRequest() {
        // Arrange
        Adaptee adaptee = new Adaptee();
        Target target = new Adapter(adaptee);

        // Act & Assert
        assertDoesNotThrow(() -> target.request());
    }
    // Adaptee.java
    class Adaptee {
    public void specificRequest() {
        System.out.println("Called specificRequest()");
    }
    
    }
    // Target.java
    interface Target {
    void request();
    }
    // Adapter.java
class Adapter implements Target {
    private Adaptee adaptee;

    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }

    @Override
    public void request() {
        adaptee.specificRequest();
    }
}
}
