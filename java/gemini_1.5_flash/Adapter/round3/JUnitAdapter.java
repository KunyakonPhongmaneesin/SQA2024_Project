class JUnitAdapter implements CodeGenerator {
    private final JUnitGenerator jUnitGenerator;

    public JUnitAdapter(JUnitGenerator jUnitGenerator) {
        this.jUnitGenerator = jUnitGenerator;
    }

    @Override
    public String generateCode(String requirements) {
        // Adapt the Adaptee's functionality to match the Target Interface
        return jUnitGenerator.generateJUnit(requirements);
    }
} 