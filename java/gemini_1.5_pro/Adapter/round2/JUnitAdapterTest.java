import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class JUnitAdapterTest {

    @Test
    void testGenerateUnitTest() {
        // Arrange
        JUnitLibrary mockJUnitLib = new JUnitLibrary();
        CodeGenerator adapter = new JUnitAdapter(mockJUnitLib);
        String code = "// Sample code";

        // Act
        String generatedTest = adapter.generateUnitTest(code);

        // Assert
        assertTrue(generatedTest.contains("Generated JUnit Test with 100% Branch Coverage:"));
        assertTrue(generatedTest.contains(code + "_Test"));
    }
}