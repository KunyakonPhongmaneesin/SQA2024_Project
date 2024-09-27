
import static org.mockito.Mockito.*;
import org.junit.jupiter.api.Test;
import com.example.Leg

import org.junit.Test;

class LoggerAdapterTest {

    @Test
    void testLog() {
        // Arrange
        LegacyLogger legacyLoggerMock = mock(LegacyLogger.class);
        Logger logger = new LoggerAdapter(legacyLoggerMock);
        String testMessage = "Hello, Adapter Pattern!";

        // Act
        logger.log(testMessage);

        // Assert
        verify(legacyLoggerMock).logMessage(testMessage);
    }
}
