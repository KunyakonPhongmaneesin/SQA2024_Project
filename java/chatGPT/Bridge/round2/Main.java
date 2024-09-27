public class Main {
    public static void main(String[] args) {
        Message plainTextEmail = new PlainTextMessage(new EmailMessaging());
        Message htmlSms = new HtmlMessage(new SmsMessaging());
        
        System.out.println(plainTextEmail.send("Hello, World!"));
        System.out.println(htmlSms.send("Hello, World!"));
    }
}
