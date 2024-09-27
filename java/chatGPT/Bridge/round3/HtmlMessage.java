// Concrete implementation for HTML Message
class HtmlMessage extends Message {
    public HtmlMessage(Notification notification) {
        super(notification);
    }

    @Override
    public String send(String content) {
        return notification.sendNotification("<html>" + content + "</html>");
    }
}
