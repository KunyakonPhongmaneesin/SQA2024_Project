// Medium.java
public class Medium extends Size {
    public Medium(Beverage beverage) {
        super(beverage);
    }

    @Override
    public String getDescription() {
        return "Medium " + beverage.getDescription();
    }

    @Override
    public double getCost() {
        return beverage.getCost() + 0.50; 
    }
}