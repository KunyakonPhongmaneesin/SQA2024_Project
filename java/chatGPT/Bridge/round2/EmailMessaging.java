// Concrete implementation for Email
class EmailMessaging implements Messaging {
    @Override
    public String sendMessage(String message) {
        return "Email: " + message;
    }
}
