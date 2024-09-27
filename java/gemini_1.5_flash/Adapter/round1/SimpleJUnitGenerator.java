import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SimpleJUnitGenerator implements JUnitTestGenerator {

    @Override
    public String generateTestCode(String className, String codeToTest) {
        // Simple implementation that generates basic test code with AAA structure
        return "import org.junit.jupiter.api.Test;\n" +
               "import static org.junit.jupiter.api.Assertions.*;\n" +
               "\n" +
               "class " + className + "Test {\n" +
               "    @Test\n" +
               "    void testSomething() {\n" +
               "        // Arrange\n" +
               "        // ...\n" +
               "        // Act\n" +
               "        // ...\n" +
               "        // Assert\n" +
               "        // ...\n" +
               "    }\n" +
               "}";
    }
}