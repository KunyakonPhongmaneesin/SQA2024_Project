import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class UserAdapterTest {

    @Test
    void testGetNameAndAge() {
        // Arrange
        LegacyUserService legacyUserService = new LegacyUserService();
        User user = new UserAdapter(legacyUserService);

        // Act
        String name = user.getName();
        int age = user.getAge();

        // Assert
        assertEquals("John Doe", name);
        assertEquals(30, age);
    }
}
