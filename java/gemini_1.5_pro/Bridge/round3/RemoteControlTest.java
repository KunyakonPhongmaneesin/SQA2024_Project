// RemoteControlTest.java
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import static org.junit.jupiter.api.Assertions.*;

public class RemoteControlTest {

    @Test
    void testRemoteControls() {
        // Arrange
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        Car sportsCar = new SportsCar();
        RemoteControl sportsCarRemote = new SportsCarRemote(sportsCar);

        Car suv = new SUV();
        RemoteControl basicRemote = new BasicRemote(suv);

        // Act 
        sportsCarRemote.pressUnlockButton();
        sportsCarRemote.pressStartButton();
        ((SportsCarRemote) sportsCarRemote).pressBoostButton();
        sportsCarRemote.pressStopButton();
        sportsCarRemote.pressLockButton();

        basicRemote.pressUnlockButton();
        basicRemote.pressStartButton();
        basicRemote.pressStopButton();
        basicRemote.pressLockButton();

        // Assert
        String expectedOutput = "Sports car unlocked.\r\n" +
                "Sports car engine roaring to life!\r\n" +
                "Engaging boost! Zoom zoom!\r\n" +
                "Sports car engine turned off.\r\n" +
                "Sports car locked.\r\n" +
                "SUV unlocked.\r\n" +
                "SUV engine started.\r\n" +
                "SUV engine turned off.\r\n" +
                "SUV locked.\r\n";

        assertEquals(expectedOutput, outContent.toString());

        // Reset System.out
        System.setOut(System.out);
    }
}