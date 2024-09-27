public class Main {
    public static void main(String[] args) {
        Message textEmail = new TextMessage(new EmailNotification());
        Message htmlSms = new HtmlMessage(new SmsNotification());
        
        System.out.println(textEmail.send("Hello, World!"));
        System.out.println(htmlSms.send("Hello, World!"));
    }
}
