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

        Light light = new Light();
        Speaker speaker = new Speaker();

        BasicRemote basicRemote = new BasicRemote(light);
        AdvancedRemote advancedRemote = new AdvancedRemote(speaker);

        // Act & Assert (using System.out for demonstration)
        basicRemote.togglePower(); // Turn on light
        basicRemote.togglePower(); // Turn off light

        advancedRemote.togglePower(); // Turn on speaker
        ((AdvancedRemote) advancedRemote).volumeUp();
        ((AdvancedRemote) advancedRemote).volumeDown();
        advancedRemote.togglePower(); // Dim speaker

        String expectedOutput = "Light is ON\r\n" +
                "Light is OFF\r\n" +
                "Speaker is ON\r\n" +
                "Speaker volume set to: 60%\r\n" +
                "Speaker volume set to: 50%\r\n" +
                "Speaker is OFF\r\n"; // Expected output based on console prints

        assertEquals(expectedOutput, outContent.toString()); 

        // Reset System.out
        System.setOut(System.out); 
    }
}