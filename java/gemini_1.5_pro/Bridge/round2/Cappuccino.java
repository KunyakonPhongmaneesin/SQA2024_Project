// Cappuccino.java
public class Cappuccino implements Beverage {
    @Override
    public String getDescription() {
        return "Cappuccino";
    }

    @Override
    public double getCost() {
        return 3.00;
    }
}