from unittest import TestCase
from alert_on_rain.functions.weather_forecast.forecast import *
from parse_it import ParseIt


parser = ParseIt(recurse=False)
owm_api_key = parser.read_configuration_variable("owm_api_key", required=True)


class BaseTests(TestCase):

    def test_weather_forecast_init(self):
        owm_object = WeatherForecast(owm_api_key, "Tel Aviv", "IL")
        self.assertEqual(owm_object.three_hour_forecast.forecast.interval, "3h")

    def test_weather_forecast_rain_tomorrow(self):
        owm_object = WeatherForecast(owm_api_key, "Tel Aviv", "IL")
        rain_tomorrow = owm_object.rain_tomorrow()
        self.assertIsInstance(rain_tomorrow, bool)
