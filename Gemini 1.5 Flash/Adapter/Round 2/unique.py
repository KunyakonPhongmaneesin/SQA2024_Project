class WeatherData:
    def get_temperature(self):
        return 25

class TemperatureSensorAdapter:
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def read_temperature(self):
        return self.weather_data.get_temperature() + 1  # Add a calibration offset