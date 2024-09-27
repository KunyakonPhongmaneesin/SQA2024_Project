import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class PaymentAdapterTest {

    @Test
    void testGetAmountAndCurrency() {
        // Arrange
        LegacyPaymentProcessor legacyPaymentProcessor = new LegacyPaymentProcessor();
        Payment payment = new PaymentAdapter(legacyPaymentProcessor);

        // Act
        double amount = payment.getAmount();
        String currency = payment.getCurrency();

        // Assert
        assertEquals(100.00, amount);
        assertEquals("USD", currency);
    }
}
