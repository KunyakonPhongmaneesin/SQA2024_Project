import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CodeGenerationExampleTest {

    @Test
    void testGenerateCode() {
        // Arrange
        CodeGenerator generator = new JUnitAdapter(new JUnitGenerator());
        String code = "public class MyClass { ... }";

        // Act
        String generatedTests = generator.generateCode(code);

        // Assert
        assertTrue(generatedTests.contains("Generated JUnit tests:"));
    }
}