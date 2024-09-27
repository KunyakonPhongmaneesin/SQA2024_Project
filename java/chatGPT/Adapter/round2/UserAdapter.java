// Adapter that converts LegacyUserService to the User interface
class UserAdapter implements User {
    private final LegacyUserService legacyUserService;

    public UserAdapter(LegacyUserService legacyUserService) {
        this.legacyUserService = legacyUserService;
    }

    @Override
    public String getName() {
        String details = legacyUserService.getUserDetails();
        return details.split(",")[0].trim(); // Extract name
    }

    @Override
    public int getAge() {
        String details = legacyUserService.getUserDetails();
        return Integer.parseInt(details.split(",")[1].trim()); // Extract age
    }
}
