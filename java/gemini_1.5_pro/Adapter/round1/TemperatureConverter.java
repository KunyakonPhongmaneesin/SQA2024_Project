public class TemperatureConverter {
    public static void main(String[] args) {
        // Arrange
        CelsiusTemperature celsiusTemperature = new CelsiusTemperature(25);
        FahrenheitTemperature fahrenheitTemperature = new CelsiusToFahrenheitAdapter(celsiusTemperature);

        // Act
        double convertedTemperature = fahrenheitTemperature.getTemperature();

        // Assert (Implicit - output to console)
        System.out.println("Celsius: " + celsiusTemperature.getTemperature());
        System.out.println("Fahrenheit: " + convertedTemperature);
    }
}