public class FahrenheitTemperature implements Temperature {
    private double fahrenheit;

    public FahrenheitTemperature(double fahrenheit) {
        this.fahrenheit = fahrenheit;
    }

    @Override
    public double getTemperature() {
        return fahrenheit;
    }
}