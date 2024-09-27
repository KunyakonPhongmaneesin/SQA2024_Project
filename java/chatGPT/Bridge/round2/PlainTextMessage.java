// Concrete implementation for Plain Text Message
class PlainTextMessage extends Message {
    public PlainTextMessage(Messaging messaging) {
        super(messaging);
    }

    @Override
    public String send(String content) {
        return messaging.sendMessage(content);
    }
}
