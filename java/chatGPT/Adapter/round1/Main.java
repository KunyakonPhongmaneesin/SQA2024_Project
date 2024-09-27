

public class Main {
    public static void main(String[] args) {
        LegacyLogger legacyLogger = new LegacyLogger();
        Logger logger = new LoggerAdapter(legacyLogger);
        
        logger.log("This is a test log message.");
    }
}
