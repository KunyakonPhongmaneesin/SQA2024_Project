public class JUnitGeneratorImpl implements JUnitTestGenerator {

    private final CoverageStrategy coverageStrategy;

    public JUnitGeneratorImpl(CoverageStrategy coverageStrategy) {
        this.coverageStrategy = coverageStrategy;
    }

    @Override
    public String generateTestCode(String className, String codeToTest) {
        return coverageStrategy.generateTests(className, codeToTest);
    }
}