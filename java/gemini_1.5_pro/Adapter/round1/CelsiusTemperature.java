public class CelsiusTemperature implements Temperature {
    private double celsius;

    public CelsiusTemperature(double celsius) {
        this.celsius = celsius;
    }

    @Override
    public double getTemperature() {
        return celsius;
    }
}