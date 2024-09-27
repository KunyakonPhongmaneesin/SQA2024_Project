// Large.java
public class Large extends Size {
    public Large(Beverage beverage) {
        super(beverage);
    }

    @Override
    public String getDescription() {
        return "Large " + beverage.getDescription();
    }

    @Override
    public double getCost() {
        return beverage.getCost() + 1.00; 
    }
}