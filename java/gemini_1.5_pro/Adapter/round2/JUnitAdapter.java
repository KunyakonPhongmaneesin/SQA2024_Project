public class JUnitAdapter implements CodeGenerator {
    private JUnitLibrary jUnitLibrary;

    public JUnitAdapter(JUnitLibrary jUnitLibrary) {
        this.jUnitLibrary = jUnitLibrary;
    }

    @Override
    public String generateCode(String requirements) {
        // Implement logic if needed, or delegate to another class
        return "// Code generated from requirements: " + requirements;
    }

    @Override
    public String generateUnitTest(String code) {
        return jUnitLibrary.generateJUnitTest(code);
    }
} 