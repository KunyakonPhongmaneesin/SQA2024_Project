package Java.Bridge.R3;

// DeviceTest.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class DeviceTest {

    @Test
    public void testTelevisionWithTVRemote() {
        // Arrange
        Remote tvRemote = new TVRemote();
        Device tv = new Television(tvRemote);

        // Act & Assert
        assertDoesNotThrow(() -> tv.operate());
    }

    @Test
    public void testAirConditionerWithACRemote() {
        // Arrange
        Remote acRemote = new ACRemote();
        Device ac = new AirConditioner(acRemote);

        // Act & Assert
        assertDoesNotThrow(() -> ac.operate());
    }
}
