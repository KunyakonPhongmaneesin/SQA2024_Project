import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class BasicJUnitGenerator implements JUnitTestGenerator {

    @Override
    public String generateTestCode(String className, String codeToTest) {
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