// Small.java
public class Small extends Size {
    public Small(Beverage beverage) {
        super(beverage);
    }

    @Override
    public String getDescription() {
        return "Small " + beverage.getDescription();
    }

    @Override
    public double getCost() {
        return beverage.getCost(); // No extra cost for Small
    }
}