public class Main {

    public static void main(String[] args) {
        // Get the code to test
        String codeToTest = "public class Calculator {\n" +
                            "    public int add(int a, int b) {\n" +
                            "        if (a > 0 && b > 0) {\n" +
                            "            return a + b;\n" +
                            "        } else {\n" +
                            "            return 0;\n" +
                            "        }\n" +
                            "    }\n" +
                            "}";

        // Use the Adapter pattern
        JUnitTestGenerator generator = new BranchCoverageJUnitGenerator(new SimpleJUnitGenerator());
        String testCode = generator.generateTestCode("Calculator", codeToTest);

        // Print the generated test code
        System.out.println(testCode);
    }
}