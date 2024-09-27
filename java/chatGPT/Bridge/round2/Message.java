// Abstraction for Messages
abstract class Message {
    protected Messaging messaging;

    protected Message(Messaging messaging) {
        this.messaging = messaging;
    }

    public abstract String send(String content);
}
