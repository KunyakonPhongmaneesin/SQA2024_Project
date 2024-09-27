public class Main {
    public static void main(String[] args) {
        LegacyUserService legacyUserService = new LegacyUserService();
        User user = new UserAdapter(legacyUserService);
        
        System.out.println("User Name: " + user.getName());
        System.out.println("User Age: " + user.getAge());
    }
}
