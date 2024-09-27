// Adapter that converts LegacyPaymentProcessor to the Payment interface
class PaymentAdapter implements Payment {
    private final LegacyPaymentProcessor legacyPaymentProcessor;

    public PaymentAdapter(LegacyPaymentProcessor legacyPaymentProcessor) {
        this.legacyPaymentProcessor = legacyPaymentProcessor;
    }

    @Override
    public double getAmount() {
        String details = legacyPaymentProcessor.processPayment();
        return Double.parseDouble(details.split(":")[1].trim().split(" ")[0]); // Extract amount
    }

    @Override
    public String getCurrency() {
        String details = legacyPaymentProcessor.processPayment();
        return details.split(" ")[1]; // Extract currency
    }
}
