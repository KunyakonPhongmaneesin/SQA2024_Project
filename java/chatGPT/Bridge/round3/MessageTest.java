import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class MessageTest {

    @Test
    void testSendTextEmail() {
        // Arrange
        Notification email = new EmailNotification();
        Message textMessage = new TextMessage(email);

        // Act
        String result = textMessage.send("Hello, World!");

        // Assert
        assertEquals("Email: Hello, World!", result);
    }

    @Test
    void testSendHtmlSms() {
        // Arrange
        Notification sms = new SmsNotification();
        Message htmlMessage = new HtmlMessage(sms);

        // Act
        String result = htmlMessage.send("Hello, World!");

        // Assert
        assertEquals("SMS: <html>Hello, World!</html>", result);
    }
}
