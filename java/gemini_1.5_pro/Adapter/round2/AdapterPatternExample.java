public class AdapterPatternExample {
    public static void main(String[] args) {
        JUnitLibrary jUnitLib = new JUnitLibrary();
        CodeGenerator codeGenerator = new JUnitAdapter(jUnitLib);

        String requirements = "Calculate the sum of two numbers.";
        String generatedCode = codeGenerator.generateCode(requirements);
        String generatedUnitTest = codeGenerator.generateUnitTest(generatedCode);

        System.out.println("Generated Code:\n" + generatedCode);
        System.out.println("\nGenerated Unit Test:\n" + generatedUnitTest);
    }
}