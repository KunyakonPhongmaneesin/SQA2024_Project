// Concrete implementation for HTML Message
class HtmlMessage extends Message {
    public HtmlMessage(Messaging messaging) {
        super(messaging);
    }

    @Override
    public String send(String content) {
        return messaging.sendMessage("<html>" + content + "</html>");
    }
}
