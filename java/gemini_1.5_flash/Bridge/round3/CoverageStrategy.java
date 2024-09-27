public interface CoverageStrategy {
    String generateTests(String className, String codeToTest);
}