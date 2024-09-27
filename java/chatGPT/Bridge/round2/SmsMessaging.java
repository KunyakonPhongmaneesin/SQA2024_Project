// Concrete implementation for SMS
class SmsMessaging implements Messaging {
    @Override
    public String sendMessage(String message) {
        return "SMS: " + message;
    }
}
