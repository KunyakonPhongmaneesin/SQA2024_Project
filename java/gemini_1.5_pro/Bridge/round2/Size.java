// Size.java
public abstract class Size {
    protected Beverage beverage;

    public Size(Beverage beverage) {
        this.beverage = beverage;
    }

    public abstract String getDescription();
    public abstract double getCost();
}