public class CelsiusToFahrenheitAdapter implements FahrenheitTemperature {
    private CelsiusTemperature celsiusTemperature;

    public CelsiusToFahrenheitAdapter(CelsiusTemperature celsiusTemperature) {
        this.celsiusTemperature = celsiusTemperature;
    }

    @Override
    public double getTemperature() {
        return celsiusTemperature.getTemperature() * 9.0 / 5.0 + 32;
    }
}