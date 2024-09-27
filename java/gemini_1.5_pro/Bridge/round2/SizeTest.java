// SizeTest.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SizeTest {

    @Test
    void testGetDescriptionAndCost() {
        // Arrange
        Beverage espresso = new Espresso();
        Beverage cappuccino = new Cappuccino();

        Size smallEspresso = new Small(espresso);
        Size mediumEspresso = new Medium(espresso);
        Size largeCappuccino = new Large(cappuccino);

        // Act & Assert
        assertEquals("Small Espresso", smallEspresso.getDescription());
        assertEquals(2.50, smallEspresso.getCost()); 

        assertEquals("Medium Espresso", mediumEspresso.getDescription());
        assertEquals(3.00, mediumEspresso.getCost());

        assertEquals("Large Cappuccino", largeCappuccino.getDescription());
        assertEquals(4.00, largeCappuccino.getCost()); 
    }
}