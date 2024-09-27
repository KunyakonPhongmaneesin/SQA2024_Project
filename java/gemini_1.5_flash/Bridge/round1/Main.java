public class Main {

    public static void main(String[] args) {
        // Get the code to test
        String codeToTest = "public class StringManipulator {\n" +
                            "    public String reverseString(String str) {\n" +
                            "        if (str == null || str.isEmpty()) {\n" +
                            "            return str;\n" +
                            "        } else {\n" +
                            "            return new StringBuilder(str).reverse().toString();\n" +
                            "        }\n" +
                            "    }\n" +
                            "}";

        // Use the Bridge pattern
        JUnitTestGenerator generator = new JUnitGeneratorImpl(new BranchCoverageStrategy());
        String testCode = generator.generateTestCode("StringManipulator", codeToTest);

        // Print the generated test code
        System.out.println(testCode);
    }
}