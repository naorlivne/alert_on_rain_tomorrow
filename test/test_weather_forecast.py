from unittest import TestCase
from alert_on_rain.functions.weather_forecast.forecast import *
from parse_it import ParseIt


parser = ParseIt(recurse=False)
owm_api_key = parser.read_configuration_variable("owm_api_key", required=True)


class BaseTests(TestCase):

    def test_weather_forecast_init(self):
        owm_object = WeatherForecast(owm_api_key, "Tel Aviv", "IL")
        pass

    def test_weather_forecast_rain_tomorrow(self):
        reply = "some_kind_of_test_here"
        self.assertIsNone(reply)
