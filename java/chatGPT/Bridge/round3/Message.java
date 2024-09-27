// Concrete implementation for Text Message
class TextMessage extends Message {
    public TextMessage(Notification notification) {
        super(notification);
    }

    @Override
    public String send(String content) {
        return notification.sendNotification(content);
    }
}
