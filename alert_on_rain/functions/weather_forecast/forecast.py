from pyowm.utils import timestamps
from pyowm.owm import OWM
from typing import Tuple, Optional


class WeatherForecast:

    def __init__(self, api_key: str, city: str, country_code: str):
        """
        Will create a OWM object daily forecaster object

        Arguments:
            :param api_key: the OpenWeatherMap api key
            :param city: the city where to get the prediction for, use https://openweathermap.org/find to locate yours
            :param country_code: the 2 capital letters country code where the city is located at
            if not set
        """

        owm = OWM('your-api-key')
        self.mgr = owm.weather_manager()
        self.daily_forecaster = self.mgr.forecast_at_place(city + "," + country_code, 'daily')

    def rain_tomorrow(self):
        """
        Checks if it will rain tomorrow

        Returns:
            :return bool, True if it will be rainy, False otherwise

        """
        tomorrow = timestamps.tomorrow()
        return self.daily_forecaster.will_be_rainy_at(tomorrow)
