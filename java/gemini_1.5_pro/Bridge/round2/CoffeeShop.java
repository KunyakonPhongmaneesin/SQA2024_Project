// CoffeeShop.java
public class CoffeeShop {
    public static void main(String[] args) {
        // Arrange
        Beverage espresso = new Espresso();
        Size smallEspresso = new Small(espresso);

        Beverage cappuccino = new Cappuccino();
        Size largeCappuccino = new Large(cappuccino);

        // Act & Assert (implicit - using console output for demo)
        System.out.println(smallEspresso.getDescription() + ": $" + smallEspresso.getCost());
        System.out.println(largeCappuccino.getDescription() + ": $" + largeCappuccino.getCost()); 
    }
}