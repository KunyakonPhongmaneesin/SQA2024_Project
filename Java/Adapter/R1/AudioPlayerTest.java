import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class AudioPlayerTest {

    private AudioPlayer audioPlayer;

    @BeforeEach
    public void setUp() {
        // Arrange
        audioPlayer = new AudioPlayer();
    }

    @Test
    public void testPlayMp3() {
        // Act
        audioPlayer.play("mp3", "song.mp3");

        // Assert
        // For simple output validation, you could mock or spy System.out
    }

    @Test
    public void testPlayMp4() {
        // Act
        audioPlayer.play("mp4", "movie.mp4");

        // Assert
        // Expect to see "Playing MP4 file. Name: movie.mp4"
    }

    @Test
    public void testPlayVlc() {
        // Act
        audioPlayer.play("vlc", "clip.vlc");

        // Assert
        // Expect to see "Playing VLC file. Name: clip.vlc"
    }

    @Test
    public void testInvalidFormat() {
        // Act
        audioPlayer.play("avi", "unknown.avi");

        // Assert
        // Expect to see "Invalid media. avi format not supported"
    }
}
