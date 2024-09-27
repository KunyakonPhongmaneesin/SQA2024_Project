import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class MessageTest {

    @Test
    void testSendPlainTextEmail() {
        // Arrange
        Messaging email = new EmailMessaging();
        Message plainTextMessage = new PlainTextMessage(email);

        // Act
        String result = plainTextMessage.send("Hello, World!");

        // Assert
        assertEquals("Email: Hello, World!", result);
    }

    @Test
    void testSendHtmlSms() {
        // Arrange
        Messaging sms = new SmsMessaging();
        Message htmlMessage = new HtmlMessage(sms);

        // Act
        String result = htmlMessage.send("Hello, World!");

        // Assert
        assertEquals("SMS: <html>Hello, World!</html>", result);
    }
}
