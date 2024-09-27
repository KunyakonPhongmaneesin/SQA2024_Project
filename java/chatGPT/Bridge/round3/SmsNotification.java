// Concrete implementation for SMS
class SmsNotification implements Notification {
    @Override
    public String sendNotification(String message) {
        return "SMS: " + message;
    }
}
