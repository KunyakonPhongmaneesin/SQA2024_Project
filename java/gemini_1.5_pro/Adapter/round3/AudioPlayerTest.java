// AudioPlayerTest.java
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import static org.junit.jupiter.api.Assertions.*;

public class AudioPlayerTest {

    @Test
    void testPlay() {
        // Arrange
        AudioPlayer audioPlayer = new AudioPlayer();
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        // Act
        audioPlayer.play("mp3", "song.mp3");
        audioPlayer.play("mp4", "video.mp4");
        audioPlayer.play("vlc", "movie.vlc");
        audioPlayer.play("avi", "unknown.avi");

        // Assert
        String expectedOutput = "Playing mp3 file. Name: song.mp3\r\n" +
                "Playing mp4 file. Name: video.mp4\r\n" +
                "Playing vlc file. Name: movie.vlc\r\n" +
                "Invalid media. avi format not supported\r\n";
        assertEquals(expectedOutput, outContent.toString());

        // Reset System.out
        System.setOut(System.out);
    }
}