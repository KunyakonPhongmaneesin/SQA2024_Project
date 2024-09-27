public interface CodeGenerator {
    String generateCode(String requirements);
    String generateUnitTest(String code);
}