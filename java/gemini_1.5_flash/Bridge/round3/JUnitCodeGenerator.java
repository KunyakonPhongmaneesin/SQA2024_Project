class JUnitCodeGenerator implements CodeGenerator {
    private final CodeGenerationStrategy strategy;

    public JUnitCodeGenerator(CodeGenerationStrategy strategy) {
        this.strategy = strategy;
    }

    @Override
    public String generateCode(String requirements) {
        return strategy.generateCode(requirements);
    }
}