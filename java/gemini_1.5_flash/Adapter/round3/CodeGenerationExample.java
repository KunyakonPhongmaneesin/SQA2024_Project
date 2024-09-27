public class CodeGenerationExample {
    public static void main(String[] args) {
        // Use the Adapter to generate JUnit tests
        CodeGenerator generator = new JUnitAdapter(new JUnitGenerator());
        String code = "public class MyClass { ... }";
        String generatedTests = generator.generateCode(code);
        System.out.println(generatedTests);
    }
} 